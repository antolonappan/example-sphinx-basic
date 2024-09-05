"""
models 

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    from pkg_name import Fake

"""

class Fake:
    """
    A fake class for testing
    """
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """
        Say hello to the fake class
        """
        return f"Hello, {self.name}!"
    