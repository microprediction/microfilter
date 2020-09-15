from microfilter.univariate.skewdist import SkewDist
import numpy as np
import scipy

if __name__ == '__main__':
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt
    except ImportError:
        raise (
            'You need to pip install seaborn and matplotlib for this example. Or ')

    '''EXAMPLE'''
    desired_mean = 497.68
    desired_skew = -1.75
    desired_sd = 77.24

    final_dist = SkewDist.skewed_sample(mean=desired_mean, sd=desired_sd, skew=desired_skew, num=225)

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.distplot(final_dist, hist=True, ax=ax, color='green', label='generated distribution')
    sns.distplot(np.random.choice(final_dist, size=225), hist=True, ax=ax, color='red', hist_kws={'alpha': .2},
                 label='sample n=100')
    ax.legend()

    print('Input mean: ', desired_mean)
    print('Result mean: ', np.mean(final_dist), '\n')

    print('Input SD: ', desired_sd)
    print('Result SD: ', np.std(final_dist), '\n')

    print('Input skew: ', desired_skew)
    print('Result skew: ', scipy.stats.skew(final_dist))

    fig.show()
