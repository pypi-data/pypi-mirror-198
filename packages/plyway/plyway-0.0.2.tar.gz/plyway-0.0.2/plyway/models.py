from dataclasses import dataclass
from enum import Enum


class Command(Enum):
    MIGRATE = "migrate"
    VALIDATE = "validate"
    UNDO = "undo"


class DatabaseType(Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"
    SQLITE = "sqlite"


@dataclass
class ArgumentParserNamespace:
    config_file: str
    plyway_username: str
    plyway_password: str
    command: Command
