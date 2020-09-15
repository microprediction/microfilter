from microfilter.univariate.expnormdist import ExpNormDist
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
from microfilter.univariate.noisysim import sim_data
import numpy as np

if __name__=='__main__':
    dist = ExpNormDist()
    zs = sim_data(chronological=True)
    zs_train = zs[:500]
    zs_test = zs[500:]
    zs_train[0] = np.nan
    zs_train[5] = np.nan
    zs_train[-1] = np.nan
    zs_train[-3] = np.nan
    dist.hyper_params['max_evals']=1000
    lagged_values = list(reversed(zs_train))
    lagged_times = [1. for _ in zs_train]
    loss = dist.loss(lagged_values=lagged_values, lagged_times=lagged_times,params=dist.params)
    dist.fit(lagged_values=lagged_values,lagged_times=lagged_times)
    pprint(dist.params)
    anchors = list()
    zs_test[0] = np.nan
    zs_test[5] = np.nan
    for z in zs_test:
        dist.update(value=z,dt=None)
        anchors.append(dist.state['anchor'])
    df = pd.DataFrame(columns=['original','smoothed'])
    df['original'] = zs_test
    df['smoothed'] = anchors
    df['prediction'] = df['smoothed'].shift(-1)
    df[['original','prediction']].plot()
    plt.show()

