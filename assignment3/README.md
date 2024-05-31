# Assignment 3: Query expansion with word embeddings


###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment3) 

In this assignment we were asked to create a little tool which takes artist and word as input expands to words, look through a csv containing lyrics and determine a percentage of songs related to that search.

> **This is from the Assignment instructions linked above:** <br>
>
>   You should write a script which does the following:
> - Loads the song lyric data
> - Downloads/loads a word embedding model via gensim
> - Takes a given word as an input and finds the most similar words via word embeddings
> - Find how many songs for a given artist feature terms from the expanded query
> - Calculate the percentage of that artist's songs featuring those terms
> - Print and/or save results in an easy-to-understand way
>   - For example, "45% of {ARTIST}'s songs contain words related to {SEARCH TERM}"

<br>

```query_expansion.py``` analyzes song lyrics. It loads a pretrained GloVe model and a Spotify dataset to see if the artist is in the dataset, and then sift through the lyrics to find and print the percentage of songs containing the specified words both the query and the expanded query by the Glove model.It is to function like a little CLI (Client Command Interface).
<br><br>

## Content table

1. [Introduction](#assignment-3-query-expansion-with-word-embeddings)
2. [Project Structure](#project-structure)
3. [Data Source](#data-source)
4. [Usage](#usage)
5. [Flags](#flags)
6. [Compatibility & Other Uses](#compatibility--other-uses)
7. [Limitations & Possible Improvements](#limitations--possible-improvements)
<br>



## Project Structure

```
assignment3/
├── in/
│   └── Spotify Million Song Dataset_exported.csv
├── src/
│   └── query_expansion.py
├── createVEnv.sh
├── image.png
├── README.md
├── requirements.txt
├── run_custom.sh
└── run.sh
```

## Data source

The data contains lyrics from 57,650 English-language songs. It can be accessed [Here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs)


## Usage

**<u> The program is written for Python v.3.12.3, other versions might not function or produce unexpected behaviour. </u>**

1. Clone the repository

    ``` sh
    git clone  https://github.com/Revo1999/cds-lang.git
    ```

<br><br>

2. Insert the data as so it matches the folder-structure provided in Project structure.

<br><br>

3. Change directory into the assignment3 directory <br>
    ``` sh
    cd assignment3
    ```

    <br><br>

4. Setup virtual environment containing the packages needed to run both programs. <br>
    ``` sh
    bash createVEnv.sh
    ```

<br><br>

5. Runs ```query_expansion.py``` by activating the virtual environment, and after the program has ran it will close the environment again.<br>
    ``` sh
    bash run.sh
    ```

 <br><br>

 6. **For custom execution** use ```run_custom.sh``` it's a sh file that will ask you for inputs and automatically add the flags and run the program in similar fashion to ```run.sh```
    ``` sh
    bash run_custom.sh
    ```
    
    > Example here:![Description](image.png?raw=true)
    
## Flags
### Arguments for ```query_expansion.py```:

- `-m`, `--model_words_amount`: How many words most similar model supplies (default: 3).
- `-a`, `--artist`: Name of the artist (default: "pHiL CoLlins").
- `-w`, `--word`: The word you're searching for (default: "AiR").
- `-e`, `--extended_search`: Provides a printed list of the most similar words that extend your search (default: False).



## Compatibility & other uses

The program is written quite specifically for this. But you could (with quite some effort) alter the code to read other csv's.


## Limitations & possible improvements

As of now the program relies on argparse to obtain the information the get the query. This also means that every time i need to send a query a bash script with flags is executed, further this implies that the whole program runs everytime. In the program loading the model takes longest. In an ideal world the program could be executed in python interactive mode, load the model once, and then take inputs. The pros of this is that if you have several queries the program can handle them much faster. The cons is if you have one query now, the setup is a little bit more consuming. The program has been tracked with codecarbon for further documentation on this check out the bottom of this readme. The results show how much emission is created from the different parts of the program. This can rougly be translated to how much computing power each part of the program uses. Here's the results:

![Description](https://github.com/Revo1999/cds-lang/blob/main/emissions(assignment5)/out/assignment3_emissions.png?raw=true)

## Emissions

*Codecarbon has been used to track the environmental impact of running this code which equates to:* **0.15 of co2-equivalents in grams**

For calculation documentation see [Emissions](https://github.com/Revo1999/cds-lang/tree/main/emissions(assignment5))





