"""[A python module to test the covid_data_interface.py module and its methods]
    """
from covid_data_interface import MyServer, logger_interface
import datetime


def test_flask_class():
    """[A function to test that an instance of the flask website occurs]
    """
    server = MyServer()
    init = [method for method in dir(
        server) if method.startswith('__') is False]
    assert isinstance(server, object)


def test_time_handler():
    """[A function to test the calculation of difference between two times]
    """
    self = []

    time_set = '00:00'
    current_time = (datetime.datetime.now()).strftime("%H:%M")
    # calculate the time delay between the two times provided
    time_seconds = 86400-((datetime.datetime.strptime(time_set, '%H:%M') -
                           datetime.datetime.strptime(current_time, '%H:%M')).seconds)

    time = 86400 - int(MyServer.time_handler(self, '00:00'))
    assert time == time_seconds
