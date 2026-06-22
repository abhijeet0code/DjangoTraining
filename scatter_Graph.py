import numpy as np
import matplotlib.pyplot as plt

range1=np.random.rand(2,12)
range2=np.random.rand(12,2)

plt.scatter(range1,range2,s=100)
plt.show()
