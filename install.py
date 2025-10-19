#!/usr/bin/python3

import os

def main():
  bashrc_path = os.path.expanduser('~/.bashrc')
  with open(bashrc_path, 'a+') as bashrc:
    bashrc.seek(0)
    add_exec = f"export PATH=\"{os.path.dirname(os.path.abspath(__file__))}:$PATH\""
    if add_exec not in bashrc.read():
      bashrc.write('\n' + add_exec + '\n')
      print('.bashrc has been updated.')
  print('O\'key')


if __name__ == '__main__':
  main()