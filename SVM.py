import pandas
import numpy
import sklearn
from sklearn import preprocessing
from sklearn import svm
from sklearn.grid_search import GridSearchCV


csvFile = pandas.read_csv('Datasets/train_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)

#We won't be using the first column (movie title)
X_train = data[:,2:-1]
y_train = data[:,-1]
X_train_scaled = preprocessing.scale(X_train)

#SVM with rbf kernel
#rbf_params = {'C':numpy.logspace(-3,4,8), 'kernel':['rbf'],'gamma':numpy.logspace(-3,4,8)}
#rbf_grid = GridSearchCV(svm.SVC(), param_grid=rbf_params, cv=20, n_jobs=8, verbose=5)
#print 'Starting rbf fit...'
#rbf_grid.fit(X_train_scaled,y_train)
#print "Best Params=",rbf_grid.best_params_, "Accuracy=", rbf_grid.best_score_
#val_rbf = rbf_grid.best_params_

#SVM with linear kernel
linear_params = {'C':numpy.logspace(-3,3,7), 'kernel':['linear']} #C=[0.001,0.01,0.1,1,10,100,1000]
linear_grid = GridSearchCV(svm.SVC(), param_grid=linear_params, cv=20, n_jobs=8, verbose=5)
print 'Starting linear fit...'
linear_grid.fit(X_train_scaled, y_train)
print "Best Params=",linear_grid.best_params_, "Accuracy=", linear_grid.best_score_
val_linear = linear_grid.best_params_

#SVM with polynomial kernel
#poly_params = {'C':numpy.logspace(-3,3,7), 'kernel':['poly'],'degree':range(2,4)} #C=[0.001,0.01,0.1,1,10,100,1000], degree=[2,3]
#poly_grid = GridSearchCV(svm.SVC(), param_grid=poly_params, cv=20, n_jobs=4, verbose=5)
#print 'Starting poly fit...'
#poly_grid.fit(X_train_scaled,y_train)
#print "Best Params=",poly_grid.best_params_, "Accuracy=", poly_grid.best_score_
#val_poly = poly_grid.best_params_

#Read the test data and scale it
csvFile = pandas.read_csv('Datasets/test_metadata_clean_category_balanced.csv')
data = numpy.array(csvFile)
X_test = data[:,2:-1]
y_test = data[:,-1]
X_test_scaled = preprocessing.scale(X_test)

#Validation of the rbf kernel
#rbftest = svm.SVC(C=val_rbf['C'], kernel=val_rbf['kernel'], gamma=val_rbf['gamma'])
#rbftest.fit(X_train_scaled, y_train)
#pred = rbftest.predict(X_test_scaled)
#print sklearn.metrics.confusion_matrix(y_test,pred)
#print sklearn.metrics.accuracy_score(y_test, pred)

#Validation of the linear kernel
lineartest = svm.SVC(C=val_linear['C'], kernel=val_linear['kernel'])
lineartest.fit(X_train_scaled, y_train)
pred = lineartest.predict(X_test_scaled)
print sklearn.metrics.confusion_matrix(y_test,pred)
print sklearn.metrics.accuracy_score(y_test, pred)

#Validation of the polynomial kernel
#polytest = svm.SVC(C=val_poly['C'], kernel=val_poly['kernel'], degree=val_poly['degree'])
#polytest.fit(X_train_scaled, y_train)
#pred = polytest.predict(X_test_scaled)
#print sklearn.metrics.confusion_matrix(y_test,pred)
#print sklearn.metrics.accuracy_score(y_test, pred)
