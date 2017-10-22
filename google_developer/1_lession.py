# LESSION - 1


from sklearn import tree
import re


# these are the features 140 is weight and 1/0 are hard and soft
features = [[140, 1], [150, 0], [131, 1], [155, 0]]


#corrospponding to above features these are the following lables.
labels = ["orange", "mango","orange", "mango"]

# its just an classifier with lots of rule inside it
clf = tree.DecisionTreeClassifier()

#training the data using the above data sets
clf = clf.fit(features, labels)


# now trying to predict the data using above dataset
print clf.predict([[190,0]])