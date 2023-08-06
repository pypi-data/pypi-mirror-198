import argparse
import os
from argparse import ArgumentParser
from typing import Any, Optional, Sequence

from plyway.models import ArgumentParserNamespace, Command


def required(val: Optional[Any]) -> bool:
    return False if val else True


def setup_parser() -> ArgumentParser:
    """
    Sets up the ArgumentParser
    """
    # Parent Parser
    parent_parser = argparse.ArgumentParser(
        prog="plyway", description="A simple Flyway clone in Python."
    )

    # Get env variable defaults
    plyway_user = os.getenv("PLYWAY_USER")
    plyway_password = os.getenv("PLYWAY_PASSWORD")

    # plyway username
    parent_parser.add_argument(
        "-u",
        "--username",
        action="store",
        required=required(plyway_user),
        default=plyway_user,
        dest="plyway_username",
        help="Username for plyway to login to the database.",
    )

    # plyway password
    parent_parser.add_argument(
        "-p",
        "--password",
        action="store",
        required=required(plyway_password),
        default=plyway_password,
        dest="plyway_password",
        help="Password for plyway to login to the database.",
    )

    # plyway config file
    parent_parser.add_argument(
        "-c",
        "--config-file",
        action="store",
        required=False,
        dest="config_file",
        help="Location of plyway config file",
    )

    subparsers = parent_parser.add_subparsers(title="Subcommands", required=True)

    migrate_parser = subparsers.add_parser("migrate", help="Migrate the database.")
    migrate_parser.set_defaults(command=Command.MIGRATE)

    validate_parser = subparsers.add_parser("validate", help="Validate the database.")
    validate_parser.set_defaults(command=Command.VALIDATE)

    undo_parser = subparsers.add_parser(
        "undo", help="Undo the latest applied migration."
    )
    undo_parser.set_defaults(command=Command.UNDO)

    return parent_parser


def parse_args(args: Optional[Sequence[str]] = None) -> ArgumentParserNamespace:
    parser = setup_parser()
    parsed_args = parser.parse_args(args=args)
    namespace = ArgumentParserNamespace(**parsed_args.__dict__)
    return namespace
