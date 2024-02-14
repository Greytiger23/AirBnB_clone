#!/usr/bin/python3
import cmd
"""module that defines the class"""


class HBNBCommand(cmd.Cmd):
    """represents the class"""
    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
