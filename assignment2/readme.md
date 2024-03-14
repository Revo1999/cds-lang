# Assignment 2 
###### Victor Rasmussen, Language Analytics, Aarhus University
-----

This project uses sci-kit's logistic regression and mlp model to classify news as real or fake in fake_or_real_news.csv. The scripts produce a lr and mlp model saved as .joblib in the model folder,  metrics for both, as well as saves fitted data variable.

[Download dataset here! Remember terms of use](https://github.com/lutzhamel/fake-news/blob/master/data/fake_or_real_news.csv)




## Project Structure

```
Assignment 2/
├── fitted_data/
│   └── fitted_variables (file)
├── in/
│   └── fake_or_real_news.csv
├── model/
│   ├── lr_classifier_model.joblib
│   ├── mlp_classifier_model.joblib
│   └── tfidf_vectorizor.joblib
├── out/
│   ├── lr_classifier_metrics.txt
│   └── mlp_classifier_metrics.txt      
├── src/
│   ├── assignment2.py
│   ├── helperfunctions.py
│   ├── lr.py
│   ├── mlp.py
│   └── vectorize.py
├── readme.md
├── requirements.txt
└── start.sh
```

## Dependencies

```
pandas
scikit-learn
numpy
```

 ### ```bash setup.sh``` will download dependencies

<br>
<br>

## Usage
Insert data from in as shown in the file tree at the top of the page, or simply run ```vectorize.py``` with ```-d "insert/full/path/and/filename.csv"``` Look below for full list of arguments for the functions

```vectorize.py``` will load and tfidf-vectorize fake_or_real_news.csv and save vector and fitted-variables

```lr.py``` performs sci-kit logistic regression model on vectors.
```mlp.py```performs sci-kit mlp model on vectors.
```assignment2.py``` contains functions which ```lr.py``` and ```mlp.py``` uses.
```helperfunctions.py``` contains ```work_here()``` and ```colorbank class``` and is a script in which i will try to add small handy things for python coding.

1. run ```bash setup.sh``` in console and accept to download dependencies
2. run ```python src\vectorize.py``` <u> note: vectorize.py will also save the fitted data for lr.py & mlp.py to use. This saves computational power. </u>
3. run ```python src\lr.py```
4. run ```python src\mlp.py``` <br> <br>
### Arguments for ```vectorize.py```:

- `-X`, `--X_name`: Name of the X value columns in the dataset (default: "text").<br><br>
- `-y`, `--y_name`: Name of the y value columns in the dataset (default: "label").<br><br>
- `-t`, `--training_test_split`: Decides the split ratio for training and testing data, default value is 80, meaning a split of 80/20 (default: 80). <br><br>
- `-s`, `--shuffle_seed`: Seed for shuffling the data (default: 42).<br><br>
- `-o`, `--overwrite_save_path`: Full save path for the trained TF-IDF vectorizer model (default: '../model/tfidf_vectorizor.joblib').<br><br>
- `-d`, `--data_input_path`: Input path for the CSV file to be vectorized (default: '../in/fake_or_real_news.csv').<br><br>
- `-f`, `--file_path_save_fitted_data`: Directory for saving fitted data (default: '../fitted_data/fitted_variables').<br><br>
<br>
<br>

### Arguments for ```lr.py```:

- `-m`, `--model_path`: File path to obtain the TF-IDF vectorizer model `.joblib` file (default: '../model/tfidf_vectorizor.joblib').<br><br>
- `-i`, `--input_path`: File path to obtain fitted data (default: '../fitted_data/fitted_variables').<br><br>
- `-o`, `--out_path`: File path to save logistic regression classifier metrics (must be a string and end with '.txt') (default: '../out/lr_classifier_metrics.txt').<br><br>
- `-s`, `--shuffle_seed`: Seed for shuffling the data (default: 42).<br><br>
- `-d`, `--dump_model_path`: File path to save logistic regression classifier model (must be a string and end with '.joblib') (default: '../model/lr_classifier_model.joblib').<br><br>


### Arguments for ```mlp.py```:

- `-m`, `--model_path`: File path to obtain the TF-IDF vectorizer model `.joblib` file (default: '../model/tfidf_vectorizor.joblib').<br><br>
- `-i`, `--input_path`: File path to obtain fitted data (default: '../fitted_data/fitted_variables').<br><br>
- `-o`, `--out_path`: File path to save MLP classifier metrics (must be a string and end with '.txt') (default: '../out/mlp_classifier_metrics.txt').<br><br>
- `-s`, `--shuffle_seed`: Seed for shuffling the data (default: 42).<br><br>
- `-d`, `--dump_model_path`: File path to save MLP classifier model (must be a string and end with '.joblib') (default: '../model/mlp_classifier_model.joblib').<br><br>
- `-mi`, `--max_iterations`: Maximum iterations parameter for MLP (default: 500).<br><br>
- `-hl`, `--hidden_layers`: Number of hidden layers parameter for MLP (default: 15).<br><br>
