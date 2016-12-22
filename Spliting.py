import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

import csv
# # Configure paths to your dataset files here
DATASET_FILE = 'metadata_clean_category_mean'
FILE_TRAIN = 'train_' + DATASET_FILE
FILE_TEST = 'test_' + DATASET_FILE



# dataset
data = pd.read_csv(DATASET_FILE+'.csv')

# separate target variable from dataset
X = data.drop('imdb_score',axis = 1)
Y = data['imdb_score']


sss = StratifiedShuffleSplit(n_splits= 1, test_size=0.2)
sss.get_n_splits(X, Y)

# Stratified Split of train and test data

val = False
count = 0
for train_index, test_index in sss.split(X, Y):
    xtrain, xtest = X.iloc[train_index], X.iloc[test_index]
    ytrain, ytest = Y[train_index], Y[test_index]

    train_dataset = xtrain.join(ytrain)
    test_dataset = xtest.join(ytest)

    train_dataset.to_csv(FILE_TRAIN + '.csv')
    test_dataset.to_csv(FILE_TEST + '.csv')