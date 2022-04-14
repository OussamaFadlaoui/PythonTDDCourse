
class Plant():
   
  name = "A plant"

  def __init__(self) -> None:
      self.initalHealth = 100
      self.health = self.initalHealth

  def isAlive(self):
    return self.health > 0
