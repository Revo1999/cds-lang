# Assignment 2: Text classification benchmarks

###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment1) 

In this assignment we were asked make two programs with binary classification models to determine if news were fake or not, one program using a logistic regression model the other using a mlp neural network model. Both from sci-kit learn.

> **This is from the Assignment instructions linked above:** <br>
>For this exercise, you should write some code which does the following:
> - Loop over each text file in the folder called in
> For this exercise, you should write two different scripts. 
> - One script should train a logistic regression classifier on the data.
> - The second notebook should train a neural network on the same dataset. 
> <br> <br>
>
> - Both notebooks should do the following:
>    - Save the classification report to a text file the folder called out
>    - Save the trained models and vectorizers to the folder called models
> - BONUS: You might want to challenge yourself to create a third script which vectorizes the data separately, and saves the new feature extracted dataset. That way, you only have to vectorize the data once in total, instead of once per script. Performance boost!

<br>
This project use sci-kit's logistic regression and mlp model to classify news as real or fake in fake_or_real_news.csv. The scripts produce a lr and mlp model saved as .joblib in the model folder,  metrics for both, as well as saves fitted data variable.
<br><br>

The structure of code is a little different in this assignment than my other. In this code all functions are kept in ```assignment2.py```. ```mlp.py```, ```lr.py``` & ```vectorize.py``` access the functions and makes the necessary calls. 

## Content table

1. [Introduction](#assignment-1-simple-image-search-algorithm)
2. [Project Structure](#project-structure)
3. [Data Source](#data-source)
4. [Usage](#usage)
5. [Flags](#flags)
6. [Compatibility & Other Uses](#compatibility--other-uses)
7. [Outputs](#outputs)
    1. [Compare Hist OpenCV](#compare-hist-opencv)
    2. [Nearest Neighbor Sci-kit Learn](#nearest-neighbor-sci-kit-learn)
8. [Limitations & Possible Improvements](#limitations--possible-improvements)

<br>



## Project Structure

```
assignment1/
├── in/
│   ├── image_0001.jpg
│   ├── image_0002.jpg
│   └── image_0003.jpg
├── out/
│   ├── compare_hist_image_0321.jpg_results.csv
│   ├── compare_hist.png
│   ├── nearest_neighbor_image_0321.jpg_results.csv
│   └── nearest_neighbor.png
├── src/
│   ├── nearest_neighbor.py
│   └── open_cv_compare_hist.py     
├── createVEnv.sh
├── README.md
├── requirements.txt
├── run_custom.sh
└── run.sh

```

## Data source

The data contains fake and real news including label and can be accessed [Here](https://github.com/lutzhamel/fake-news/blob/master/data/fake_or_real_news.csv)

<br>

## Usage

**<u> The program is written for Python v.3.12.3, other versions might not function or produce unexpected behaviour. </u>**

1. Clone the repository

    ``` sh
    git clone  https://github.com/Revo1999/cds-lang.git
    ```

<br><br>

2. Insert the data as so it matches the folder-structure provided in Project structure.

<br><br>

3. Change directory into the assignment2 directory <br>
    ``` sh
    cd assignment2
    ```

    <br><br>

4. Setup virtual environment containing the packages needed to run both programs. <br>
    ``` sh
    bash createVEnv.sh
    ```

<br><br>

5. Run ```vectorize.py```, ```lr.py``` & ```mlp.py``` by activating the virtual environment, and after the program has ran it will close the environment again.<br>
    ``` sh
    bash run.sh
    ```

 <br><br>

## Flags


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




## Compatibility & other uses

The program has quite a lot of flags which can be used to tailor whatever dataset you have to fit you needs.

## Outputs




