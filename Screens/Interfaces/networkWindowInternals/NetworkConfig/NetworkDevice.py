# This Python file uses the following encoding: utf-8
import enum

class NetworkDevice:
    def __init__(self):
        self.deviceType = self.Types.GENERIC
        self.name = ""

    class Types(enum.Enum):
        GENERIC = 0
        ROUTER = 1
        SWITCH = 2
        COMPUTER = 3
