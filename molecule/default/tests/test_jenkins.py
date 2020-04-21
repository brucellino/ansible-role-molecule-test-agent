import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_jenkins_user(host):
    jenkins_user = host.user('jenkins')
    assert jenkins_user.name == 'jenkins'
