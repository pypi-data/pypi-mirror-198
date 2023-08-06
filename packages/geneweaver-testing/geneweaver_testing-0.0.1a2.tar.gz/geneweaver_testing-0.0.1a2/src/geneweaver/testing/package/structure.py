from .utils import find_root_dir, get_package_name_from_pyproject

__all__ = [
    "test_has_src_directory",
    "test_has_geneweaver_directory",
    "test_geneweaver_dir_is_namespace_package",
    "test_has_package_directory",
    "test_has_tests_directory",
]


def test_has_src_directory():
    """Test that the src directory exists."""
    assert (
        find_root_dir() / "src"
    ).is_dir(), '"src" directory expected at root of git repository'


def test_has_geneweaver_directory():
    """Test that the geneweaver namespace exists."""
    assert (
        find_root_dir() / "src" / "geneweaver"
    ).is_dir(), '"geneweaver" namespace expected in "src" directory'


def test_geneweaver_dir_is_namespace_package():
    """Test that the geneweaver namespace is a namespace package."""
    assert (
        find_root_dir() / "src" / "geneweaver" / "__init__.py"
    ).is_file() is False, (
        '"geneweaver" namespace is not a namespace package, '
        "it should not have an __init__.py file"
    )


def test_has_package_directory():
    """Test that the package directory exists."""
    package_name = get_package_name_from_pyproject()
    package_postfix = package_name.split("-")[-1]
    assert (
        find_root_dir() / "src" / "geneweaver" / package_postfix
    ).is_dir(), (
        f'"{package_postfix}" package directory expected in "geneweaver" namespace'
    )


def test_has_tests_directory():
    """Test that the tests directory exists."""
    assert (
        find_root_dir() / "tests"
    ).is_dir(), '"tests" directory expected at root of git repository'
