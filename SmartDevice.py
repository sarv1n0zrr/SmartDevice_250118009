from abc import ABC, abstractmethod

# Target
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        ...

    @abstractmethod
    def turn_off(self) -> None:
        ...

    @abstractmethod
    def is_on(self) -> bool:
        ...

    @abstractmethod
    def get_power_percent(self) -> int:
        """Standard range: 0 to 100"""
