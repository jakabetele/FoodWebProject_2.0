import numpy as np

import random

import math

import Animal

import warnings
warnings.filterwarnings("ignore")

class Map(object):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        self.field = [[[] for y in self.size_y] for x in self.size_x]
    
    def add_animal(self, animal: Animal):
        x = animal.position[0]
        y = animal.position[1]
        
        self.field[x][y].append(animal)

    def get_animal_cel_pos(self, animal: Animal, x: int, y: int):
        for i, anim in enumerate(self.field[x][y]):
            if anim == animal:
                return i
        
        return False
        
    def delete_animal(self, animal: Animal):
        x = animal.position[0]
        y = animal.position[1]
        pos = self.get_animal_cel_pos(self, animal, x, y)

        if pos != False:            
            self.field[x][y] = self.field[x][y][:pos] + self.field[x][y][pos + 1:]
            return True
        
        return False
    
    def get_all_animals(self, x, y):
        return self.field[x][y]