foodnet_config_obj = {
    "lion" : ["wildcat", "rabbit"],
    "wildcat": ["rabbit"],
    "rabbit": ["grass"]
}

animals_config_obj = [
            {
             "number": 100,
             "animal": {"species" : "rabbit",                #The species name
                        "color" : "gray",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.3,              #The energy whith which the animal is born
                        "nutrition_value" : 0.5,             #The energy value for predator
                        "feed_range" : 1.0,                  #The distance in which it can eat from field or hunt
                        "life_expectancy" : (15, 3),         #The expected life length and the std coefficient
                        "maturity" : (9, 3),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.3, 3, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.5,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.1, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (10, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (10.0, 1),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            },
            {
             "number": 10,
             "animal": {"species" : "wildcat",                #The species name
                        "color" : "black",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.75,              #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 2.0,                   #The distance in which it can eat from field or hunt 
                        "life_expectancy" : (20, 3),         #The expected life length and the std coefficient
                        "maturity" : (10, 2),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.5, 2, 0.5),          #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.4,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.1, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (10, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (15.0, 1),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.2                  #The cost of a fight
                        }
            }
            ,
            {
             "number": 1,
             "animal": {"species" : "lion",                #The species name
                        "color" : "orange",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.9,              #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 200.0,                  #The distance in which it can eat from field or hunt
                        "life_expectancy" : (25, 3),         #The expected life length and the std coefficient
                        "maturity" : (10, 2),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.8, 2, 0.5),          #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.4,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.0, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (10, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (25.0, 4),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.2                  #The cost of a fight
                        }
            }
]

simulation_config_obj = {
    "simulation_steps" : 1,
    "generate_simulation_gif" : True,
    "frame_duration" : 3.0,
    "save_path" : "D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/",
    "plot_config_obj" : {
        "figsize" : (12, 10)
    }
}

"""
            {
            "number": 40,
            "animal": {"species_name" : "wildcat", "species_type" : "carnivore",
                       "initial_energy" : 0.5,
                       "life_expectancy" : (30, 5), "maturity" : (8, 1.0),
                       "fertility" : (0.4, 2), "min_energy_to_bread" : 0.7,
                       "mobility" : (14, 2), "unit_energy_consumption" : 0.1,
                       "fight_stat" : 15.0, "fight_costs" : (0.2, 0.05)  
                      }
            },
            {
            "number": 10,
            "animal": {"species_name" : "lion", "species_type" : "carnivore",
                       "initial_energy" : 0.5,
                       "life_expectancy" : (40, 5), "maturity" : (10, 1.5),
                       "fertility" : (0.3, 2), "min_energy_to_bread" : 0.6,
                       "mobility" : (30, 2), "unit_energy_consumption" : 0.2,
                       "fight_stat" : 20.0, "fight_costs" : (0.2, 0.05)  
                      }
            }
"""