import numpy as np

import FoodNet
import Map
import Animal

import warnings
warnings.filterwarnings("ignore")

class Carnivore(Animal.Animal):

    def __init__(self, species_name: str, species_type: int,
                 initial_position: tuple, initial_energy: float, 
                 life_time: tuple, maturity: tuple, fertility: tuple, min_energy_to_bread: float,
                 mobility: tuple, unit_energy_consumption: float, 
                 fight_stats: tuple, fight_costs: tuple,
                 foodnet: FoodNet.FoodNet, map: Map.Map):
        
        Animal.Animal.__init__(self, species_name, species_type,
                               initial_position, initial_energy, 
                               life_time, maturity, fertility, min_energy_to_bread,
                               mobility, unit_energy_consumption, 
                               fight_stats, fight_costs, 
                               foodnet, map)