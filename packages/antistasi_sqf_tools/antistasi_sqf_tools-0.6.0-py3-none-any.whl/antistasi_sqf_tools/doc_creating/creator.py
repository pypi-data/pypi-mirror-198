"""
WiP.

Soon.
"""

# region [Imports]

# * Standard Library Imports ---------------------------------------------------------------------------->
import os
import sys
from typing import TextIO
import json
import pickle
import platform
import subprocess
from typing import Union
from pathlib import Path

# * Third Party Imports --------------------------------------------------------------------------------->
from sphinx.cmd.build import main as sphinx_build

# * Local Imports --------------------------------------------------------------------------------------->
from antistasi_sqf_tools import CONSOLE
from antistasi_sqf_tools.doc_creating.env_handling import EnvManager
from antistasi_sqf_tools.doc_creating.config_handling import DocCreationConfig
from antistasi_sqf_tools.doc_creating.isolated_build_env import IsolatedBuildEnvironment
from antistasi_sqf_tools.doc_creating.preprocessing.preprocessor import PreProcessor

# endregion [Imports]

# region [TODO]


# endregion [TODO]

# region [Logging]


# endregion [Logging]

# region [Constants]

THIS_FILE_DIR = Path(__file__).parent.absolute()

# endregion [Constants]python -m fastero


class StdOutModifier:

    def __init__(self) -> None:
        self.originial_std_out: TextIO = None
        self.output_dir = None

    def set_output_dir(self, output_dir: Path):
        self.output_dir = output_dir

    def write(self, s: str):
        if s.startswith("The HTML pages are in"):
            self.originial_std_out.write(f"<original_text> {s.strip()!r}\n")
            s = f"The HTML pages are in {self.output_dir.as_posix()!r}.\n"

        self.originial_std_out.write(s)

    def __getattr__(self, name: str):
        return getattr(self.originial_std_out, name)

    def __enter__(self):
        self.originial_std_out = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.originial_std_out


def _each_part_alphabetical_length(in_label: str):

    try:
        file, section = in_label.split(":")
    except ValueError:
        file = in_label
        section = ""

    file_parts = file.split("/")

    _out = []
    for part in file_parts:
        _out.append(part)
        _out.append(len(part))
    _out.append(section)
    return tuple(_out)


LABEL_SORT_KEY_FUNCTIONS = {'parts-alphabetical-length': _each_part_alphabetical_length}


