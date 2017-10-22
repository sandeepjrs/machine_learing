from sklearn.datasets import load_iris

iris = load_iris()

# print iris.feature_names
# print iris.target_names

# print iris.data[0]
# print iris.target[0]

# for i in range(len(iris.target)):
#     print "examples {}, label {} ".format(iris.data[i], iris.target_names[iris.target[i]])


test_idx = [0,50,100]

print iris.target[test_idx]

