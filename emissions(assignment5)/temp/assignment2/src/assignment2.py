import vrashelper as vh
from joblib import dump, load
import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import metrics


def tfidf_vect(X_name, y_name, save_model_path, training_split_value_percent, shuffle_seed, data_file_path, file_path_save_fitted_data):
   
    print('loading data...')

    data = pd.read_csv(data_file_path)

    X = data[X_name]
    y = data[y_name]

    
    X_train, X_test, y_train, y_test = train_test_split(X,                                                  # texts for the model
                                                        y,                                                  # classification labels
                                                        test_size=(100-training_split_value_percent)/100,   # takes percent value of training in percent and converts to test and maps it between 0 and 1.
                                                        random_state=shuffle_seed) # Functions like seed does in perlin noise, the number corresponds to a specific shuffle in this sense.


    print('training model')
    vectorizer = TfidfVectorizer(ngram_range = (1,2),    # unigrams and bigrams (1 word and 2 word units)
                                lowercase =  True,       # why use lowercase?
                                max_df = 0.95,           # remove very common words
                                min_df = 0.05,           # remove very rare words
                                max_features = 100)      # keep only top 100 features

    print('fitting data.')
    # first we fit to the training data...
    X_train_feats = vectorizer.fit_transform(X_train)

    #... then do it for our test data
    X_test_feats = vectorizer.transform(X_test)

    # get feature names
    feature_names = vectorizer.get_feature_names_out()


    #save model
    print('saving model')
    dump(vectorizer, save_model_path)
    print(vh.colorbank.hackergreen + 'model saved' + vh.colorbank.default)

    save_data = [feature_names, X_test_feats, X_train_feats, y_test, y_train]


    with open(file_path_save_fitted_data, 'wb') as file: 
        # A new file will be created 
        pickle.dump(save_data, file)


def load_fitted_data(filepath):
    print('loading fitted data')

    with open(filepath, "rb") as f:
        feature_names, X_test_feats, X_train_feats, y_test, y_train = pickle.load(f)

    print(vh.colorbank.hackergreen + 'data loaded' + vh.colorbank.default)

    return feature_names, X_test_feats, X_train_feats, y_test, y_train


def load_model(filepath):
    # Loading model
    print('loading model')
    clf = load(filepath)
    print(vh.colorbank.hackergreen + 'model loaded' + vh.colorbank.default)

    return clf

def write_metrics(out_path, y_test, y_pred):
    classifier_metrics = metrics.classification_report(y_test, y_pred)

    with open(out_path, 'w') as file:
        file.write(classifier_metrics)

def lr(model_path, data_path, out_path, shuffle_seed, dump_model_path):

    feature_names, X_test_feats, X_train_feats, y_test, y_train = load_fitted_data(data_path)

    clf = load_model(model_path)


    print('testing model')

    classifier = LogisticRegression(random_state=shuffle_seed).fit(X_train_feats, y_train)

    y_pred = classifier.predict(X_test_feats)

    write_metrics(out_path, y_test, y_pred)

    print('saving model')
    dump(classifier, dump_model_path)
    print(vh.colorbank.hackergreen + 'model saved' + vh.colorbank.default)


def mlp(model_path, data_path, out_path, shuffle_seed, dump_model_path, hidden_layers, max_iterations):

    feature_names, X_test_feats, X_train_feats, y_test, y_train = load_fitted_data(data_path)

    clf = load_model(model_path)


    print('testing model')

    classifier = MLPClassifier(activation = "logistic",
                           hidden_layer_sizes = (hidden_layers,),
                           max_iter=max_iterations,
                           random_state = shuffle_seed)

    #training the classifier on the training data
    classifier.fit(X_train_feats, y_train)

    # Predicting labels for the test set
    y_pred = classifier.predict(X_test_feats)

    write_metrics(out_path, y_test, y_pred)

    print('saving model')
    dump(classifier, dump_model_path)
    print(vh.colorbank.hackergreen + 'model saved' + vh.colorbank.default)