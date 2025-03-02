import numpy as np

import random

import math

import FoodNet
import Map

import warnings
warnings.filterwarnings("ignore")

class Animal(object):

    def __init__(self, species_name: str, species_type: int,
                 initial_position: tuple, initial_energy: float, 
                 life_time: tuple, maturity: tuple, fertility: tuple, min_energy_to_bread: int,
                 mobility: tuple, unit_energy_consumption: float, 
                 fight_stats: tuple, fight_costs: tuple,
                 foodnet: FoodNet.FoodNet, map: Map.Map):
        
        self.species_name = species_name
        self.species_type = species_type

        self.position = initial_position
        self.energy = initial_energy

        self.life_time = life_time
        self.maturity = maturity
        self.fertility = fertility
        self.min_energy_to_bread = min_energy_to_bread

        self.mobility = mobility
        self.unit_energy_consumption = unit_energy_consumption
        
        self.fight_stats = fight_stats
        self.fight_costs = fight_costs
        
        self.foodnet = foodnet
        self.map = map

        self.alive = True

    def genarate_random_distance(self) -> float:
        return random.gauss(self.mobility[0], self.mobility[1]**2)

    def generate_random_direction(self, quarter_allowed = [0, 1, 2, 3]) -> float:
        q_pi = math.pi/2 
        quarter = random.choice(quarter_allowed)
        direction_res = q_pi*quarter + random.random() * q_pi
           
        return direction_res
        
    def move(self):
        distance = self.genarate_random_distance()
        distance = min(distance, self.energy * self.unit_energy_consumption)
        distance_to_do = distance

        direction = self.generate_random_direction([0, 1, 2, 3])

        while distance_to_do != 0:
            new_x = int(self.position[0] + distance_to_do * math.cos(direction))
            new_y = int(self.position[1] + distance_to_do * math.sin(direction))

            new_x = max(0, min(self.map.size_x, new_x))
            new_y = max(0, min(self.map.size_y, new_y))

            distance_to_do = distance_to_do - (np.linalg.norm((self.x, self.y) - (new_x, new_y)))
            
            quarter_allowed = []
            if new_x != self.map.size_x and new_y != self.map.size_y:
                quarter_allowed.append(0)
            if new_x != 0 and new_y != self.map.size_y:
                quarter_allowed.append(1)
            if new_x != 0 and new_y != 0:
                quarter_allowed.append(2)
            if new_x != self.map.size_x and new_y != 0:
                quarter_allowed.append(3)

            direction = self.generate_random_direction()
        
        self.position[0] = new_x
        self.position[1] = new_y

        self.energy -= distance * self.unit_energy_consumption

    def fight(self, other):
        if self.foodnet[self.species_type][other.species_type] == True and other.alive:

            this_attack = self.fight_stats[0] * random.random()
            other_defence =  other.fight_stats[1] * random.random()

            if this_attack > other_defence:
                self.energy += other.energy * other.nutrition_ratio
                other.alive = False
            else:
                other.energy -= other.fight_costs[1]
            
            self.energy -= self.fight_costs[0]
 
    def interact(self):
        pass

    def die(self):
        if self.energy == 0:
            self.alive = False

    def bread(self):
        pass
    
    def simulate_epoch(self):
        if not self.alive:
            return False, self.position
        
        self.move()
        self.interact()
        self.bread()
        self.die()
