from microfilter.univariate.expnormdist import ExpNormDist
import numpy as np
from scipy.stats import skewnorm
import random
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt


def sim_data():
    a = random.choice([2., 3., 4.])
    ys = skewnorm.rvs(a, size=1000)
    outliers = [ random.choice([-1.,1.])*10. if np.random.rand()<0.05 else 0. for _ in ys]
    xs = np.cumsum(0.1*np.random.randn(1000))
    zs = [x + y + o for x, y, o in zip(xs, ys, outliers)]
    return zs

if __name__=='__main__':
    dist = ExpNormDist()
    zs = sim_data()
    zs_train = zs[:500]
    zs_test = zs[500:]
    dist.hyper_params['max_evals']=500
    dist.fit(lagged_values=list(reversed(zs_train)),lagged_times=[1. for _ in zs_train])
    pprint(dist.params)
    anchors = list()
    for z in zs_test:
        dist.update(value=z,dt=None)
        anchors.append(dist.state['anchor'])
    df = pd.DataFrame(columns=['original','smoothed'])
    df['original'] = zs_test
    df['smoothed'] = anchors
    df.plot()
    plt.show()
