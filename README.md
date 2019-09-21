# Molecule Test Agent

This role provisions an environment in which to test Ansible roles.
In order to test Ansible roles, you probably want to do a few things:

1. Ensure adherence to a style guide
2. Ensure proper code and quality checks
3. Ensure functional test coverage

## Requirements

None.

## Role Variables

Variable Name | Variable Description
--------------|---------------------
`ruby_packages` | OS-dependent name of the ruby package to install

## Dependencies

None.

## Example Playbook

Add this role to your requirements as such

```yaml
# requrements.yml
- name: brucellino.test_agent
  src: https://github.com/brucellino/ansible-role-molecule-test-agent
  version: master
```

Then write your playbook to use it.

```yaml
    - hosts: servers
      roles:
         - { role: brucellino.test_agent }
```

## Test coverage and scenarios

Test Name | Description | Scenarios
---------|-----------|------------
`test_connectivity` | Assert connectivity to Chef SuperMarket | Default
`test_inspec`       | Assert ability to run Inspec | Default

## License

Apache

## Author Information

Bruce Becker

### Housekeeping

- Use prettier to keep yaml and markdown in the right shape:
  - `find . -name "*.md" -exec prettier --write --single-quote=true --prose-wrap=always {} \;`
  - `find . -name *.yml -exec prettier --write {} \;`
