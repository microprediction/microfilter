from microfilter.univariate.expnormdist import ExpNormDist
import numpy as np
from scipy.stats import skewnorm
import random
from pprint import pprint
import pandas as pd

def sim_data():
    a = random.choice([2., 3., 4.])
    ys = skewnorm.rvs(a, size=1000)
    xs = np.cumsum(np.random.randn(1000))
    zs = [x + y for x, y in zip(xs, ys)]
    return zs


def test_expnormdist():
    dist = ExpNormDist()
    zs = sim_data()
    zs_train = zs[:500]
    zs_test = zs[500:]
    pprint(dist.params)
    anchors = list()
    for z in zs_test:
        dist.update(value=z,dt=None)
        anchors.append(dist.state['anchor'])
