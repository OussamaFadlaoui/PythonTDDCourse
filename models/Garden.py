
from typing import List
from models.Plant import Plant


class Garden:

  def __init__(self, capacity: int = 10) -> None:
    self.plants: List[Plant] = list()
    self.capacity: int = capacity
