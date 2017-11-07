import numpy as np
from copy import deepcopy

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
        Z = self.fit_fun((X, Y))
        self.land = Z
    def _draw_fit(self, ax):
        self._update_fit_landscape()
        ax.imshow(self.land, extent=(self.area[0], self.area[1], self.area[2], self.area[3]))
    def _draw_ind(self, ax):
        self._update_fit_landscape()
        x0 = [x.x[0] for x in self.individuals]
        x1 = [x.x[1] for x in self.individuals]
        self._draw_fit(ax)
        ax.plot(x0, x1, 'x', color='r')
        #ax.autoscale(False)        
    def calc_fit(self):
        self.fit = {}
        for ind in self.individuals:
            self.fit[ind] = self.fit_fun(ind.x)
    def mutate(self, ind):
        for i in range(0, len(ind.x)):
            ind.x[i] = ind.x[i] + np.random.normal(0.0, 0.3)            
    def make_selection(self):
        self.calc_fit()
        new_individuals = []
        fit_sum = 0
        for ind in self.individuals:
            fit_sum += self.fit[ind]
        while len(new_individuals)<len(self.individuals):
            #weighted roulet selection
            p = np.random.uniform(0, fit_sum)
            sel_sum = 0
            sel_ind = None
            for i in self.individuals:
                sel_ind = deepcopy(i)
                sel_sum = sel_sum + self.fit[i]
                if(sel_sum >= p):
                    break
            self.mutate(sel_ind)
            new_individuals.append(sel_ind)
        self.individuals = new_individuals
                