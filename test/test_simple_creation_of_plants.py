import unittest

from models.AfricanSheepBush import AfricanSheepBush


class TestSimpleCreationOfPlants(unittest.TestCase):
  
  def test_creating_african_sheepbush(self) -> None:
    africanSheepBush: AfricanSheepBush = AfricanSheepBush()
    self.assertIsInstance(africanSheepBush, AfricanSheepBush)
    self.assertTrue(africanSheepBush.is_alive())

if __name__ == '__main__':
  unittest.main()
