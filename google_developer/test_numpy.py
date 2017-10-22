# import numpy as np


# arr = np.array([[10,20,30,40],[1,2],])

# nearr =  np.array([99,88,77])

# appArr = np.concatenate([90,89], axis=0)


# print appArr

# # delm= np.delete(appArr, [0,1,2])

# # print delm


from sklearn.datasets import load_iris


iris = load_iris()
print iris.target[[0,50,100]]