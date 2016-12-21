import pandas
import numpy
import sklearn
import sklearn.cross_validation as cv
import sklearn.naive_bayes as nb
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import cross_val_predict
from sklearn.metrics import accuracy_score
from sklearn import metrics


csvFile = pandas.read_csv('Datasets/train_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)
#We won't be using the first column (movie title)
X_train = data[:,2:-1]
y_train = data[:,-1]

csvFile = pandas.read_csv('Datasets/test_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)
X_test = data[:,2:-1]
y_test = data[:,-1]

#20-fold cross validation with Naive Bayes
cv_scores = cross_val_score(nb.GaussianNB(), X=X_train, y=y_train, cv=20, scoring='accuracy')
print cv_scores
print numpy.mean(cv_scores)

print '************************************************************************************'
#With confusion matrix
predicted = cross_val_predict(nb.GaussianNB(), X=X_train, y=y_train,  cv=20)  
print sklearn.metrics.confusion_matrix(y_train, predicted)
print sklearn.metrics.accuracy_score(y_train, predicted)

print '************************************************************************************'
#Classification report
print metrics.classification_report(y_train, predicted)


print '************************************************************************************'
#Prediction
print 'Test dataset prediction:'
clf = nb.GaussianNB()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print metrics.classification_report(y_test, pred)
print metrics.confusion_matrix(y_test, pred, labels=['LET_57','GET_58_AND_LET_65','GET_66_AND_LET_71','GET_72'])
print metrics.accuracy_score(y_test, pred)
