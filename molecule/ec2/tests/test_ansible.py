import os
# import pytest
import re
# from distutils.version import LooseVersion
import testinfra.utils.ansible_runner

ansible_test_command = (
    ". /opt/virtualenv/molecule/bin/activate " + " ; ansible --version"
)
molecule_test_command = (
    ". /opt/virtualenv/molecule/bin/activate" + " ; molecule --version"
)
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_ansible_venv(host):
    """
    Check that ansible is installed in virtualenv
    and is executable with the correct Python env
    """

    assert "ansible" in host.pip_package.get_packages(
        pip_path="/opt/virtualenv/molecule/bin/pip"
    )

    ansible_command = host.run(ansible_test_command)
    assert ansible_command.rc == 0

    assert "ansible 2.9.2" in ansible_command.stdout
    # the python version is on the last line of the output
    # We convert the command output to a list of lines, then
    # match the regex on the last one.
    assert re.match(r"^\s+python version = 3.6.\d.*$",
                    ansible_command.stdout.splitlines()[-1], re.M)


def test_molecule_venv(host):
    """
    Check that molecule is available in the virtualenv
    and is executable with the right dependecies
    """

    assert "molecule" in host.pip_package.get_packages(
        pip_path="/opt/virtualenv/molecule/bin/pip"
    )
    molecule_command = host.run(molecule_test_command)

    assert molecule_command.rc == 0
    assert "2.22" in molecule_command.stdout


def test_aws_provisioner(host):
    """
    Try to use the boto library to interact with AWS
    Requires credentials
    """

    assert True
