#!/usr/bin/python3

"""
Module that creates a line oriented command interpreter
"""
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import json


class HBNBCommand(Cmd):
    """
    entry point hbnb class
    """
    prompt = "(hbnb) "
    all_classes = ["BaseModel", "User"]

    def do_quit(self, arg):
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

    def do_create(self, arg):
        """ create """
        if not arg:
            print("** class name missing **")
            return
        else:
            if arg in self.all_classes:
                command = arg.split(' ')[0]
                obj = eval("{}()".format(command))
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
                return

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        my_list = arg.split(' ')
        class_name = my_list[0]
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return
        if len(my_list) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = my_list[0] + '.' + my_list[1]
        if key not in objects:
            print("** no instance found **")
            return
        else:
            print(objects[key])

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return
        my_list = arg.split(' ')
        class_name = my_list[0]
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return
        if len(my_list) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = my_list[0] + '.' + my_list[1]
        if key not in objects:
            print("** no instance found **")
            return
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        objects = storage.all()
        new_list = []
        if not arg:
            for key in objects.keys():
                new_list.append(key)
            print(new_list)
            return
        class_name = arg.split(' ')[0]
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return
        else:
            new_list=[]
            class_name = str(objects).split('.')[0]
            class_name = class_name.split('\'')[1]
            instance_id = str(objects).split('.')[1]
            instance_id = instance_id.split('\'')[0]
            beg = "[" + class_name + "] (" + instance_id + ")"
            print(class_name)
            print(instance_id)
            print()
            for obj in objects.items():
                if obj[0].split('.')[0] == class_name:
                    new_list.append(beg)
                    new_list.append(obj[1].to_dict())
            print(new_list)
            return

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        my_list = arg.split(' ')
        class_name = my_list[0]
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return
        if len(my_list) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = my_list[0] + '.' + my_list[1]
        if key not in objects:
            print("** no instance found **")
            return
        if len(my_list) < 3:
            print("** attribute name missing **")
            return
        if len(my_list) < 4:
            print("** value missing **")
            return
        val = objects[key]
        try:
            val.__dict__[my_list[2]] = eval(my_list[3])
        except Exception:
            val.__dict__[my_list[2]] = my_list[3]
        val.save()






if __name__ == '__main__':
    HBNBCommand().cmdloop()
