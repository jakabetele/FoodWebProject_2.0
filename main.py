import json

from config_obj import animals_config_obj
from src.animal.Animal import Animal

#from src.Simulation import Simulation

def main():
    
    animals_obj_all = []
    for animal in animals_config_obj:
        animal_new = Animal(animal)
        animals_obj_all.append(animal_new)
        

    print(len(animals_obj_all))
    return True

def gen_map():
    ma = [] 
    for i in range(500):
        row = []
        for j in range(500):
            row.append({"height": 10, "type": "grass", "nutrition": 0.05, "regeneration": 0.01})
        ma.append(row)

    with open("map.txt", "a") as f:
      f.write(str(ma))
      
gen_map()
