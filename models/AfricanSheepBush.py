from models.Plant import Plant

class AfricanSheepBush(Plant):

  name = "African Sheep Bush"

  def __init__(self) -> None:
      super().__init__()
      self.initial_health = 80
