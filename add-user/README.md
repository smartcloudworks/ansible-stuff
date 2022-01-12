add-user

## What does this do? ##
This is a Linux cli, created in Python, that creates a user account across select Ansible nodes.

## What does this not do? ##
For now, this isn't intended to be a complete solution. Rather, it is simply a proof of concept, a learning experience for myself.

## Why? ##
In the case where you may be managing multiple Linux servers which require user accounts, this can ease the creation process for those that may not be Linux or Ansible savvy.

It aims to do several things:

1. Require the administrator to input nodes.
    1. One option is 'ansible-playbook add-user.yml --limit proxyservers'. The problem with this is that the playbook may imply 'all' by default. If the administrator forgets the --limit flag, the account is created across all nodes.
2. Provide a --help menu.

## Is this even practical? ##
Not really. You can do the same by requiring the administrator to specify hosts when executing the playbook via cli.
