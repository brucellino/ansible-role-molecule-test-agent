import os
# import pytest
from distutils.version import LooseVersion
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")
inspec_test_command = (
    ". /opt/virtualenv/molecule/bin/activate " + " ; ansible --version"
)
dev_sec_profile = "dev-sec/linux-baseline"


def test_inspec(host):
    """
    Check that we can execute inspec in a basic way and that
    the inspec variable is a sane version
    """
    inspec = host.package("inspec")
    assert host.exists("inspec")
    assert LooseVersion(inspec.version) > LooseVersion("4.7")


def test_inspect_profile(host):
    """
    We should be able to execute a dummy inspec profile against this host
    """

    cmd = "inspec supermarket info " \
        + dev_sec_profile \
        + " --chef-license=accept-silent"
    inspec_command = host.run(cmd)
    assert inspec_command.rc == 0
