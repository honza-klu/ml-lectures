from instance import Instance
import math
import numpy as np

class Knn:
    def __init__(self):
        self.train = []
    def _learn_list(self, l_x):
        for a in l_x:
            self.learn(a)
    def learn(self, x):
        if isinstance(x, list):
            print("Learning list")
            self._learn_list(x)
            return
        if x in self.train:
            print("Already in train set")
            return
        self.train.append(x)
    def _learn_list_ib2(self, l_x):
        for a in l_x:
            self.learn_ib2(a)
    def learn_ib2(self, l_x):
        if isinstance(l_x, list):
            print("Learning list")
            self._learn_list_ib2(l_x)
            return
        if len(self.train)==0: #always add first one
            self.learn(l_x)
            return
        cls = self.clasify(l_x)
        if cls != l_x.y:
            self.learn(l_x)
    def _dist(self, x, y):
        assert len(x.x)==2
        assert len(y.x)==2
        return math.sqrt((x.x[0]-y.x[0])**2+(x.x[1]-y.x[1])**2)
    def _find_nearest(self, x):
        assert len(self.train) > 0
        dist = float("inf")
        nearest = None
        for t in self.train:
            if self._dist(t, x)<dist:
                dist = self._dist(t, x)
                nearest = t
        return nearest
    def clasify(self, x):
        near = self._find_nearest(x)
        return near.y
    def clasify_list(self, l_x):
        for x in l_x:
            x.y = self.clasify(x)
        return l_x
    def get_map(self, num=50):
        map = []
        for x1 in np.linspace(-1.0, 1.0, num):
            for x2 in np.linspace(-1.0, 1.0, num):
                p = Instance([x1, x2], None)
                p.y = self.clasify(p)
                map.append(p)
        return map
        
    