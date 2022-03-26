#!/bin/bash

# Install & run Ansible playbook
echo -e "Installing latest Ansible \n"
sudo apt update
sudo apt install -y -q ansible
echo -e "Ansible is installed \n"
echo -e "Running Ansible Playbook \n"
ansible-playbook playbook.yaml
echo -e "Ansible playbook complete \n"