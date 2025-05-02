import json

from config_obj import animals_config_obj
from src.animal.Animal import Animal

def main():
    
    animals_obj_all = []
    for animal in animals_config_obj:
        animal_new = Animal(animal)
        animals_obj_all.append(animal_new)
        

    print(len(animals_obj_all))
    return True


main()
