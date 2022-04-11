import imp
from tolmesurements import Instrument

class Magnet(Instrument):
    def __init__(self, instrConfig):
        super().__init__(instrConfig)

    def reset(self):
        pass

    def getValue(self):
        return float(self.controller.query('KRDG? A'))