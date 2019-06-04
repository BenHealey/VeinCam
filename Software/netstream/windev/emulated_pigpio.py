# VEINCAM pigpio emulation script
from flask import Flask

app = Flask(__name__)

class pi():
    """An emulated pigpio implementation does nothing."""

    @staticmethod
    def write(pin, state):
        pass

    @staticmethod
    def read(pin):
        pass

    @staticmethod
    def hardware_PWM(pin, hz, duty):
        pass
        