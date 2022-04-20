import numpy as np
import time
from tolmesurements import Instrument
from tolmesurements.src.instrument import InstrumentConfig

class Magnet(Instrument):
    def __init__(self, instrConfig):
        super().__init__(instrConfig)

    def reset(self):
        self.controller.write("A1D0")

    def getValue(self):
        pass

    def setValue(self, value):
        value = (value * 3200).round().astype(np.int16)
        self.controller.write(f'A1D{value}')
        time.sleep(1)