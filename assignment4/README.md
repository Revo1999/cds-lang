# Assignment 4: Emotion analysis with pretrained language models


###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment4) 

In this assignment we were asked to create a python script for computational analysis of the Game Of Throne script.

> **This is from the Assignment instructions linked above:** <br>
>
> - Predict emotion scores for all lines in the data
> - For each season
>    - Plot the distribution of all emotion labels in that season
> - For each emotion label
>   - Plot the relative frequency of each emotion across all seasons

<br>

```Predictor.py``` This program loads a CSV containing Game of Thrones scripts, uses a pretrained model ( [this one](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) ) to classify emotions in each line, and saves the results. Then the program visualizes the relative frequency of each emotion per season in a line chart and creates bar charts for emotion counts in each season.
<br><br>

## Table of Contents

1. [Introduction](#assignment-4-emotion-analysis-with-pretrained-language-models)
2. [Project Structure](#project-structure)
3. [Data Source](#data-source)
4. [Usage](#usage)
5. [Compatibility & Other Uses](#compatibility--other-uses)
6. [Limitations & Possible Improvements](#limitations--possible-improvements)
7. [Output](#output)
<br>



## Project Structure

```
assignment4/
├── in/
│   └── Game_of_Thrones_script.csv
├── out/
│   ├── Barchart_Season 1.png'
│   ├── ..
│   ├── Barchart_Season 8.png
│   ├── LineChart.png
│   └── with_predictions.csv
├── src/
│   └── predicter
├── createVEnv.sh
├── README.md
├── requirements.txt
└── run.sh

```

## Data source

The data contains all lines from The Game Of Thrones series and can be accessed [Here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv).


## Usage

**<u> The program is written for Python v.3.12.3, other versions might not function or produce unexpected behaviour. </u>**

1. Clone the repository

    ``` sh
    git clone  https://github.com/Revo1999/cds-lang.git
    ```

<br><br>

2. Insert the data as so it matches the folder-structure provided in Project structure.

<br><br>

3. Change directory into the assignment4 directory <br>
    ``` sh
    cd assignment4
    ```

    <br><br>

4. Setup virtual environment containing the packages needed to run both programs. <br>
    ``` sh
    bash createVEnv.sh
    ```

<br><br>

5. Runs ```predictor.py``` by activating the virtual environment, and after the program has ran it will close the environment again.<br>
    ``` sh
    bash run.sh
    ```

 <br><br>




## Compatibility & other uses

The program is written quite specifically for this. Needs a lot of rewriting to accomadate other datasets. Unless data has exactly the same column names.


## Limitations & possible improvements

The program could have been written to accomodate different datasets better. It might be possible to preprocess the lines and remove certain lesser important word, this might make the model faster in general. Though this might negatively impact accuracy (this can not be measured), as the model is trained on complete sentences.

More visualization could further give insights. Following specific character emotion across seasons (this could lead to spoilers if a character is dead or written out). Emotions across episodes could also give insights to how episodes generally might unfold.

## Output

The distribution of predictions across the dataset. The neutral feeling is most prevelent in the dataset by far, accounting for almost half of dataset (48%).


In the lineplot i will not show neutral in the plot, as this can be regarded as a feeling which is not, or is less interesting in terms of analysis, in the calculation of relative frequencies the neutral values are still used.

![Relative Frequencies across seasons](out/LineChart.png?raw=true)

The picture above is the relative frequencies of emotions across seasons.

Across all the seasons anger is the most prevalent emotion (besides neutral) peaking in the last season. Digust declines from season 3 onwards. Joy and Fear performs relatively steadely throughout the seasons in the bottom of the chart.

| Barcharts |  |  |
|---------|---------|---------|
| ![1](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%201.png?raw=true) | ![2](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%202.png?raw=true) | ![3](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%203.png?raw=true) |
| ![4](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%204.png?raw=true) | ![5](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%205.png?raw=true) | ![6](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%206.png?raw=true) |
| ![7](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%207.png?raw=true) | ![8](https://github.com/Revo1999/cds-lang/blob/main/assignment4/out/BarChart_Season%208.png?raw=true) |         |


Throughout the barcharts the prevalence of neutral becomes obvious. This might have to due with the model defaulting the neutral when it cant decide on an emotion, but could also be due to some dialog not having an emotion. The barcharts all look quite similar, with neutral peaking, and anger second and then suprise.

If you have seen Game of Thrones you might be able to contribute certain events in the seasons, that result in the changes from season to season.

This type of analysis might prove itself useful to provide insights to what kind of tv-show Game of Thrones is. It might be interesting to compare these results, to other tv-shows.


## Emissions

*Codecarbon has been used to track the environmental impact of running this code which equates to:* **21.8 of co2-equivalents in grams**

For calculation documentation see [Emissions](https://github.com/Revo1999/cds-lang/tree/main/emissions)

<br><br><br><br>