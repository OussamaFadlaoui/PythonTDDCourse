import unittest

from models.AfricanSheepBush import AfricanSheepBush


class TestSimpleCreationOfPlants(unittest.TestCase):
  
  def test_creating_african_sheepbush(self):
    newPlant: AfricanSheepBush = AfricanSheepBush()
    self.assertIsInstance(newPlant, AfricanSheepBush)
    self.assertTrue(newPlant.isAlive)

if __name__ == '__main__':
  unittest.main()
