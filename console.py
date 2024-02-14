#!/usr/bin/python3
"""module that defines the class"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """represents the class"""
    prompt = "(hbnb) "
    _classes = {
            "BaseModel",
            "City",
            "User",
            "Place",
            "Amenity",
            "Review",
            "State"
            }

    def do_quit(self, arg):
        """exit program"""
        return True

    def do_EOF(self, arg):
        """exit program"""
        print("")
        return True

    def emptyline(self):
        """do nonthing"""
        pass

    def create(self, arg):
        """creates new module"""
        if not arg:
            print("** class name missing **")
            return
        a = arg.split()
        c = a[0]
        if c not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return
        n = HBNBCommand._classes[c]()
        n.save()
        print(n.id)

    def do_show(self, arg):
        """prints string"""
        if not arg:
            print("** class name missing **")
            return
        a = arg.split()
        c = a[0]
        if c not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return
        if len(a) < 2:
            print("** instance id missing **")
            return
        obj_id = a[1]
        key = "{}.{}".format(c, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """destroys instance"""
        if not arg:
            print("** class name missing **")
            return
        a = arg.split()
        c = a[0]
        if c not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return
        if len(a) < 2:
            print("** instance id missing **")
            return
        obj_id = a[1]
        key = "{}.{}".format(c, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """prints all string"""
        if arg:
            if arg not in HBNBCommand._classes:
                print("** class doesn't exist **")
                return
            o = [str(obj) for key, obj in models.storage.all() if key.split(
                '.')[0] == arg]
        else:
            o = [str(obj) for obj in models.storage.all().values()]
        print(o)

    def do_update(self, arg):
        """updates"""
        if not arg:
            print("** class name missing **")
            return
        a = shlex.split(arg)
        c = a[0]
        if c not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return
        if len(a) < 2:
            print("** instance id missing **")
            return
        obj_id = a[1]
        key = "{}.{}".format(c, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(a) < 3:
            print("** attribute name missing **")
            return
        if len(a) < 4:
            print("** value missing **")
            return
        b = a[2]
        d = a[3]
        obj = models.storage.all()[key]
        setattr(obj, b, d)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
