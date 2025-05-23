import numpy as np
import pandas as pd

import json

from config_dir.map_config import color_dictionary, map_config_obj
from config_dir.config_obj import foodnet_config_obj, animals_config_obj, simulation_config_obj 

from src.Map import Map
from src.Animal import Animal
from src.Simulation import Simulation

def setup_animal_kingdom(map_size, animals_config):
    species_all = {}
    list_of_animals_all = []
    for animal_config in animals_config_obj:
        
        number = animal_config['number']
        species = {animal_config['animal']['species']: animal_config['animal']}
        species_all.update(species)

        for i in range(number):
            list_of_animals_all.append(Animal(map_size, animal_config['animal']))

    return species_all, list_of_animals_all

def main():

    map_ = Map(color_dictionary, map_config_obj)
    map_size = [map_.size_x, map_.size_y]
    
    foodnet = foodnet_config_obj

    species_all, list_of_animals_all = setup_animal_kingdom(map_size, animals_config_obj)

    simulation_config = simulation_config_obj
        
    simulation = Simulation(map_, foodnet, species_all,
                            list_of_animals_all, simulation_config)

    animal_state_all, map_state_all = simulation.start()

    df_animal_state_all = pd.concat(animal_state_all, axis = 0)
    #df_map_state_all = pd.concat(map_state_all, axis = 0)
    
    df_animal_state_all.to_csv("D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/" + "animal_state_all.csv")
    #df_map_state_all.to_excel("D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/" + "map_state_all.xlsx")
    

main()
