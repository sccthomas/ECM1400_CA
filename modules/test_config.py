"""[A python module to test the config.py methods]
    """
from config import *


def test_config_opening():
    """[This is a function to test if the data in the config file is a dictionary]
    """
    assert isinstance(contents, dict)
