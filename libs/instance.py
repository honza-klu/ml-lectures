import matplotlib
import matplotlib.pyplot as plt
import numpy as np

PALETE = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
class Instance:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#    def __str__(self):
#        ret = "%s %s" % (str(x), str(y),)
#        return ret

basic_format = 'x' #x
def _plot_points(instances, alpha, ms=5):
    srt = {}
    for i in instances:
        if not i.y in srt:
            srt[i.y] = []
        srt[i.y].append(i)
    idx = 0
    for cls in srt.keys():
        idx = idx + 1
        frm = basic_format
        clr = matplotlib.colors.to_rgba(PALETE[cls%len(PALETE)], alpha)
        x0 = [x.x[0] for x in srt[cls]]
        x1 = [x.x[1] for x in srt[cls]]
        plt.plot(x0, x1, frm, color=clr, markersize=ms)
        plt.title(cls)
        
def plot_instances(instances, alpha=1, map_instances=None, map_alpha=0.2, highlight=None):
    plt.axis([-1, 1, -1, 1])
    plt.grid(True)
    plt.xlabel('X_1')
    plt.ylabel('X_2')
    #instances
    _plot_points(instances, alpha)
    if map_instances:
        _plot_points(map_instances, map_alpha)
    if highlight:
        _plot_points([highlight], 1.0, ms=15)
    plt.show()
    