# Ansible Role Test Agent

_**Note:** this role previously referred to the use of [Molecule](https://molecule.readthedocs.io) to provision and converge environments. Due to divergence in features in Molecule, we no longer use it for this function, relying instead on a [Terraform module](https://github.com/UEFADigital/tfmod-ansible-test-harness)_

This role provisions an environment in which to test Ansible roles. In order to
test Ansible roles, you probably want to do a few things:

1. Ensure adherence to a style guide
2. Ensure proper code and quality checks
3. Ensure functional test coverage

This role provides the execution environment for running these tasks, typically
in a containerised environment.

The role adds the following tools:

- Python, pip, virtual environment (only Python3)
- [Ansible](https://docs.ansible.com/ansible) (as a dependency of Molecule)
- Ruby (required for executing [Inspec](https://inspec.io) tests)
- [Inspec](https://inspec.io) executable

## Requirements

**This role has to be bootstrapped**, since it is used to test itself. This can
be done by running the role against the control machine. In order to lint
scenarios using the `inspec` verifier, we need `rubocop` on the control node.

## Role Variables

| Variable Name           | Variable Description                                 |
| ----------------------- | ---------------------------------------------------- |
| `rvm_gpg_keys`          | GPG keys of the Ruby Version Manager maintainers     |
| `dev_sec_prerequisites` | Prerequisites for the Dev-Sec Inspec profile         |
| `prerequisites`         | OS-dependent list of packages needed as prerequisite |
| `inspec_version`        | Version of Chef Inspec to install                    |

## Dependencies

You will need a means to create the initial state. We typically use a [Terraform module](https://github.com/UEFADigital/tfmod-ansible-test-harness)

## Example Playbook

Add this role to your requirements as such

```yaml
# requrements.yml
- name: uefa_devops.test_agent
  src: https://github.com/UEFADigital/ansible-role-test-agent
  version: master
```

Then write your playbook to use it.

```yaml
- hosts: servers
  roles:
    - { role: uefa_devops.test_agent }
```

## Test coverage and scenarios

| Test Name              | Description                                    | Scenarios |
| ---------------------- | ---------------------------------------------- | --------- |
| `test_connectivity`    | Assert connectivity to Chef SuperMarket        | Default   |
| `test_inspec`          | Assert ability to run Inspec                   | Default   |
| `test_inspect_profile` | Assert that an Inspect profile can be executed | Default   |
| `test_ansible`         | Assert that Ansible can be executed            | default   |

## Artefacts

Beware: circular dependency ! **This role uses artifacts produced by itself to
test itself**. In order to execute the continuous delivery pipeline, an
execution agent is needed _with the same environment that this role expresses_.
This is a bootstrapping problem which needs to be broken the first time by
executing the build and delivery by hand.

[Packer](https://packer.io) is used to create executable artefacts in different
envrionments (AWS, Docker)

## License

Apache

## Author Information

Bruce Becker, UEFA DevOps

### Housekeeping

- Use prettier to keep yaml and markdown in the right shape:
  - `find . -name "*.md" -exec prettier --write --single-quote=true --prose-wrap=always {} \;`
  - `find . -name *.yml -exec prettier --write {} \;`
