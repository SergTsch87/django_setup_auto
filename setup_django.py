import os
import sys
import subprocess
import platform
from  pathlib import Path


def get_os():
    return platform.system()


def is_file(path: Path) -> bool:
    return path.is_file()


def main():
    pass


if __name__ == '__main__':
    main()