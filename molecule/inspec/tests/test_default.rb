# frozen_string_literal: true

# Molecule managed

describe file('/etc/hosts') do
  its('owner') { should eq 'root' }
  its('group') { should eq 'root' }
  its('mode') { should cmp '0644' }
end

# https://inspec.io/docs/reference/resources/gem/
describe gem('rubocop') do
  it { should be_installed }
  its('version') { should cmp >= '0.82.0' }
end

# https://inspec.io/docs/reference/resources/command/
describe command('rubocop --version') do
  its('stdout') { should match('0.82.0') }
  its('stderr') { should_not match(/.*/) }
  its('exit_status') { should eq 0 }
end
