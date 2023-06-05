from abc import *

class Account(ABC):
    @abstractmethod
    def get_min_bal(self):
        pass
    