class Creator:
    label_sort_key = "parts-alphabetical-length"
    env_manager = EnvManager()

    def __init__(self, config_file: Union[str, os.PathLike], builder_name: str, base_folder: Union[str, os.PathLike] = None) -> None:
        self.builder_name = builder_name
        self.base_folder = Path(config_file).resolve().parent if base_folder is None else Path(base_folder).resolve()
        self.config = DocCreationConfig(config_file, env_manager=self.env_manager).setup()

        self.is_release = False
        if self.builder_name == "release":
            self.is_release = True
            self.builder_name = self.config.get_release_builder_name()
        self.env_manager.set_env("IS_RELEASE", self.is_release)
        self.console = CONSOLE
        self._build_env: IsolatedBuildEnvironment = None

    def post_build(self, build_success: bool = True):

        def open_in_browser(browser_name: str, use_private_browser: bool, file_path: Path):
            browser_name = browser_name.strip().casefold()
            if browser_name == "firefox":
                args = ["firefox", "-private-window"] if use_private_browser is True else ["firefox"]

            if browser_name == "chrome":
                args = ["chrome", "--incognito"] if use_private_browser is True else ["chrome"]

            # args.append(file_path.resolve().as_uri())
            args.append(file_path.resolve())

            startup_info = None

            if platform.system() == "Windows":
                startup_info = subprocess.STARTUPINFO()
                startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            proc = subprocess.run(args, text=True, start_new_session=True, check=False, shell=False, creationflags=subprocess.DETACHED_PROCESS, startupinfo=startup_info)
            if proc.stderr:
                print(proc.stderr)

        if build_success is True:

            if self.is_release is False:

                if self.config.local_options["auto_open"] is True and self.is_release is False:
                    open_in_browser(self.config.local_options["browser_for_html"], self.config.local_options["use_private_browser"], self._build_env.target.original_path.joinpath("index.html"))

            elif self.is_release is True:

                if self.config.get_create_top_level_index_link():
                    self.create_top_level_index_link_file()

    def create_top_level_index_link_file(self) -> Path:
        release_dir = self.config.get_release_output_dir().resolve()
        if "docs" in {p.casefold() for p in release_dir.parts}:
            index_link_file_dir = release_dir
            while index_link_file_dir.is_dir() is False or index_link_file_dir.name.casefold() != "docs":
                index_link_file_dir = index_link_file_dir.parent

        else:
            index_link_file_dir = release_dir.parent

        index_link_file_path = index_link_file_dir.joinpath("index.html")
        source_index_file_path = release_dir.joinpath("index.html")

        rel_source_index_file_path = source_index_file_path.relative_to(index_link_file_path.parent)
        index_link_file_path.write_text(f"""<meta http-equiv="refresh" content="0; url=./{rel_source_index_file_path.as_posix()}" />""")

    def pre_build(self) -> None:

        preprocessor_conf_file = self._build_env.source.temp_path.joinpath("preprocessing_conf.py")
        if preprocessor_conf_file.exists():
            self.console.print(f"Running preprocessing with preprocessor_conf_file: {preprocessor_conf_file.as_posix()!r}")
            preprocessor = PreProcessor(source_dir=self._build_env.source.temp_path, target_dir=self._build_env.target.temp_path, preprocessing_conf_file=preprocessor_conf_file, doc_creation_config=self.config)
            preprocessor.pre_process()

    def _get_all_labels(self, build_dir: Path) -> tuple[str]:
        env_pickle_file = next(build_dir.glob("**/environment.pickle"))
        with env_pickle_file.open("rb") as f:
            dat = pickle.load(f)
        raw_labels = set(dat.domaindata['std']['labels'].keys())
        try:
            return tuple(sorted(raw_labels, key=LABEL_SORT_KEY_FUNCTIONS[self.label_sort_key]))
        except Exception as e:
            self.console.rule(f"ERROR: {e!r}", style="bold red")
            self.console.print(f"While sorting labels, encountered Error {e!r}.", style="white on red")
            self.console.print_exception()
            self.console.rule(style="bold red")
            return tuple(set(raw_labels))

    def build(self):
        self.console.rule("PRE-LOADING", style="bold")
        self.console.print(f"- Trying to load env-file {self.config.local_options['env_file_to_load'].as_posix()!r}", style="bold")
        self.env_manager.load_env_file(self.config.local_options["env_file_to_load"])
        if self.is_release is True:
            return self.release()

        self._build_env = IsolatedBuildEnvironment(source_dir=self.config.get_source_dir(self), target_dir=self.config.get_output_dir(self))
        with self._build_env:
            self.pre_build()
            # args = ["-M", self.builder_name, str(self.config.get_source_dir(self)), str(temp_build_dir)]
            meta_dir = self._build_env.target.temp_path.joinpath("meta_data")
            meta_dir.mkdir(exist_ok=True, parents=True)
            args = [str(self._build_env.source.temp_path), str(self._build_env.target.temp_path), "-b", self.builder_name]

            with StdOutModifier() as mod_std_out:
                mod_std_out.set_output_dir(self._build_env.target.original_path)
                returned_code = sphinx_build(args)
                build_success = True if returned_code == 0 else False
            if build_success is True:

                label_list = self._get_all_labels(self._build_env.target.temp_path)

                available_labels_file = self._build_env.target.temp_path.joinpath("available_label.json")
                available_labels_file.parent.mkdir(exist_ok=True, parents=True)

                with available_labels_file.open("w", encoding='utf-8', errors='ignore') as f:
                    json.dump(label_list, f, indent=4, sort_keys=False, default=str)

        self.post_build(build_success)

    def release(self):
        self._build_env = IsolatedBuildEnvironment(source_dir=self.config.get_release_source_dir(), target_dir=self.config.get_release_output_dir())
        with self._build_env:
            self.pre_build()
            # args = ["-M", self.builder_name, str(self.config.get_source_dir(self)), str(temp_build_dir)]
            meta_dir = self._build_env.target.temp_path.joinpath("meta_data")
            meta_dir.mkdir(exist_ok=True, parents=True)
            args = [str(self._build_env.source.temp_path), str(self._build_env.target.temp_path), "-b", self.builder_name]

            with StdOutModifier() as mod_std_out:
                mod_std_out.set_output_dir(self._build_env.target.original_path)
                returned_code = sphinx_build(args)
                build_success = returned_code == 0
            if build_success is True:

                label_list = self._get_all_labels(self._build_env.target.temp_path)

                available_labels_file = self._build_env.target.temp_path.joinpath("available_label.json")
                available_labels_file.parent.mkdir(exist_ok=True, parents=True)

                with available_labels_file.open("w", encoding='utf-8', errors='ignore') as f:
                    json.dump(label_list, f, indent=4, sort_keys=False, default=str)

        self.post_build(build_success)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(builder_name={self.builder_name!r}, base_folder={self.base_folder.as_posix()!r}, config={self.config!r})"

# region [Main_Exec]


if __name__ == '__main__':
    pass

# endregion [Main_Exec]
