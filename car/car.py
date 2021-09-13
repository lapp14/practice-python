"""Car class"""

import uuid


class Car:
    """Represents a new car being made"""

    def __init__(self):
        """Creates a new car with unique id"""
        self.id = uuid.uuid4()
        self.colour = None
        self.top_speed = 200  # in km/h

    def paint(self, colour):
        """Paints car a specific colour"""
        if not isinstance(colour, str):
            raise Exception('Must supply string to Car.paint()')

        self.colour = colour.strip().lower()

        if self.colour == 'red':
            # red cars go 20% faster
            self.top_speed = self.top_speed * 1.2
