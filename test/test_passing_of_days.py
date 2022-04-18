
import unittest
from models.Plant import Plant


class TestPassingOfDays(unittest.TestCase):

  """
  Days passing should mean that a plant's health deteriorates
  """
  def test_passing_of_a_day_deteroriates_plant_health(self) -> None:
    some_plant: Plant = Plant()
    initial_health: int = some_plant.get_health()

    some_plant.pass_day()

    health_after_days: int = some_plant.get_health()

    self.assertNotEqual(initial_health, health_after_days)
