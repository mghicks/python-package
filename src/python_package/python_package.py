"""
This is a trivial Python package used to demonstrate GitHub actions
and other integrations.
"""
from pathlib import Path


def cwd() -> Path:
    """Return the current working directory."""
    return Path.cwd()


if __name__ == "__main__":
    cwd()
