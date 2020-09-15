# microfilter

Some ad-hoc approaches to filtering noisy data, using hyperopt

## Usage example

Train filter on simulated noisy data

    from microfilter.univariate.expnormdist import ExpNormDist
    from microfilter.univariate.noisysim import sim_lagged_values_and_times
    
    lagged_values, lagged_times = sim_lagged_values_and_times
    dist = ExpNormDist()
    dist.hyper_params['max_evals']=500
    dist.fit(lagged_values=lagged_values, lagged_times=lagged_times)
    pprint(dist.params) 
    new_value = 17.0
    dist.update(value=new_value, dt=1.0)
    pprint(dist.state) 
    
See https://github.com/microprediction/microfilter/blob/master/examples/plot_expnorm.py 
    
     
