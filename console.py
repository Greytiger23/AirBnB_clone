#!/usr/bin/python3
import cmd
"""module that defines the class"""


class HBNBCommand(cmd.Cmd):
    """represents the class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def emptyline(self):
        """nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
