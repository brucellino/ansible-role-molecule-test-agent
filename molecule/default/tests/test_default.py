import os
from distutils.version import StrictVersion, LooseVersion
import testinfra.utils.ansible_runner
import pytest
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_connectivity(host):
    '''
    The test agent should be able to connect to the chef
    supermarket and have access to the internet
    '''
    supermarket = host.addr('supermarket.chef.io')

    assert supermarket.is_resolvable
    for port in ['80', '443']:
        assert supermarket.port(port).is_reachable


@pytest.mark.parmetrize('good_pythons', [
    'python3',
    'pip3'])
@pytest.mark.parametrize('bad_pythons', [
    'python2',
    'pip2'])
def python(good_pythons, bad_pythons, host):
    '''
    Check that python is present and that it is the right version
    '''
    python = host.package('python')
    assert python.is_installed
    assert host.exists('python')
    assert host.exists(good_pythons)
    assert not host.exists(bad_pythons)
    assert LooseVersion(python.version) >= StrictVersion('3.6')


def test_inspec(host):
    '''
    Check that we can execute inspec in a basic way and that
    the inspec variable is a sane version
    '''
    inspec = host.package('inspec')
    assert host.exists('inspec')
    assert LooseVersion(inspec.version) > LooseVersion('4.7')
