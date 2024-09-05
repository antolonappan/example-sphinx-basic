"""
This is a module that contains a function that returns the name and age of a person.
"""

def experiment(name, age):
    """
    Return the name and age of the person.

    :param name: The name of the person.
    :type name: str
    :param age: The age of the person.
    :type age: int
    :return: The name and age of the person.
    :rtype: str
    """
    return f"{name} is {age} years old."


class Person:
    """
    A class that represents a person.
    """

    def __init__(self, name, age):
        """
        Initialize the person with a name and age.

        :param name: The name of the person.
        :type name: str
        :param age: The age of the person.
        :type age: int
        """
        self.name = name
        self.age = age
    
    def get_name(self):
        """
        Return the name of the person.

        :return: The name of the person.
        :rtype: str
        """
        return self.name

    def __str__(self):
        """
        Return a string representation of the person.

        :return: The name and age of the person.
        :rtype: str
        """
        return f"{self.name} is {self.age} years old."