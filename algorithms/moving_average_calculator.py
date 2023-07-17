from abc import ABC, abstractmethod
from typing import List, Dict

class MovingAverageCalculator(ABC):
    @abstractmethod
    def calculate_average(self, events: List[Dict[str, str]], window_size: int) -> List[Dict[str, float]]:
        pass