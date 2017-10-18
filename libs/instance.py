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
    
def plot_instances(instances, alpha=1):
    srt = {}
    basic_format = 'x' #x
    plt.axis([-1, 1, -1, 1])
    plt.grid(True)
    plt.xlabel('X_1')
    plt.ylabel('X_2')
    for i in instances:
        if not i.y in srt:
            srt[i.y] = []
        srt[i.y].append(i)
    idx = 0
    for cls in srt.keys():
        idx = idx + 1
        frm = basic_format
        clr = matplotlib.colors.to_rgba(PALETE[idx%len(PALETE)], alpha)
        x0 = [x.x[0] for x in srt[cls]]
        x1 = [x.x[1] for x in srt[cls]]
        plt.plot(x0, x1, frm, color=clr)
        plt.title(cls)
    plt.show()
    