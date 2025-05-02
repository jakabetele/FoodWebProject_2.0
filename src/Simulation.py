import matplotlib.pyplot as plt


class Simulation():

    def __init__(self, figsize = (12, 8)):

        # Setup parameters
        self.figsize = figsize

        # Inner parameters
        self.frame_nr = 0
        self.frame_list_all = []
        
        self.fig, self.ax = plt.subplots(2, 1, figsize = figsize, gridspec_kw={'height_ratios': [4, 1]})
        self.fig.tight_layout()

        plt.show()

    def generate_frame(self, df, x1_feature, y1_feature, c1_feature, x2_feature, y2_feature, c2_feature):

        self.ax[0].scatter(x = df[x1_feature], y = df[y1_feature], color = df[c1_feature])
        self.ax[1].plot(x = df[x2_feature], y = df[y2_feature], color = df[c2_feature])

        self.frame_list_all.append(self.fig.savefig(f"{self.frame_nr}.png", dpi=200))
        
Simulation()
