from abc import ABC, abstractmethod
import pyvisa

### Abstract Class for Instruments
class Instrument(ABC):
    def __init__(self, instrConfig):
        self.rm = instrConfig.rm
        self.controller = self.rm.open_resource(f'GPIB0::{instrConfig.gpio}::INSTR')
        self.reset()

    def list(self):
        print(self.rm.list_resources())

    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def setValue(self):
        raise NotImplementedError()
    
    @abstractmethod
    def getValue(self):
        raise NotImplementedError()

class InstrumentConfig:
    def __init__(self, rm, gpio):
        self.rm = rm
        self.gpio = gpio
    
