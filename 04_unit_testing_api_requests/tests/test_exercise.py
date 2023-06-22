from lib.exercise import *
from unittest.mock import *

def test_time_error():
    """request = TimeError()

    server_time = requests.get("https://worldtimeapi.org/api/ip").json()["unixtime"]
    assert int(request.error()) + int(time.time()) == int(server_time)"""
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1668262850}
    
    timer_mock = Mock()
    timer_mock.time.return_value = 1668262850.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5