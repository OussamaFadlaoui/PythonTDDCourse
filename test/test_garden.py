
import unittest

from models.Garden import Garden


class TestGarden(unittest.TestCase):

  """
  Create a simple empty garden
  """
  def test_create_simple_garden(self) -> None:
    garden: Garden = Garden()
    self.assertIsInstance(garden, Garden)
