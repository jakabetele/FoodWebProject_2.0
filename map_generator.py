import numpy as np
import pandas as pd

import random

import matplotlib.pyplot as plt

def generate_map(df_map_state):

    fig, ax = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [3, 1]})
    fig.tight_layout()

    

    plt.show()


def gen_map():
    with open("map_config.py", "a") as f:
        map_config = {}
        ma = [] 
        for i in range(500):
            row = []
            for j in range(500):
                row.append(10)
            ma.append(row)
    

        map_config.update({"height": ma})    
        #f.write("\"height\":")  
        #f.write(str(ma))

        

        ma = [] 
        for i in range(500):
            row = []
            for j in range(500):
                row.append("grass")
            ma.append(row)

        map_config.update({"type": ma})
        #f.write("\n\"type\":")
        #f.write(str(ma))

        ma = [] 
        for i in range(500):
            row = []
            for j in range(500):
                row.append(0.05)
            ma.append(row)

        map_config.update({"nutrition": ma})
        #f.write("\n\"nutrition\":")
        #f.write(str(ma))

        ma = [] 
        for i in range(500):
            row = []
            for j in range(500):
                row.append(0.01)
            ma.append(row)

        map_config.update({"regeneration": ma})
        #f.write("\n\"regeneration\":")
        #f.write(str(ma))
        
        f.write(str(map_config))
            
gen_map()
