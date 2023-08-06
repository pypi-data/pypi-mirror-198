import argparse
from argparse import ArgumentParser
from typing import Any, Optional


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
