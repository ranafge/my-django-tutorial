import random
def PercentConvertion(Percent):
  IntPercent = int(Percent / 10)
  Chance = random.randint(1, IntPercent)
  purpose = int(IntPercent / 2)
  hit = None
  if Chance == purpose:
    hit = True
  else:
    hit = False
  return hit

PercentConvertion(20)