from sklearn import datasets
iris = datasets.load_iris()



X = iris.data  #data is like [.6,.9, .78] --> featuere
y = iris.target #label example [stosa] --> label

from sklearn.cross_validation import train_test_split

#splitting the data for the training test
# X_train and y_train are the feature and label for traing
# X_test and y_test are the feature and label for traing
# test_size = .5 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .5)



###################################################################
# # desisionTREE clasifire 
# # time to build the classfier
# from sklearn import tree
# #choosing the decision treee algothrim
# my_classifier = tree.DecisionTreeClassifier()
###################################################################
###########################<<-----OR--->>##########################
###################################################################
# KNeighbor clasifier
# time to build the classfier
from sklearn.neighbors import KNeighborsClassifier
#choosing the decision treee algothrim
my_classifier = KNeighborsClassifier()





###################################################################
#trinin the model using train data
my_classifier.fit(X_train, y_train)

#predection if the test data
predections = my_classifier.predict(X_test)

#this print the prediction of the label for each row
print predections


#lets see how much accurate our model is 

from sklearn.metrics import accuracy_score
#it takes the testing lables and predected label and gived the accuracy
print accuracy_score(y_test, predections)
