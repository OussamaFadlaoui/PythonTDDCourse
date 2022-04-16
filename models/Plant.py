
from models.value.PlantHealthValue import PlantHealthValue


class Plant():
   
  name = 'A plant'

  def __init__(self) -> None:
    self.watering = PlantHealthValue(deterioration_rate=.1, level=100)
    self.sunlight = PlantHealthValue(deterioration_rate=.5, level=100)

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
    return (self.watering.level + self.sunlight.level) / 2

  """
  Advance a day in the life of a plant
  """
  def pass_day(self):
    self.watering.level -= self.watering.level * self.watering.deterioration_rate
    self.sunlight.level -= self.sunlight.level * self.sunlight.deterioration_rate

  def pass_days(self, days_to_pass: int = 1):
    for _ in range(days_to_pass):
      self.pass_day()
