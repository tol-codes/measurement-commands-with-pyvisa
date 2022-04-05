from abc import ABC, abstractmethod
import pyvisa

class Measurement(ABC):
    def __init__(self, rm, gpio):
        self.controller = rm.open_resource(f'GPIB0::{gpio}::INSTR')
        self.rm = rm
        self.reset()

    def list(self):
        print(self.rm.list_resources())

    @abstractmethod
    def reset(self):
        pass
