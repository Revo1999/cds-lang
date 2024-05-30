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

## Table of contents


1. [Introduction](#assignment-1-extracting-linguistic-features-using-spacy)
2. [Project Structure](#project-structure)
3. [Data Source](#data-source)
4. [Usage](#usage)
5. [Compatibility & Other Uses](#compatibility--other-uses)
6. [Outputs](#outputs)
7. [Limitations & Possible Improvements](#limitations--possible-improvements)

<br>



## Project Structure

```
assignment1/
├── in/
│   └── USEcorpus/
│       ├── a1/
│       │   ├── 0100.a1.txt
│       │   ├── 0101.a1.txt
│       │   └── ...
│       ├── a2/
│       │   ├── 0100.a2.txt
│       │   └── ....
│       └── a3/
│           └── ..
├── src/
│   └── spacy_extract.py
├── out/
│   ├── a1_table.csv
│   ├── a2_table.csv
│   └── ...
├── createVEnv.sh
├── README.md
├── requirements.txt
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


## Output

Here is an example of the outputs found in the out folder:


|Filename   |RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|-----------|------------|------------|-----------|-----------|----------|----------|----------|
|2038.a1.txt|1822.03     |1440.68     |805.08     |395.48     |4         |0         |3         |
|1082.a1.txt|1303.78     |1395.05     |651.89     |664.93     |1         |0         |1         |
|0205.a1.txt|1398.77     |1619.63     |785.28     |711.66     |2         |0         |0         |
|1073.a1.txt|1488.55     |1450.38     |674.3      |712.47     |2         |0         |0         |
|0169.a1.txt|1492.92     |1415.7      |707.85     |592.02     |0         |0         |2         |
|1042.a1.txt|1574.34     |1438.29     |758.02     |894.07     |6         |0         |2         |

To gain real insights, or to use the output for analysis it needs to be coupled to something that can track the evolution of data throughout the datasets. For example you could track the number of unique persons, orginizations where you may assume a rise in these numbers could be indicative of more cultural knowledge. Or that evolution in these numbers could be indicative of the students english vocabulary improving.


## Limitations

The program does not present the data in an easy to understand matter, understood as the the data in the out folder is scattered across many csv's that dont present the whole picture.

## Emissions

*Codecarbon has been used to track the environmental impact of running this code which equates to:* **2.16 of co2-equivalents in grams**

For calculation documentation see [Emissions](https://github.com/Revo1999/cds-lang/tree/main/emissions)