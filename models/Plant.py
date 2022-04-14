
class Plant():
   
  name = "A plant"

  def __init__(self) -> None:
      self.initial_health = 100
      self.watering_level = 100
      self.sunlight_level = 100

  """
  Simply check if the health is greater than 0
  """
  def is_alive(self):
    return self.get_health() > 0

  """
  The health of a plant is based on the wateringLevel
  and the sunlightLevel.
  """
  def get_health(self):
    return (self.watering_level + self.sunlight_level) / 2
