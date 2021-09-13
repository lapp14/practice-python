"""Unit tests."""

import re
from car import car


def test_assertions():
    """First test just to make pytest run."""
    test_list = [1, 2, 3]
    assert len(test_list) == 3


def test_car_id():
    """Ensure car id is uuid v4, and set on initialization"""
    test_car = car.Car()
    uuid_regex = re.compile(
        '[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}')
    assert uuid_regex.match(str(test_car.id))


def test_paint_car():
    """Test car paint function"""
    test_car = car.Car()

    # A brand new car that has not been painted will not have a colour
    assert test_car.colour is None

    test_car.paint('black')
    assert test_car.colour == 'black'

    # test trim
    test_car.paint(' black  ')
    assert test_car.colour == 'black'

    # test to lower case
    test_car.paint('BlAcK')
    assert test_car.colour == 'black'


def test_car_speed():
    """Ensure that top speed is a positive integer"""
    test_car = car.Car()
    assert isinstance(test_car.top_speed, int) and test_car.top_speed > 0


def test_red_car_speed():
    """Red cars go 20% faster so check top speed after painting red"""
    test_white_car = car.Car()
    test_white_car.paint('white')

    test_red_car = car.Car()
    test_red_car.paint('red')

    assert test_red_car.top_speed == test_white_car.top_speed * 1.2
