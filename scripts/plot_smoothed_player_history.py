import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

x=[]
y=[]

with open("x-data.txt",'r') as xd:
    for line in xd:
        x.append(int(line.strip()))
xd.close()
with open("y-data.txt",'r') as yd:
    for line in yd:
        y.append(int(line.strip()))
yd.close()

# Sample data
t = np.linspace(0, 10, 100)  # Time points
f = np.sin(t) + np.random.normal(0, 0.1, size=100)  # Discrete function with added noise

# Apply Savitzky-Golay filter for smoothing
smoothed_f = savgol_filter(y, window_length=20, polyorder=1)

# Find local minima and maxima
local_minima = np.where((smoothed_f[1:-1] < smoothed_f[:-2]) & (smoothed_f[1:-1] < smoothed_f[2:]))[0] + 1
local_maxima = np.where((smoothed_f[1:-1] > smoothed_f[:-2]) & (smoothed_f[1:-1] > smoothed_f[2:]))[0] + 1

# Print the identified local minima and maxima
# print("Local Minima:", x[local_minima])
# print("Local Maxima:", x[local_maxima])

plt.semilogy(x,y)
plt.semilogy(x,smoothed_f)
plt.show()