import yaml
import pytest


def required_packages():
    """
    Reads input.yml file and returns the list for the fixture
    """
    with open(r"required-packages.yml") as file:
        inputs = yaml.load(file, Loader=yaml.FullLoader)
    return inputs["required_packages"]


def optional_packages():
    """
    Reads input.yml and returns a list of optional
    packages for the fixture
    """
    with open(r"tests/input.yml") as file:
        inputs = yaml.load(file, Loader=yaml.FullLoader)
    return inputs["optional_packages"]


def python_packages():
    """
    Reads input.yml and returns a list of python
    related packages
    """
    with open(r"tests/input.yml") as file:
        inputs = yaml.load(file, Loader=yaml.FullLoader)
    return inputs["python_packages"]


@pytest.mark.parametrize("package_name", required_packages())
def test_required_packages(host, package_name):
    assert host.package(package_name).is_installed


# @pytest.mark.parametrize("package_name", optional_packages())
# def test_optional_packages(host, package_name):
#     assert host.package(package_name).is_installed
