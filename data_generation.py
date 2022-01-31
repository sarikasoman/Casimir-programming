import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mus = [2,6]
sigmas = [0.4,0.7]
x = np.linspace(0,10,1000)

data = np.zeros(shape=x.shape)
for m,s in zip(mus,sigmas):
    data += norm.pdf(x, m, s)
    
noise = np.random.random(data.shape) * 0.1
data = data + noise

plt.plot(x, data)
