class vehicle:
  
  def __init__(self,engine):
    print("we are in vehicle")
    self.engine = engine

class car(vehicle):

  def __init__(self, engine, max_speed):
    super().__init__(engine)
    print("we are in car")
    self.max_speed = max_speed

class electric_car(car):

  def __init__(self, engine, max_speed, km_range):
    super().__init__(engine, max_speed)
    print("we are in electric_car")
    self.km_range = km_range

ev = electric_car("1500cc",250,800)
