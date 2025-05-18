import json


from config_dir.map_config import map_config_obj
from config_dir.config_obj import foodnet_config_obj, animals_config_obj 

from src.Map import Map
from src.Animal import Animal
from src.Simulation import Simulation

def main():

    map_ = Map(map_config_obj)
    
    species_all = {}
    list_of_animals_all = []
    for animal_config in animals_config_obj:
        number = animal_config['number']
        species = {animal_config['animal']['species']: animal_config['animal']}
        species_all.update(species)

        for i in range(number):
            list_of_animals_all.append(Animal(animal_config['animal']))

        
    simulation = Simulation(map_, foodnet_config_obj, 
                            species_all, list_of_animals_all)

main()
