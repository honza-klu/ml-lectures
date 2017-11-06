import numpy as np

class Individual:
    def __init__(self, x):
        self.x = x        
        
class GanAlg:
    def __init__(self, fit_fun=None, area=(-1, 1, -1, 1)):
        self.fit_fun = fit_fun        
    def _draw_fit(self, ax):
        ax.imshow(Z, extent=(LOW_LIMIT, HIGH_LIMIT, LOW_LIMIT, HIGH_LIMIT))
    def _draw_ind(self, ax):
        pass