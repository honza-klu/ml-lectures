import numpy as np

class Individual:
    def __init__(self, x):
        self.x = x        
        
class GanAlg:
    def __init__(self, fit_fun=None, area=(-1, 1, -1, 1), individuals=None, plot_size=None):
        self.fit_fun = fit_fun        
        self.area = area
        if individuals:
            self.individuals = individuals
        else:
            self.individuals = []
        self.plot_size = plot_size
            
    def _update_fit_landscape(self):
        X = np.arange(self.area[0], self.area[1], 0.25)
        Y = np.arange(self.area[2], self.area[3], 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = self.fit_fun(X, Y)
        self.land = Z
    def _draw_fit(self, ax):
        self._update_fit_landscape()
        ax.imshow(self.land, extent=(self.area[0], self.area[1], self.area[2], self.area[3]))
    def _draw_ind(self, ax):
        self._update_fit_landscape()
        x0 = [x.x[0] for x in self.individuals]
        x1 = [x.x[1] for x in self.individuals]
        ax.plot(x0, x1, 'x', color='r')
        ax.autoscale(False)
        self._draw_fit(ax)
        