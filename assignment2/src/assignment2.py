from helperfunctions import colorbank
from joblib import dump

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

def tfidf_vect(X_name, y_name, save_model_path, training_split_value_percent, shuffle_seed, data_file_path):
   
    print('loading data...')

    data = pd.read_csv(data_file_path)

    X = data[X_name]
    y = data[y_name]

    print('training model')
    X_train, X_test, y_train, y_test = train_test_split(X,                                                  # texts for the model
                                                        y,                                                  # classification labels
                                                        test_size=(100-training_split_value_percent)/100,   # takes percent value of training in percent and converts to test and maps it between 0 and 1.
                                                        random_state=shuffle_seed) # Functions like seed does in perlin noise, the number corresponds to a specific shuffle in this sense.

    vectorizer = TfidfVectorizer(ngram_range = (1,2),     # unigrams and bigrams (1 word and 2 word units)
                                lowercase =  True,       # why use lowercase?
                                max_df = 0.95,           # remove very common words
                                min_df = 0.05,           # remove very rare words
                                max_features = 100)      # keep only top 100 features


    # first we fit to the training data...
    X_train_feats = vectorizer.fit_transform(X_train)

    #... then do it for our test data
    X_test_feats = vectorizer.transform(X_test)

    # get feature names
    feature_names = vectorizer.get_feature_names_out()

    #save model
    print('saving model')
    dump(vectorizer, save_model_path)
    print(colorbank.hackergreen + 'model saved' + colorbank.default)