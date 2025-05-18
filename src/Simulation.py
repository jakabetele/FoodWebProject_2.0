import numpy as np
import pandas as pd

import random

import matplotlib.pyplot as plt

import imageio.v2 as imageio
import os


from FoodNet import FoodNet
from Map import Map
from Animal import Animal

class Simulation():

    def __init__(self,
                 map: Map,
                 foodnet: dict,
                 species_all: dict,
                 list_of_animals_all : list[Animal],
                 simulation_config_obj: dict):

        
        self.map = map
        self.foodnet = foodnet
        self.species_all = species_all
        self.list_of_animals_all = list_of_animals_all

        self.simulation_steps = simulation_config_obj['simulation_steps']
        self.generate_simulation_gif = simulation_config_obj['generate_simulation_gif']
        if self.generate_simulation_gif:
            self.frame_duration = simulation_config_obj['frame_duration']
            self.save_path = simulation_config_obj['save_path']
            self.plot_config_obj = simulation_config_obj['plot_config_obj']

        self.state_all = []
        self.interaction_map = [[[] for j in range(self.map.size_y)] for i in range(self.map.size_x)]
    
    def animal_interaction(self, animal_a: Animal, animal_b: Animal):
        if animal_b.species in self.foodnet[animal_a.species]: # animal_b is a pray animal of animal_a
                animal_a.hunt(animal_b)
        elif animal_a.species in self.foodnet[animal_b.species]: # animal_a is a pray animal of animal_b
                animal_b.hunt(animal_a)
        else:
            pass

        return True

    def simulate_interaction_pos(self, animals_interact_all: list[Animal]):
        nr_animals = len(animals_interact_all)
        random.shuffle(animals_interact_all)

        for i in range(0, nr_animals-1):
            animal_a = animals_interact_all[i]
            
            if animal_a.alive:
                for j in range(i+1, nr_animals):
                    animal_b = animals_interact_all[j]
                    
                    if animal_b.alive:
                        self.animal_interaction(animal_a, animal_b)
                    else:
                        pass
            else:
                pass
        
        for i in range(0, nr_animals):
            animal = animals_interact_all[i]
            x_pos, y_pos = animal.position


            if map.field[x_pos][y_pos][1] in self.foodnet[animal.species_name]:
                consumed = animal.eat_field(map.field[x_pos][y_pos][2])
                map.field[x_pos][y_pos][2] -= consumed
        
        return True

    def calculate_state(self):
        state = []
        nr_animal = len(self.list_of_animals_all)
        for i in range(nr_animal):
            animal = self.list_of_animals_all[i]
            
            if animal.alive:
                pos = animal.get_pos()
                species  = animal.get_species()
                color = animal.get_color()
                state.append([species, color, pos[0], pos[1]])
            else:
                self.list_of_animals_all.pop(i)
                i -= 1
        
        df_state = pd.DataFrame(state, columns = ['species', 'color', 'x', 'y'])
        self.state_all.append(df_state)

    def end_of_step(self):
        new_born_all = []
        nr_animal = len(self.list_of_animals_all)
        
        for i in range(nr_animal):
            animal = self.list_of_animals_all[i]
            
            if animal.alive:
                nr_offsprings = animal.bread()
                pos = animal.get_pos()
                for j in range(nr_offsprings):
                    offspring = Animal(self.species_all[animal.species])
                    offspring.position = pos
                    new_born_all.append(offspring)
            else:
                self.list_of_animals_all.pop(i)
                i -= 1
        
        self.list_of_animals_all += new_born_all

    def start_simualtion(self):
        
        for i in range(self.simulation_steps):
            self.calculate_state()

            interaction_pos_all = []
            for animal in self.list_of_animals_all:
                animal.move()
                pos = animal.get_pos()

                if len(self.interaction_map[pos[0]][pos[1]]) == 0:
                    interaction_pos_all.append(pos)

                self.interaction_map[pos[0]][pos[1]].append(animal)
            
            for pos in interaction_pos_all:
                animals_interact_all = self.interaction_map[pos[0]][pos[1]]
                self.simulate_interaction_pos(animals_interact_all)
                
                self.interaction_map[pos[0]][pos[1]] = []
            
        
            self.end_of_step()

            self.map.regenare_grass()
        
        if self.generate_simulation_gif:
            self.generate_gif()
    
    def generate_gif(self):
                  
        with imageio.get_writer(self.save_path, mode='I', duration = self.frame_duration) as writer:
            history_all = []

            for i, df_state in enumerate(self.state_all):
                species_all = df_state['species'].unique()
            
                for species in species_all:
                    nr_animal = df_state[df_state['species'] == species].shape[0]
                    species_color = df_state['color'][df_state['species'] == species].iloc[0]
                    history_all.append([species, i, nr_animal, species_color])
                    
                df_history = pd.DataFrame(history_all, columns = ['species', 'step', 'nr_animal', 'color'])

                fig, ax = plt.subplots(2, 1, figsize = (10, 6), gridspec_kw = {'height_ratios': [3, 1]})
                fig.tight_layout()
                ax[0].grid(True)
                ax[1].grid(True)

                ax[0].scatter(x = df_state['x'], y = df_state['y'], color = df_state['color'])

                for species in df_history['species'].unique():
                    df_species = df_history[df_history['species'] == species]
                    color_species = df_species['color'][df_species['species'] == species].iloc[0]
                    
                    ax[1].plot(df_species['step'], df_species['nr_animal'], color = color_species, label = species)

                ax[1].legend()

                frame_name = f"{str(i)}.png"
                plt.savefig(frame_name)

                image = imageio.imread(frame_name)
                writer.append_data(image)
                os.remove(os.path.join(self.save_path, frame_name))
        
Simulation()
