
from models.AfricanSheepBush import AfricanSheepBush


if __name__ == '__main__':
  africanPlant: AfricanSheepBush = AfricanSheepBush()

  print(africanPlant.get_health())
  africanPlant.pass_days(days_to_pass=1)
  print(africanPlant.get_health())
