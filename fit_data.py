import numpy as np
import matplotlib.pytplot as plt

filename = "example_data.csv"
data = np.loadtext(filename, delimiter=",", skiprows=1)
plt.pot(data[:,0], data{:,1])
plt.show()
