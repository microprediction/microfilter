from microfilter.univariate.expnormdist import ExpNormDist
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
from microfilter.univariate.noisysim import sim_data

if __name__=='__main__':
    dist = ExpNormDist()
    zs = sim_data(chronological=True)
    zs_train = zs[:500]
    zs_test = zs[500:]
    dist.hyper_params['max_evals']=10
    dist.fit(lagged_values=list(reversed(zs_train)),lagged_times=[1. for _ in zs_train])
    pprint(dist.params)
    anchors = list()
    for z in zs_test:
        dist.update(value=z,dt=None)
        anchors.append(dist.state['anchor'])
    df = pd.DataFrame(columns=['original','smoothed'])
    df['original'] = zs_test
    df['smoothed'] = anchors
    df['prediction'] = df['smoothed'].shift(-1)
    df[['original','prediction']].plot()
    plt.show()

