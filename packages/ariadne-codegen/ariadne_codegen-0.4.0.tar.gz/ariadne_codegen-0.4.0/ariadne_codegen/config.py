import os
from dataclasses import dataclass, field, fields
from keyword import iskeyword
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, Optional
from warnings import simplefilter, warn

import toml

from .exceptions import ConfigFileNotFound, InvalidConfiguration, MissingConfiguration
from .generators.scalars import ScalarData

simplefilter("default", DeprecationWarning)


@dataclass
class Settings:
    queries_path: str
    schema_path: Optional[str] = None
    remote_schema_url: Optional[str] = None
    remote_schema_headers: dict = field(default_factory=dict)
    target_package_name: str = "graphql_client"
    target_package_path: str = field(default_factory=lambda: Path.cwd().as_posix())
    client_name: str = "Client"
    client_file_name: str = "client"
    base_client_name: Optional[str] = None
    base_client_file_path: Optional[str] = None
    enums_module_name: str = "enums"
    input_types_module_name: str = "input_types"
    include_comments: bool = True
    convert_to_snake_case: bool = True
    async_client: bool = True
    files_to_include: List[str] = field(default_factory=list)
    plugins: List[str] = field(default_factory=list)
    scalars: Dict[str, ScalarData] = field(default_factory=dict)

    def __post_init__(self):
        if not self.schema_path and not self.remote_schema_url:
            raise InvalidConfiguration(
                "Schema source not provided. Use schema_path or remote_schema_url"
            )

        self._set_default_base_client_data()

        if self.schema_path:
            self._assert_path_exists(self.schema_path)
        self._assert_path_exists(self.queries_path)

        self._assert_string_is_valid_python_identifier(self.target_package_name)
        self._assert_path_is_valid_directory(self.target_package_path)

        self._assert_string_is_valid_python_identifier(self.client_name)
        self._assert_string_is_valid_python_identifier(self.client_file_name)
        self._assert_string_is_valid_python_identifier(self.base_client_name)
        self._assert_path_exists(self.base_client_file_path)
        self._assert_path_is_valid_file(self.base_client_file_path)
        self._assert_class_is_defined_in_file(
            Path(self.base_client_file_path), self.base_client_name
        )

        self._assert_string_is_valid_python_identifier(self.enums_module_name)
        self._assert_string_is_valid_python_identifier(self.input_types_module_name)

        for file_path in self.files_to_include:
            self._assert_path_is_valid_file(file_path)

        self._resolve_remote_schema_headers()

    def _set_default_base_client_data(self):
        if not self.base_client_name and not self.base_client_file_path:
            generators_path = Path(__file__).parent / "generators" / "dependencies"
            if self.async_client:
                self.base_client_file_path = generators_path.joinpath(
                    "async_base_client.py"
                ).as_posix()
                self.base_client_name = "AsyncBaseClient"
            else:
                self.base_client_file_path = generators_path.joinpath(
                    "base_client.py"
                ).as_posix()
                self.base_client_name = "BaseClient"

    def _assert_path_exists(self, path: str):
        if not Path(path).exists():
            raise InvalidConfiguration(f"Provided path {path} doesn't exist.")

    def _assert_path_is_valid_directory(self, path: str):
        if not Path(path).is_dir():
            raise InvalidConfiguration(f"Provided path {path} isn't a directory.")

    def _assert_path_is_valid_file(self, path: str):
        if not Path(path).is_file():
            raise InvalidConfiguration(f"Provided path {path} isn't a file.")

    def _assert_string_is_valid_python_identifier(self, name: str):
        if not name.isidentifier() and not iskeyword(name):
            raise InvalidConfiguration(
                f"Provided name {name} cannot be used as python indetifier"
            )

    def _assert_class_is_defined_in_file(self, file_path: Path, class_name: str):
        file_content = file_path.read_text()
        if f"class {class_name}" not in file_content:
            raise InvalidConfiguration(f"Cannot import {class_name} from {file_path}")

    def _resolve_remote_schema_headers(self):
        self.remote_schema_headers = {
            key: self._get_header_value(value)
            for key, value in self.remote_schema_headers.items()
        }

    def _get_header_value(self, value: str) -> str:
        env_var_prefix = "$"
        if value.startswith(env_var_prefix):
            env_var_name = value.lstrip(env_var_prefix)
            var_value = os.environ.get(env_var_name)
            if not var_value:
                raise InvalidConfiguration(
                    f"Environment variable {env_var_name} not found."
                )
            return var_value

        return value


