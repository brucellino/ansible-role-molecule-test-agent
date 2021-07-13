from distutils.version import LooseVersion
import pytest

dev_sec_profile = "dev-sec/linux-baseline"
ansible_test_command = (
    ". /opt/virtualenv/molecule/bin/activate " + " ; ansible --version"
)


def test_connectivity(host):
    """
    The test agent should be able to connect to the chef
    supermarket and have access to the internet
    """
    supermarket = host.addr("supermarket.chef.io")

    assert supermarket.is_resolvable
    for port in ["80", "443"]:
        assert supermarket.port(port).is_reachable


@pytest.mark.parametrize("good_python", ["python3", "pip3"])
@pytest.mark.parametrize("bad_python", ["python2", "pip2"])
def test_python(good_python, bad_python, host):
    """
    Check that python is present and that it is the right version
    """
    python = host.package("python3")
    assert python.is_installed
    assert host.exists(good_python)
    # assert not host.exists(bad_python)
    assert LooseVersion(python.version) >= LooseVersion("3.6")


@pytest.mark.parametrize("pip", [
    "boto",
    "boto3",
    "botocore",
    "molecule",
    "ansible",
    "docker"])
def test_pips(host, pip):
    """
    Check that the required pip packages are present
    """

    assert pip in host.pip.get_packages(
        pip_path="/opt/virtualenv/molecule/bin/pip"
    )


def test_ansible(host):
    """
    Check that Ansible is available with the right version
    """

    assert "ansible" in host.pip.get_packages(
        pip_path="/opt/virtualenv/molecule/bin/pip"
    )
    assert "ansible" in host.pip.get_packages(
        pip_path="/opt/virtualenv/molecule/bin/pip"
    )

    ansible_command = host.run(ansible_test_command)
    assert ansible_command.rc == 0
