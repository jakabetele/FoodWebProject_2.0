import matplotlib.pyplot as plt

from FoodNet import FoodNet
from Map import Map

class Simulation():

    def __init__(self,
                 map: Map,
                 foodnet: FoodNet,
                 list_of_animals_all : list,
                 simulation_config_obj: dict):

        self.list_of_animals_all = list_of_animals_all
        self.foodnet = foodnet
        self.map = map
        self.simulation_length = simulation_config_obj['lenght']
        self.save_path = simulation_config_obj['save_path']
        self.plot_config_obj = simulation_config_obj['plot_config_obj']

        # Inner parameters
        self.frame_nr = 0
        self.frame_list_all = []

        self.figsize = self.plot_config_obj['figsize']
        self.fig, self.ax = plt.subplots(2, 1, figsize = self.figsize, gridspec_kw={'height_ratios': [4, 1]})
        self.fig.tight_layout()

    def start(self):
        for i in range(self.simulation_length):
            print(i)

    def generate_frame(self, df, x1_feature, y1_feature, c1_feature, x2_feature, y2_feature, c2_feature):

        self.ax[0].scatter(x = df[x1_feature], y = df[y1_feature], color = df[c1_feature])
        self.ax[1].plot(x = df[x2_feature], y = df[y2_feature], color = df[c2_feature])

        self.frame_list_all.append(self.fig.savefig(f"{self.frame_nr}.png", dpi=200))
    
        
Simulation()
