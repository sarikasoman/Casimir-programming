import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import find_peaks

mus = [2, 6]
sigmas = [0.4, 0.7]
x = np.linspace(0, 10, 1000)

data = np.zeros(shape=x.shape)
for m, s in zip(mus, sigmas):
    data += norm.pdf(x, m, s)

noise = np.random.random(data.shape) * 0.1
data = data + noise

# find the peaks and properties
peaks, properties = find_peaks(data, height=0,prominence=0.1, width=0.1)
npeak = len(peaks) # number of peaks
width = properties["widths"]

start = peaks-(width/2)
end = peaks+(width/2)
filtered =[]

# store the data near peaks into "filtered"
for i in range(0, npeak ):

    p_x=x[int(start[i]):int(end[i])]
    p_d=data[int(start[i]):int(end[i])]
    filtered.append({'peak_number':i, "x":p_x, "data":p_d})

# plot filtered data
for i in range(0,npeak):
    plt.plot(filtered[i]["x"], filtered[i]["data"])


plt.scatter(x[peaks],data[peaks],c="red") #mark peaks

plt.show()
print (properties["widths"])