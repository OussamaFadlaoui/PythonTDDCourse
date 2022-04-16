import unittest

from models.AfricanSheepBush import AfricanSheepBush
from models.Plant import Plant


class TestSimpleCreationOfPlants(unittest.TestCase):
  
  def test_creating_african_sheepbush(self) -> None:
    africanSheepBush: AfricanSheepBush = AfricanSheepBush()
    self.assertIsInstance(africanSheepBush, AfricanSheepBush)
    self.assertTrue(africanSheepBush.is_alive())

  def test_creating_plant(self) -> None:
    plant: Plant = Plant()
    self.assertIsInstance(plant, Plant)
    self.assertTrue(plant.is_alive())

if __name__ == '__main__':
  unittest.main()
