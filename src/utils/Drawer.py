import matplotlib.pyplot as plt
import matplotlib


# matplotlib.use('TKAgg')
class Drawer:
    def __init__(self):
        str_dict = {
            "point": "o",
        }
        pass

    def create_canvas(self, m, n):
        self.fig, self.ax = plt.subplots(m, n, figsize=(m, n * 2))

    def get_window(self, window):
        return self.ax[window]

    def draw(self, *args, channel, feature):

        self.ax[channel, feature].plot(*args)
        self.fig.savefig("./results/plots/draw_func_plot.png")

    def scatter(self, *args, channel, feature):
        self.ax[channel, feature].scatter(*args)
        self.fig.savefig("./results/plots/scatter_func_plot.png")

    def show(self):
        plt.show()
