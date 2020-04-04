import os

# from distutils.version import LooseVersion
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


try:
    quay_pass = os.environ["QUAY_USER"]
except KeyError:
    print("QUAY_USER environment variable not set")


def test_hello_world(host):
    with host.sudo("root"):
        execute = host.run("docker run hello-world")
        assert execute.succeeded


def test_quay_credentials(host):
    assert True  # disabled for now
