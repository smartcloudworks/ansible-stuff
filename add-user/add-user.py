#!/usr/bin/python3

import argparse
import subprocess

def get_args():
  # first line provides info for the --help command.
  # prog - what name to display as the program name
  # description - self-explanatory
  # usage - displays command line format
  parser = argparse.ArgumentParser(prog='add-user', \
                                   description='Add User To Site', \
                                   usage='%(prog)s user=USER nodes=NODES [options]')

  # user and nodes are mandatory arguments that must be passed.
  parser.add_argument('user', help='Username')
  parser.add_argument('nodes', help='Ansible Group, Host or All. Comma-deliminate.')

  # the remaining are optional arguments
  parser.add_argument('-b', '--become', action='store_true', help='Run operation with become')
  parser.add_argument('-i', '--inventory', nargs='?', help='Inventory File')
  parser.add_argument('--comment', nargs='?', help='User Description')
  parser.add_argument('--shell', nargs='?', help='User Shell')

  # if there are no errors detected, the argument values are returned
  return parser.parse_args()

def verify_input(args):
  pass

# build_command_list()
# This function builds the command line arguments into a python list.
# This ensures that the command is compatible with the submodule
# library.
def build_command_list(args):
  # initialize list
  command_list = ['ansible-playbook', 'add-user.yml']

  # Adds inventory arguments if the inventory flag was entered.
  if args.inventory != None:
    command_list.append('-i')
    command_list.append(args.inventory)

  # Adds become argument
  if args.become:
    command_list.append('-b')

  # Adds user argument
  command_list.append('-e')
  command_list.append(args.user)

  # Adds nodes argument
  command_list.append('-e')
  command_list.append(args.nodes)

  # Adds comment argument if the comment flag was entered.
  if args.comment != None:
    command_list.append('-e')
    command_list.append(f"comment='{args.comment}'")

  # Adds shell argument if the shell flag was entered.
  if args.shell != None:
    command_list.append('-e')
    command_list.append(f"shell={args.shell}")

  return command_list

# main function, this is where the magic starts
if __name__ == '__main__':
  # retrieve arguments from command line.
  # if argument format is invalid, the function
  # should error out and exit.
  args = get_args()

  # verifies input (TODO)
  verify_input(args)

  # builds list of commands to be passed to subprocess.run
  command_list = build_command_list(args)

  subprocess.run(command_list)
