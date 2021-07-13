#!/bin/bash
set -e
#!/usr/bin/env bash
# A script to execute pytest for the EC2 use case
# This script is intended to be executed in the context of a test matrix
# automatically, by Jenkins.

# Get the IP addresses of the instances created
FOCAL_IP=$(terraform output --json | jq -r '.focal_ip.value[0]')
SSH_KEY=$(terraform output --json | jq -r '.ssh_key.value')
pip3 install pytest-testinfra

echo "---- Focal ----"
py.test \
	--sudo \
	--ssh-identity-file="${SSH_KEY}" \
	--ssh-config=.ssh/ssh_config \
	--hosts="ssh://ubuntu@${FOCAL_IP}" test_default.py
