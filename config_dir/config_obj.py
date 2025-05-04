foodnet_config_obj = [
    {"animal": "lion", "preys": ["wildcat", "rabbit"]},
    {"animal": "wildcat", "preys": ["rabbit"]},
    {"animal": "rabbit","preys": []}
]

animals_config_obj = [
            {
             "number": 3,
             "animal": {"species_name" : "rabbit", "species_type" : "herbivore",
                        "initial_energy" : 0.4,
                        "life_expectancy" : (15, 3), "maturity" : (5, 0.5),
                        "fertility" : (0.5, 4), "min_energy_to_bread" : 0.5,
                        "mobility" : (10, 2), "unit_energy_consumption" : 0.05,
                        "fight_stat" : 10.0, "fight_costs" : (0.1, 0.03)  
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