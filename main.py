import json


from config_dir.map_config import map_config_obj
from config_dir.config_obj import animals_config_obj

from src.Map import Map
from Animal import Animal

#from src.Simulation import Simulation

def main():

    map_ = Map(map_config_obj)

    print(map_)
    
    return True

main()
