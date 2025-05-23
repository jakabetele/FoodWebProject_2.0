import numpy as np
import pandas as pd
import math
import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

import imageio
from io import BytesIO

import os

#from src.FoodNet import FoodNet
from src.Map import Map
from src.Animal import Animal

class Simulation():

    def __init__(self,
                 map_: Map,
                 foodnet: dict,
                 species_all: dict,
                 list_of_animals_all : list[Animal],
                 simulation_config_obj: dict):

        
        self.map_ = map_
        self.map_size = [self.map_.size_x, self.map_.size_y]

        self.foodnet = foodnet

        self.species_all = species_all

        self.list_of_animals_all = list_of_animals_all

        self.simulation_steps = simulation_config_obj['simulation_steps']
        self.generate_simulation_gif = simulation_config_obj['generate_simulation_gif']
        if self.generate_simulation_gif:
            self.frame_duration = simulation_config_obj['frame_duration']
            self.save_path = simulation_config_obj['save_path']
            self.plot_config_obj = simulation_config_obj['plot_config_obj']

        self.map_state_all = []
        self.animal_state_all = []
        self.interaction_map = [[[] for j in range(self.map_.size_y)] for i in range(self.map_.size_x)]

    def draw_colored_cells(self, ax, df_map_state, cell_size=1.0):
        patches_list = []
        facecolors = []
        alphas = []

        for _, row in df_map_state.iterrows():
            rect = patches.Rectangle(
                (row['x'], row['y']),  # bottom-left corner
                width=cell_size,
                height=cell_size
            )
            patches_list.append(rect)
            facecolors.append(row['color'])
            alphas.append(row['alpha'])

        collection = PatchCollection(patches_list, facecolor=facecolors, alpha=None)
        collection.set_alpha(None)  # defer to individual alphas
        collection.set_array(np.array(alphas))  # apply per-patch alpha via array

        ax.add_collection(collection)

    def generate_gif(self):
        x_size = self.map_.size_x
        x_tolr = int(x_size * 0.01)
        y_size = self.map_.size_y
        y_tolr = int(y_size * 0.01)

        sim_len = len(self.animal_state_all)
        sim_len_tol = int(sim_len * 0.01)

        max_animal = max([df_animal_state['species'].value_counts()[0] for df_animal_state in self.animal_state_all if df_animal_state.shape[0] != 0])
        max_animal_tol = int(max_animal * 0.01)

        history_all = []

        with imageio.get_writer(self.save_path + "simulation.gif", mode='I', duration=self.frame_duration) as writer:

            for i, (df_animal_state, df_map_state) in enumerate(zip(self.animal_state_all, self.map_state_all)):
                species_all = df_animal_state['species'].unique()

                for species in species_all:
                    nr_animal = df_animal_state[df_animal_state['species'] == species].shape[0]
                    species_color = df_animal_state['color'][df_animal_state['species'] == species].iloc[0]
                    history_all.append([species, i, nr_animal, species_color])

                df_history = pd.DataFrame(history_all, columns=['species', 'step', 'nr_animal', 'color'])

                fig, ax = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [3, 1]})
                fig.tight_layout()

                # Top plot
                ax[0].grid(True)
                #self.draw_colored_cells(ax[0], df_map_state, 1.0)
                #ax[0].set_facecolor("green")

                ax[0].set_xlim(left=0 - x_tolr, right=x_size + x_tolr)
                ax[0].set_ylim(bottom=0 - y_tolr, top=y_size + y_tolr)
                ax[0].scatter(x=df_animal_state['x'], y=df_animal_state['y'], color=df_animal_state['color'])

                # Bottom plot
                ax[1].grid(True)
                ax[1].set_xlim(left=0 - sim_len_tol, right=sim_len + sim_len_tol)
                ax[1].set_ylim(bottom=0, top=max_animal + max_animal_tol)

                for species in df_history['species'].unique():
                    df_species = df_history[df_history['species'] == species]
                    color_species = df_species['color'].iloc[0]
                    ax[1].plot(df_species['step'], df_species['nr_animal'], color=color_species, label=species)

                ax[1].legend()

                buf = BytesIO()
                plt.savefig(buf, format='png')
                plt.close(fig)
                buf.seek(0)

                image = imageio.v3.imread(buf, extension='.png')
                writer.append_data(image)
                buf.close()

                print(f"______________________END OF STATE {i} RENDER______________________")
    
    def build_interaction_map(self):
        interaction_pos_all = []

        for animal in self.list_of_animals_all:
            animal.move()
            pos = animal.get_pos()

            if len(self.interaction_map[pos[0]][pos[1]]) == 0:
                interaction_pos_all.append(pos)

            self.interaction_map[pos[0]][pos[1]].append(animal)
        
        for pos in interaction_pos_all:
            print(pos)
            for animal in self.interaction_map[pos[0]][pos[1]]:
                print('\t',animal.species)

        return interaction_pos_all

    def animal_interaction(self, animal_a: Animal, animal_b: Animal):
        if animal_a == animal_b:
            return False

        if animal_b.species in self.foodnet[animal_a.species]: # animal_b is a pray animal of animal_a
                animal_a.hunt(animal_b)
        elif animal_a.species in self.foodnet[animal_b.species]: # animal_a is a pray animal of animal_b
                animal_b.hunt(animal_a)
        else:
            pass

        return True

    def simulate_interactions_pos(self, animals_interact_pos: list[Animal]):
        nr_animals = len(animals_interact_pos)
        random.shuffle(animals_interact_pos)

        for i in range(0, nr_animals-1):
            animal_a = animals_interact_pos[i]
            
            if animal_a.alive:
                for j in range(i+1, nr_animals):
                    animal_b = animals_interact_pos[j]
                    
                    if animal_b.alive:
                        self.animal_interaction(animal_a, animal_b)
                    else:
                        pass
            else:
                pass
        
        return True

    def generate_interaction_zone(self, pos, range_):
        x, y = pos
        size_x, size_y = self.map_size

        x_min = max(0, int(math.floor(x - range_)))
        x_max = min(size_x - 1, int(math.ceil(x + range_)))
        y_min = max(0, int(math.floor(y - range_)))
        y_max = min(size_y - 1, int(math.ceil(y + range_)))

        zone = [
            [(i, j), math.hypot(i - x, j - y)]
            for i in range(x_min, x_max + 1)
            for j in range(y_min, y_max + 1)
            if math.hypot(i - x, j - y) <= range_
        ]
        zone.sort(key=lambda item: item[1])
        zone = [coord for coord, _ in zone]

        return zone

    def simulate_interactions(self):
        nr_animals = len(self.list_of_animals_all)
        random.shuffle(self.list_of_animals_all)
        
        for i in range(nr_animals - 1, -1, -1):
            animal = self.list_of_animals_all[i]
            
            if animal.is_alive():
                pos = animal.get_pos()
                feed_range = animal.get_feed_range()
                interaction_zone = self.generate_interaction_zone(pos, feed_range)

                if animal.get_species() == 'lion':
                    #animal.print_animal()
                    print(len(interaction_zone))
                    print(interaction_zone[:1000])

                    for pos in interaction_zone:
                        if len(self.interaction_map[pos[0]][pos[1]]) == 0:
                            for a in self.interaction_map[pos[0]][pos[1]]:
                                print(a.species)

                for pos in interaction_zone:
                    if len(self.interaction_map[pos[0]][pos[1]]) == 0:
                        for animal_b in self.interaction_map[pos[0]][pos[1]]:
                            self.animal_interaction(animal, animal_b)

            else:
                self.list_of_animals_all.pop(i)
    
    def feed_from_ground(self):

        nr_animals = len(self.list_of_animals_all)

        for i in range(nr_animals - 1, -1, -1):
            animal = self.list_of_animals_all[i]

            if animal.alive:
                pos = animal.get_pos()

                if self.map_.field[pos[0]][pos[1]][1] in self.foodnet[animal.species]:
                    consumed = animal.eat_field(self.map_.field[pos[0]][pos[1]][2])
                    self.map_.field[pos[0]][pos[1]][2] -= consumed
            else:
                self.list_of_animals_all.pop(i)

    def append_animal_state(self, step):
        state = []
        nr_animal = len(self.list_of_animals_all)
        for i in range(nr_animal-1, -1, -1):
            animal = self.list_of_animals_all[i]
            
            if animal.alive:
                pos = animal.get_pos()
                species  = animal.get_species()
                color = animal.get_color()
                state.append([species, color, pos[0], pos[1]])
            else:
                self.list_of_animals_all.pop(i)
        
        df_animal_state = pd.DataFrame(state, columns = ['species', 'color', 'x', 'y'])
        df_animal_state['step'] = step
        self.animal_state_all.append(df_animal_state)
    
    def append_map_state(self, step):
        #df_map_state = self.map_.get_state()
        #df_map_state['step'] = step
        #self.map_state_all.append(df_map_state)

        self.map_state_all.append(None)

    def end_of_step(self):
        new_born_all = []
        nr_animal = len(self.list_of_animals_all)
        
        for i in range(nr_animal-1, -1, -1):
            animal = self.list_of_animals_all[i]
            animal.get_older()

            if animal.is_alive():
                if animal.gender == 'Female':
                    nr_offsprings = animal.bread()
                    pos = animal.get_pos()

                    for j in range(nr_offsprings):
                        offspring = Animal(self.map_size, self.species_all[animal.species])
                        offspring.position = pos
                        new_born_all.append(offspring)

                
            else:
                self.list_of_animals_all.pop(i)
                i -= 1
        
        self.list_of_animals_all += new_born_all
    
    def start(self):

        self.append_animal_state(0)
        self.append_map_state(0)
        
        for i in range(1, self.simulation_steps + 1):
        
            interaction_pos_all = self.build_interaction_map()
            """
            for pos in interaction_pos_all:
                animals_interact_pos = self.interaction_map[pos[0]][pos[1]]
                self.simulate_interactions_pos(animals_interact_pos)
                
                self.interaction_map[pos[0]][pos[1]] = []
            """

            self.simulate_interactions()

            self.feed_from_ground()

            for pos in interaction_pos_all:
                self.interaction_map[pos[0]][pos[1]] = []

            self.end_of_step()
            self.map_.regenare_grass()

            self.append_animal_state(i)
            self.append_map_state(i)

            if len(self.list_of_animals_all) == 0:
                print(f"_________________________GLOBAL EXTINSION AT STEP {i}_________________________")
                break
            else: 
                print(f"_________________________END OF STEP {i}_________________________")

                       
        
        if self.generate_simulation_gif:
            self.generate_gif()
        
        return self.animal_state_all, self.map_state_all
