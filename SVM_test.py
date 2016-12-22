import pandas
import numpy
import sklearn
from sklearn import preprocessing
from sklearn import svm


csvFile = pandas.read_csv('Datasets/train_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)
#We won't be using the first column (movie title)
X_train = data[:,2:-1]
y_train = data[:,-1]

csvFile = pandas.read_csv('Datasets/test_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)
X_test = data[:,2:-1]
y_test = data[:,-1]

X_train_scaled = preprocessing.scale(X_train)
X_test_scaled = preprocessing.scale(X_test)


print '\nValidation of the rbf kernel'
rbftest = svm.SVC(C=100, kernel='rbf', gamma=0.001)
rbftest.fit(X_train_scaled, y_train)
pred = rbftest.predict(X_test_scaled)
print rbftest.support_vectors_
print rbftest.support_vectors_.shape
print sklearn.metrics.confusion_matrix(y_test, pred)
print sklearn.metrics.accuracy_score(y_test, pred)

print '\nValidation of the polynomial kernel'
polytest = svm.SVC(C=10, kernel='poly', degree=3)
polytest.fit(X_train_scaled, y_train)
pred = polytest.predict(X_test_scaled)
print polytest.support_vectors_
print polytest.support_vectors_.shape
print sklearn.metrics.confusion_matrix(y_test, pred)
print sklearn.metrics.accuracy_score(y_test, pred)

print '\nValidation of the linear kernel'
lineartest = svm.SVC(C=10, kernel='linear')
lineartest.fit(X_train_scaled, y_train)
pred = lineartest.predict(X_test_scaled)
print lineartest.support_vectors_
print lineartest.support_vectors_.shape
print sklearn.metrics.confusion_matrix(y_test, pred)
print sklearn.metrics.accuracy_score(y_test, pred)


