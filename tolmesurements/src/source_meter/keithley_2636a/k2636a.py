from tolmesurements import Instrument
from tolmesurements.src.instrument import InstrumentConfig
import numpy as np

class K2636A(Instrument):
    def __init__(self, instrConfig):
        super().__init__(instrConfig)

    def reset(self):
        self.controller.write("smua.reset()")
        self.controller.write("smub.reset()")

    def getValue(self):
        pass

    def setValue(self, value):
        value = (value * 3200).round().astype(np.int16)
        self.controller.write(f'A1D{value}')
    
    def setRange(self, value):
        ch = value["ch"]
        rangev = value["v"]
        rangei = value["i"]

        self.controller.write(f'smu{ch}.measure.rangev = {rangev}')
        self.controller.write(f'smu{ch}.measure.rangev = {rangei}')