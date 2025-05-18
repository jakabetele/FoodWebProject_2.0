import warnings
warnings.filterwarnings("ignore")

class Map(object):
    def __init__(self, map_config_obj: dict):
        
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
                field_row.append([[h, t, n, r]])
            
            self.field.append(field_row)
    
    def regenare_grass(self):

        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.field[x][y][1] == 'grass':
                    self.field[x][y][2] = min(self.field[x][y][2] + self.field[x][y][3], 1)
                    
