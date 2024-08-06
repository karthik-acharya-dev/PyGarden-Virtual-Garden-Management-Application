class Plant:
  def __init__(self,name,water_need):
    self.name=name
    self.water_need=water_need
    self.water_level=0

  def water(self,amount):
    self.water_level+=amount

  def display(self):
    print(f"{self.name}-Water Level:{self.water_level}/{self.water_need}")

  
class Garden:
  def __init__(self):
    self.plants=[]


  def add_plant(self,plant):
    self.plants.append(plant)

  def water_plants(self,plant_name,amount):
    for plant in self.plants:
      if plant.name==plant_name:
        plant.water(amount)

  def display_plants(self):
    for plant in self.plants:
      plant.display()



#pygarden instance
pygarden=Garden()


plant1=Plant("Rose",10)
plant2=Plant("Tomato",15)

pygarden.add_plant(plant1)
pygarden.add_plant(plant2)

#water plants in pygarden
pygarden.water_plants("Rose",5)
pygarden.water_plants("Tomato",10)

#display
pygarden.display_plants()