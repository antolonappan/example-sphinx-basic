"""
models 

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    from pkg_name import Fake

"""

class Fake:
    """
    A class representing a fake entity for testing purposes.

    Attributes:
        name (str): The name of the fake entity.
    """

    def __init__(self, name):
        """
        Initializes the Fake class with a name.

        Args:
            name (str): The name of the fake entity.
        """
        self.name = name

    def say_hello(self):
        """
        Returns a greeting message that includes the entity's name.

        Returns:
            str: A greeting message with the name of the fake entity.
        """
        return f"Hello, {self.name}!"

    