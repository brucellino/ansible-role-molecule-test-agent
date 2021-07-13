variable "test" {
  type    = bool
  default = true
}

variable "region" {
  type    = string
  default = "eu-central-1"
}

data "amazon-ami" "focal-ami" {
  filters = {
    virtualization-type = "hvm"
    name                = "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"
    root-device-type    = "ebs"
  }

  owners      = ["099720109477"]
  most_recent = true
}

source "amazon-ebs" "focal-ami" {
  source_ami      = local.focal_ami
  region          = var.region
  skip_create_ami = var.test
  ami_name        = "molecule-test-harness-focal"
  instance_type   = "t3.micro"
  ssh_interface   = "private_ip"
  ssh_username    = "ubuntu"

  subnet_filter {
    filters = {
      "tag:team" : "devops"
      "tag:scope" : "internal"
      "tag:bake" : "true"
      "availability-zone" : "eu-central-1a"
    }
    random = true
  }
  security_group_filter {
    filters = {
      "tag:application" : "packer"
    }
  }
}

locals {
  focal_ami = data.amazon-ami.focal-ami.id
}


build {
  name    = "focal-ami"
  sources = ["source.amazon-ebs.focal-ami"]

  provisioner "ansible" {
    only          = ["amazon-ebs.focal-ami"]
    groups        = ["amis"]
    playbook_file = "playbook.yml"
    user          = "ubuntu"
    ansible_env_vars = [
      "ANSIBLE_ROLES_PATH=$PWD/../../",
      "ANSIBLE_STDOUT_CALLBACK=yaml",
      "ANSIBLE_REMOTE_USER=ubuntu"
    ]
  }
  # -{{ formatdate('DD-MMM-YYYY-hh:mm-ZZZ', timestamp()) }}

}