def get_config_file_path(file_name: str = "pyproject.toml") -> Path:
    """Get config file path. If not found raise exception."""
    directory = Path.cwd()
    while not directory.joinpath(file_name).exists():
        if directory == directory.parent:
            raise ConfigFileNotFound(f"Config file {file_name} not found.")
        directory = directory.parent
    return directory.joinpath(file_name).resolve()


def get_config_dict(config_file_name: Optional[str] = None) -> Dict:
    """Get config dict."""
    if config_file_name:
        config_file_path = get_config_file_path(config_file_name)
    else:
        config_file_path = get_config_file_path()

    return toml.load(config_file_path)


def parse_config_dict(config_dict: Dict) -> Settings:
    """
    Parse configuration from toml file. Raise exception if section or key was not found.
    """
    section = get_section(config_dict)
    try:
        section["scalars"] = {
            name: ScalarData(
                type_=data["type"],
                serialize=data.get("serialize"),
                parse=data.get("parse"),
                import_=data.get("import"),
            )
            for name, data in section.get("scalars", {}).items()
        }
    except KeyError as exc:
        raise MissingConfiguration(
            "Missing 'type' field for scalar definition"
        ) from exc

    try:
        return Settings(**section)
    except TypeError as exc:
        expected_fields = {f.name for f in fields(Settings)}
        missing_fields = expected_fields.difference(section)
        raise MissingConfiguration(
            f"Missing configuration fields: {', '.join(missing_fields)}"
        ) from exc


def get_section(config_dict: Dict) -> Dict:
    """Get section from config dict."""
    tool_key = "tool"
    codegen_key = "ariadne-codegen"
    if tool_key in config_dict and codegen_key in config_dict.get(tool_key, {}):
        return config_dict[tool_key][codegen_key]

    if codegen_key in config_dict:
        warn(
            f"Support for [{codegen_key}] section has been deprecated "
            "and will be dropped in future release. "
            f"Instead use [{tool_key}.{codegen_key}].",
            DeprecationWarning,
            stacklevel=2,
        )
        return config_dict[codegen_key]

    raise MissingConfiguration(f"Config has no [{tool_key}.{codegen_key}] section.")


def get_used_settings_message(settings: Settings) -> str:
    comments_msg = (
        "Including comments."
        if settings.include_comments
        else "Not including comments."
    )
    snake_case_msg = (
        "Converting fields and arguments name to snake case."
        if settings.convert_to_snake_case
        else "Not converting fields and arguments name to snake case."
    )
    async_client_msg = (
        "Generating async client."
        if settings.async_client
        else "Generating not async client."
    )
    files_to_include_list = ",".join(settings.files_to_include)
    return dedent(
        f"""\
        Using schema from '{settings.schema_path}'.
        Reading queries from '{settings.queries_path}'.
        Using '{settings.target_package_name}' as package name.
        Generating package into '{settings.target_package_path}'.
        Using '{settings.client_name}' as client name.
        Using '{settings.base_client_name}' as base client class.
        Coping base client class from '{settings.base_client_file_path}'.
        Generating enums into '{settings.enums_module_name}.py'.
        Generating inputs into '{settings.input_types_module_name}.py'.
        {comments_msg}
        {snake_case_msg}
        {async_client_msg}
        Coping following files into package: {files_to_include_list}
        """
    )
