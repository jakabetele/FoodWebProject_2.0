import pandas as pd

import warnings
warnings.filterwarnings("ignore")

class Map(object):
    def __init__(self, color_dictionary: dict, map_config_obj: dict, ):
        
        self.color_dictionary = color_dictionary

        self.size_x = map_config_obj["size_x"]
        self.size_y = map_config_obj["size_y"]

        height = map_config_obj["layers"]["height"]
        type = map_config_obj["layers"]["type"]
        nutrition = map_config_obj["layers"]["nutrition"]
        regeneration = map_config_obj["layers"]["regeneration"]

        self.field = []
        for height_row, type_row, nutrition_row, regeneration_row in zip(height, type, nutrition, regeneration):
            field_row = []

            for h, t, n, r in zip(height_row, type_row, nutrition_row, regeneration_row):
                field_row.append([h, t, n, r])
            
            self.field.append(field_row)
    
    def regenare_grass(self):

        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.field[x][y][1] == 'grass':
                    self.field[x][y][2] = min(self.field[x][y][2] + self.field[x][y][3], 1)
    
    def get_state(self):
        res_all = []

        for x in range(self.size_x):
            for y in range(self.size_y):
                type_ = self.field[x][y][1]
                value = self.field[x][y][2]

                color = self.color_dictionary[type_]['color']
                alpha = value/ self.color_dictionary[type_]['max']

                res_all.append([x, y, color, alpha])
        
        df_map_state = pd.DataFrame(res_all, columns= ['x', 'y', 'color', 'alpha'])
        return df_map_state


                    
