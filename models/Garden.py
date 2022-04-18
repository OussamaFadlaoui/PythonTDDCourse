
from typing import List
from models.Plant import Plant


class Garden:

  def __init__(self, capacity: int = 10) -> None:
    self.plants: List[Plant] = list()
    self.capacity: int = capacity

  def add_plant(self, plant_to_add: Plant) -> bool:
    if len(self.plants) >= self.capacity:
      return False

    self.plants.append(plant_to_add)
    
    return True
