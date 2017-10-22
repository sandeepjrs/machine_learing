




#
# #LESSION - 2
#
#
# from sklearn.datasets import load_iris
#
# iris = load_iris()
# print iris.feature_names


# Lession 4



from sklearn.datasets import load_iris
#
iris = load_iris()
X = iris.data  #all rows, if I do data[0] it gonna thrugh me row 0
y = iris.target #lables, if i do target[0], it gonna through me lable for row 0

# print (x,y)  => (array([ 7. ,  3.2,  4.7,  1.4]), 1)


from sklearn.cross_validation import  train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = .5)
from sklearn import tree

#here using  the desicion tree classfier it can be changed anytime based on the accuracy results
myClasfier = tree.DecisionTreeClassifier()



myClasfier.fit(X_train, y_train)
predictions = myClasfier.predict(X_test)
print  predictions


from sklearn.metrics import accuracy_score

print accuracy_score(y_test, predictions)











