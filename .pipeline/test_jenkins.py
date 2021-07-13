# Tests of the execution environment that jenkins jobs
# will execute in


def test_jenkins_user(host):
    '''
    Jenkins user should exist
    '''
    jenkins_user = host.user('jenkins')
    assert jenkins_user.name == 'jenkins'


def test_step_executables(host):
    '''
    Executables required in Jenkins steps should be available
    '''

    assert host.exists('github_changelog_generator')
    assert host.exists('rubocop')
