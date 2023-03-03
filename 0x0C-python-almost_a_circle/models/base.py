#!/usr/bin/python3
""" a module defining base class"""


import json


class Base:
    """Base class containing all common attributes"""
    _nb_objects = 0

    def __init__(self, id=None):
        """initializing method called when an instance is instantiated"""
        if not id:
            self.id = type(Base).__nb__objects + 1
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string that represents list_dictionaries"""
        if not list_dictionaries:
            return []
        else:
            return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string that represents of list_objs
           into a json file
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, 'w') as json_file:
            if not list_objs:
                json_file.write('[]')
            else:
                dict_list = [obj.to_dictionary() or obj in list_objs]
                json_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns SON string list that represents json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance witch all fields are set"""
        if dictionary:
            if cls.__name__ == 'Rectangle':
                temp = cls(2, 4)
            elif cls.__name__ == 'Square':
                temp = cls(2)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """ a method that returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r') as json_file:
                dicts = cls.from_json_string(json_file.read())
                return [cls.create(**dict) for dict in dict]

        except IOError:
            return []
