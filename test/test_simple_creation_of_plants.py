import unittest


class TestSimpleCreationOfPlants(unittest.TestCase):
  
  def test_creating_african_sheepbush(self):
    newPlant = AfricanSheepBush()
    self.assertIsInstance(newPlant, AfricanSheepBush)
    self.assertTrue(newPlant.isAlive)

if __name__ == '__main__':
  unittest.main()
