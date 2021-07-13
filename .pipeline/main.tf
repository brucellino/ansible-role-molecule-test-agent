terraform {
  backend "s3" {
    bucket = "tfmod-test"
    key    = "ansible-role-test-agent"
    region = "eu-central-1"
  }
}
# This is an example for EC2 instances.
# Provisions two EC2 instances: focal and bionic
# along with relevant VPC resources

module "instance" {
  source = "github.com/UEFADigital/tfmod-ansible-test-harness"
  bionic = false
  focal  = true
  docker = false
  ec2    = true
}

output "focal_ip" {
  value = module.instance.focal_instance_ip
}

output "bionic_ip" {
  value = module.instance.bionic_instance_ip
}

output "ssh_key" {
  value = module.instance.ssh_priv_key_file
}
