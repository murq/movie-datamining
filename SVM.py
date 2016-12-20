import pandas
import numpy
import sklearn
from sklearn import preprocessing
from sklearn import svm
from sklearn.grid_search import GridSearchCV


csvFile = pandas.read_csv('Datasets/train.csv')
data = numpy.array(csvFile)

#We won't be using the first column (movie title)
X_train = data[:,1:-1]
y_train = data[:,-1]
X_train_scaled = preprocessing.scale(X_train)

#SVM with rbf kernel
rbf_params = {'C':numpy.logspace(-3,4,8), 'kernel':['rbf'],'gamma':numpy.logspace(-3,4,8)}
rbf_grid = GridSearchCV(svm.SVC(), param_grid=rbf_params, cv=20, n_jobs=4, verbose=5)
print 'Starting rbf fit...'
rbf_grid.fit(X_train_scaled,y_train)
print "Best Params=",rbf_grid.best_params_, "Accuracy=", rbf_grid.best_score_
val_rbf = rbf_grid.best_params_

#SVM with linear/polynomial kernel
poly_params = {'C':numpy.logspace(-3,4,8), 'kernel':['poly'],'degree':range(1,5)} #C=[0.001,0.01,0.1,1,10,100,1000,10000], degree=[1,2,3,4]
poly_grid = GridSearchCV(svm.SVC(), param_grid=poly_params, cv=20, n_jobs=4, verbose=5)
print 'Starting poly fit...'
poly_grid.fit(X_train_scaled,y_train)
print "Best Params=",poly_grid.best_params_, "Accuracy=", poly_grid.best_score_
val_poly = poly_grid.best_params_

#Read the test data and scale it
csvFile = pandas.read_csv('Datasets/test.csv')
data = numpy.array(csvFile)
X_test = data[:,1:-1]
y_test = data[:,-1]
X_test_scaled = preprocessing.scale(X_train)

#Validation of the rbf kernel
val_rbf = {'kernel':'rbf', 'C':100, 'gamma':0.001}
rbftest = svm.SVC(C=val_rbf['C'], kernel=val_rbf['kernel'], gamma=val_rbf['gamma'])
rbftest.fit(X_train_scaled, y_train)
pred = rbftest.predict(X_test_scaled)
print sklearn.metrics.confucion_matrix(y_test,pred)
print sklearn.metrics.accuracy_score(y_test, pred)

#Validation of the linear/polynomial kernel
val_poly = {'kernel':'rbf', 'C':100, 'gamma':0.001}
polytest = svm.SVC(C=val_rbf['C'], kernel=val_rbf['kernel'], gamma=val_rbf['gamma'])
polytest.fit(X_train_scaled, y_train)
pred = rbftest.predict(X_test_scaled)
print sklearn.metrics.confucion_matrix(y_test,pred)
print sklearn.metrics.accuracy_score(y_test, pred)
