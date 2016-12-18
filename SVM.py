import pandas
import numpy
import sklearn
from sklearn import svm
from sklearn.grid_search import GridSearchCV


csvFile = pandas.read_csv('metadata_clean_nomissing.csv')
data = numpy.array(csvFile)

#We won't be using the first column (movie title)
X = data[:,1:-1]
y = data[:,-1]

poly_params = {'C':numpy.logspace(-3,4,8), 'kernel':['poly'],'degree':range(1,4)} #C=[0.001,0.01,0.1,1,10,100,1000,10000], degree=[1,2,3,4]
poly_grid = GridSearchCV(svm.SVC(), param_grid=poly_params, cv=20)
poly_grid.fit(X,y)
print "Best Params=",poly_grid.best_params_, "Accuracy=", poly_grid.best_score_

rbf_params = {'C':numpy.logspace(-3,4,8), 'kernel':['rbf'],'gamma':numpy.logspace(-3,4,8)}
rbf_grid = GridSearchCV(svm.SVC(), param_grid=rbf_params, cv=20)
rbf_grid.fit(X,y)
print "Best Params=",rbf_grid.best_params_, "Accuracy=", rbf_grid.best_score_

