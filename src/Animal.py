import numpy as np

import random

import math

import warnings
warnings.filterwarnings("ignore")

class Animal(object):

    def __init__(self, map_size: [int], config_obj : dict):
        
        self.map_size = map_size
        
        self.species = config_obj["species"]
        self.color = config_obj["color"]

        self.energy = config_obj["initial_energy"]
        self.nutrition_value = config_obj["nutrition_value"]

        self.life_expectancy = config_obj["life_expectancy"]
        self.maturity = config_obj["maturity"]
        self.fertility = config_obj["fertility"]
        self.min_energy_to_bread = config_obj["min_energy_to_bread"]
        self.breading_cost_per_offspring = config_obj["breading_cost_per_offspring"]

        self.mobility = config_obj["mobility"]
        self.unit_energy_consumption = config_obj["unit_energy_consumption"]
        
        self.fight_stat = config_obj["fight_stat"]
        self.fight_costs = config_obj["fight_costs"]
        
        self.alive = True
        self.position = [int(random.random() * map_size_x), 
                         int(random.random() * map_size_y)]

    def genarate_distance(self) -> float:
        return int(round(random.gauss(self.mobility[0], self.mobility[1]**2), 0))
    
    def get_dist(self, pos_a, pos_b):
        return int(round(((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)**(1/2), 0))
        
    def move(self):
        angle_step = math.radians(5)
        
        x, y = self.position
        x_max, y_max = self.map_size

        distance = self.genarate_distance()
        distance = min(distance, self.energy / self.unit_energy_consumption)
        self.energy -= distance * self.unit_energy_consumption
        
        angle = random.uniform(0, 2 * math.pi)

        rotation_direction = random.choice([1, -1])
        
        while True:
            x_new = x + distance * math.cos(angle)
            y_new = y + distance * math.sin(angle)
            
            if 0 <= x_new <= x_max and 0 <= y_new <= y_max:
                new_pos = [int(x_new), int(y_new)]
                break
    
            angle += rotation_direction * angle_step
        
        self.position = new_pos

    def hunt(self, prey: Animal):

        predator_power = int(round(random.gauss(self.fight_stat[0], self.fight_stat[1]**2), 0))
        prey_power =  int(round(random.gauss(prey.fight_stat[0], prey.fight_stat[1]**2), 0))

        if predator_power > prey_power:
            self.energy += prey.nutrition_value - self.fight_costs
            prey.die()
        
        self.energy -= self.fight_costs
        prey.energy -= prey.fight_costs
    
    def eat_field(self, field_nutrition_value: float):
        if self.energy + field_nutrition_value > 1:
            consumed = 1 - self.energy
            self.energy = 1
        else:
            consumed = field_nutrition_value
            self.energy += field_nutrition_value
        
        return consumed

    def get_species(self):
        return self.species_name
    
    def get_color(self):
        return self.color

    def get_pos(self):
        return self.position

    def bread(self):
        if self.energy >= self.min_energy_to_bread:
            num = random.random()
            
            if num <= self.fertility[0]:
                nr_offsprings = int(round(random.gauss(self.fertility[1], self.fertility[2]**2), 0))
                
                while nr_offsprings * self.breading_cost_per_offspring > self.energy:
                    nr_offsprings -= 1

                self.energy -= nr_offsprings * self.breading_cost_per_offspring

                return nr_offsprings
            else:
                return 0
        else:
            return 0

    def die(self):
        self.alive = False

map_size_x = 1000
map_size_y = 1000

config_obj = {"species_name" : "rabbit",           #
              "species_type" : "herbivore",        #
              "initial_energy" : 0.4,              #The energy whith which the animal is born
              "life_expectancy" : (15, 3),         #The expected life length and the std coefficient
              "maturity" : (5, 0.3, 3),            #The time from which it can reproduce and its std coefficients (pre maturity and post maturity)
              "fertility" : (0.5, 4, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
              "min_energy_to_bread" : 0.5,         #The minimum energy level for getting pregnant
              "breading_cost_per_offspring" : 0.1, #The cost of energy for every living offspring righ after pregnancy
              "mobility" : (10, 1),                #The expected distance to moove in a turn and the std coefficient
              "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
              "fight_stat" : (10.0, 2),            #The expected fight power in a fight and std coefficient
              "fight_costs" : 0.1                  #The cost of a fight
}

animal = Animal((map_size_x, map_size_y), config_obj)