import pathlib
from typing import Optional, Union

import tomli


def find_file(
    start_path: str, filename: str, is_dir: bool = False
) -> Optional[pathlib.Path]:
    """
    Find a file or directory in the parent directories of a given path.
    :param start_path: The path to start searching from.
    :param filename: The name of the file or directory to find.
    :param is_dir: Whether to search for a directory or a file.
    :return: The path to the file or directory (as a pathlib.Path) if exists,
    otherwise None.
    """
    for path in pathlib.Path(start_path).parents:
        possible_path = path / filename
        if is_dir and possible_path.is_dir():
            return possible_path
        elif possible_path.is_file():
            return possible_path

    return None


def find_pyproject_toml() -> Optional[pathlib.Path]:
    """Find the pyproject.toml file, should be at the root of the git repository."""
    return find_file(__file__, "pyproject.toml")


def find_git_dir() -> Optional[pathlib.Path]:
    """Find the .git directory, should be at the root of the git repository."""
    print(__file__)
    return find_file(__file__, ".git", is_dir=True)


def find_root_dir() -> Optional[pathlib.Path]:
    """Find the root directory of the git repository."""
    git_dir = find_git_dir()
    return git_dir.parent if git_dir else None


def get_pyproject_toml_contents() -> Optional[dict]:
    """

    :return:
    """
    pyproject_path = find_pyproject_toml()
    return read_pyproject_toml(pyproject_path) if pyproject_path else None


def read_pyproject_toml(pyproject_path: Union[str, pathlib.Path]) -> dict:
    """
    Read the contents of a pyproject.toml file.
    :param pyproject_path: The path to the pyproject.toml file.
    :return: A dictionary containing the contents of the pyproject.toml file.
    """
    with open(pyproject_path, "rb") as pyproject_file:
        return tomli.load(pyproject_file)


def get_package_name_from_pyproject() -> Optional[str]:
    """Get the package name from the pyproject.toml file."""
    pyproject = get_pyproject_toml_contents()
    return pyproject["tool"]["poetry"]["name"] if pyproject else None
