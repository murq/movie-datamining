import pandas
import numpy
import sklearn
import sklearn.cross_validation as cv
import sklearn.naive_bayes as nb
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import cross_val_predict
from sklearn.metrics import accuracy_score
from sklearn import metrics


csvFile = pandas.read_csv('Datasets/train.csv')
data = numpy.array(csvFile)
#We won't be using the first column (movie title)
X = data[:,1:-1]
y = data[:,-1]

#20-fold cross validation with Naive Bayes
cv_scores = cross_val_score(nb.GaussianNB(), X=X, y=y, cv=20, scoring='accuracy')
print cv_scores
print numpy.mean(cv_scores)

print '************************************************************************************'
#With confusion matrix
predicted = cross_val_predict(nb.GaussianNB(), X=X, y=y,  cv=20)  
print sklearn.metrics.confusion_matrix(y, predicted)
print sklearn.metrics.accuracy_score(y, predicted)

print '************************************************************************************'
#Classification report
print metrics.classification_report(y, predicted)
