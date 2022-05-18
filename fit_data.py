import numpy as np
import matplotlib.pytplot as plt

data = np.loadtext("example_data.csv", delimiter=",", skiprows=1)
plt.pot(data[:,0], data{:,1])
plt.show()
