import os

import testinfra.utils.ansible_runner

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


def test_inspec(host):
    '''
    Check that we can execute inspec in a basic way and that
    the inspec variable is a sane version
    '''
    assert host.exists('inspec')
