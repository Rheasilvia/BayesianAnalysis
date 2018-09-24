import pymc3 as pm
from scipy import stats
import numpy as np

np.random.seed(42)
n_experiments = 4
theta_real = 0.35
data = stats.bernoulli.rvs(p=theta_real, size=n_experiments)
print (data)

# array([1, 0, 0, 0])