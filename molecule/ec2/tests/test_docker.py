import os

# from distutils.version import LooseVersion
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


try:
    quay_user = os.environ["QUAY_USER"]
except KeyError:
    print("QUAY_USER environment variable not set")
try:
    quay_pass = os.environ["QUAY_PASS"]
except KeyError:
    print("QUAY_PASS environment variable not set")


def test_docker_1(host):
    """
    Test presence and functionality of Docker engine
    """
    with host.sudo("root"):
        assert host.exists('docker')
        version_info = host.run("docker version")
        assert version_info.rc == 0


def test_docker_service(host):
    """
    Test that the docker daemon is running
    """
    dockerd = host.service('docker')

    assert dockerd.is_running


def test_hello_world(host):
    with host.sudo("root"):
        execute = host.run("docker run hello-world")
        assert execute.succeeded


def test_hello_world_jenkins(host):
    with host.sudo("jenkins"):
        execute = host.run("docker run hello-world")
        assert execute.succeeded


def test_hello_world_ubuntu(host):
    with host.sudo("ubuntu"):
        execute = host.run("docker run hello-world")
        assert execute.succeeded


def test_quay_credentials(host):
    assert True  # disabled for now
