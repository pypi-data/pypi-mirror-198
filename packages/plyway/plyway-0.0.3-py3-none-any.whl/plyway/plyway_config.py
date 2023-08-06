import os
from dataclasses import dataclass, field
from typing import Self, Type

import tomllib

from plyway.exceptions import InvalidConfigFileException
from plyway.models import ArgumentParserNamespace, DatabaseType

_DEFAULT_CONFIG_FILE_PATH = "pyproject.toml"


@dataclass
class PlywayConfig:
    database_type: DatabaseType
    username: str
    password: str
    host: str
    port: int
    params: dict[str, str] = field(default_factory=dict)
    migration_path: str = field(default="migrations")

    def __post_init__(self):
        if isinstance(self.database_type, str):
            self.database_type = DatabaseType(self.database_type)

    @classmethod
    def from_namespace(cls: Type[Self], ns: ArgumentParserNamespace) -> Self:
        config_path = ns.config_file if ns.config_file else _DEFAULT_CONFIG_FILE_PATH

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Cannot find plyway config file '{config_path}'.")

        if os.path.splitext(config_path)[1] != ".toml":
            raise InvalidConfigFileException(
                f"Config file at path '{config_path}' is not a TOML file."
            )

        with open(config_path, "rb") as fp:
            parsed_toml = tomllib.load(fp)

        if "tool" not in parsed_toml or "plyway" not in parsed_toml["tool"]:
            raise KeyError(
                f"Cannot find 'tool.plyway' section in file '{config_path}'."
            )

        config_args = {
            "username": ns.plyway_username,
            "password": ns.plyway_password,
        } | parsed_toml["tool"]["plyway"]
        return cls(**config_args)
