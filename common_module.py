from abc import ABC, abstractmethod

class common_module(ABC):
    
    def __init__(self, module_name):
        self.module_name = module_name

    @abstractmethod
    def exec_task():
        pass
