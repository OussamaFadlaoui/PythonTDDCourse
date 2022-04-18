
import unittest

from models.Garden import Garden
from models.AfricanSheepBush import AfricanSheepBush


class TestGarden(unittest.TestCase):

  """
  Create a simple empty garden
  """
  def test_create_simple_garden(self) -> None:
    garden: Garden = Garden()
    self.assertIsInstance(garden, Garden)

  """
  Add a plant to a garden
  """
  def test_adding_plant_to_garden(self) -> None:
    garden: Garden = Garden()
    africanSheepBush: AfricanSheepBush = AfricanSheepBush()

    plantAdded: bool = garden.add_plant(africanSheepBush)

    self.assertIn(africanSheepBush, garden.plants)
    self.assertTrue(plantAdded)
