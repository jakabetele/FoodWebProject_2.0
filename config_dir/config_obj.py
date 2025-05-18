foodnet_config_obj = {
    "lion" : ["wildcat", "rabbit"],
    "wildcat": ["rabbit"],
    "rabbit": ["grass"]
}

animals_config_obj = [
            {
             "number": 3,
             "animal": {"species" : "rabbit",                #
                        "color" : "gray",               #
                        "initial_energy" : 0.4,              #The energy whith which the animal is born
                        "nutrition_value" : 0.2,             #The energy value for predator 
                        "life_expectancy" : (15, 3),         #The expected life length and the std coefficient
                        "maturity" : (5, 0.3, 3),            #The time from which it can reproduce and its std coefficients (pre maturity and post maturity)
                        "fertility" : (0.5, 4, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.5,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.1, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (10, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (10.0, 2),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            },"""
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
            }"""
]


plot_config_obj = {
    "figsize" : (12, 10)
}