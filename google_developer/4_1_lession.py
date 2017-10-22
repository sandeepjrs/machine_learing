import numpy as np

import matplotlib.pyplot as plt 


# trying to have a 500dogs
greyhundsDogs = 500
labDogs = 500

# 500 different heights near around 28
grey_height = 28 + 4 * np.random.randn(greyhundsDogs)

labs_height = 24 + 4 * np.random.randn(labDogs)


# displaying a histogram
plt.hist([grey_height, labs_height], stacked = False, color=['r','b'])

plt.show()

