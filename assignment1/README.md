# Assignment 1: Extracting linguistic features using spaCy

###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment1) 

In this assignment we were asked to extract features from The Uppsala Student English Corpus using spaCy.

> **This is from the Assignment instructions linked above:** <br>
>For this exercise, you should write some code which does the following:
> - Loop over each text file in the folder called in
Extract the following information:
>   - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
>    - Total number of unique PER, LOC, ORGS
> - For each sub-folder (in the dataset: a1, a2, a3, ...) save a table which shows the following information:

<br>

```spacy_extract.py``` goes through txt-files and extracts: relative frequency of nouns, verbs, adjective, and adverbs per 10,000 words, aswell as total number of unique PER, LOC, ORGS per text, using spaCy. The program automatically removes meta-data (for the read files, not editing txt files)

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

The Uppsala Student English Corpus (USE). The data contains eassays written by Swedish students, collected over several years. The data can be accessed [here!](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457)

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

3. Change directory into the assignment1 directory <br>
    ``` sh
    cd assignment1
    ```

    <br><br>

4. Setup virtual environment containing the packages needed to run both programs. <br>
    ``` sh
    bash createVEnv.sh
    ```

<br><br>

5. Run ```spacy_extract.py``` by activating the virtual environment, and after the program has ran it will close the environment again.<br>
    ``` sh
    bash run.sh
    ```

 <br><br>

## Compatibility & other uses

The program can be used on other datasets, the dataset needs to be ".txt" (the program can be rewritten to accept other filetypes be bu then the reading functions needs to be changed.) The dataset needs to be structured in folders and will seperately process these.

## Limitations