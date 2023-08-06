import random

from robot.api import Error

class ViaNumber():
    def choose_number(stopNumber):
        try:
            return random.randrange(1, stopNumber)
        except Exception as e:
            raise Error(e)
