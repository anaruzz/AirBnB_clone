#!/usr/bin/python3

"""
Module that creates a line oriented command interpreter
"""
from cmd import Cmd


class HBNBCommand(Cmd):
    """
    entry point hbnb class
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quits the console."""
        return True

    def do_EOF(self, line):
        """
        end of file Ctrl+d
        """
        return True

    def emptyline(self):
        """
        empty line
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
