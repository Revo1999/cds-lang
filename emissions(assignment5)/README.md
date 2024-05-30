# Assignment 5: Evaluating environmental impact of your exam portfolio

###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment5) 

In this assignment we were asked make two track the emission of Assignment 1-4


## Tracking Tool

I've created a script for tracking projects with CodeCarbon running them in a temparary folder. The tool is made to make Emission tracking easy to use as well as the running automatic, enabling job-queueing.

<u>How to use the script is detailed in usage section</u>




## Overview



|![Relative Frequencies across seasons](out/Assignments_emissions.png?raw=true)| Assignment 4 uses a large pre-trained language model had highest emissions (0.022g) due to the models complexity. <br> Assignments 1-3 involving lighter tasks like linguistic feature extraction, text classification models, and word embeddings had low emissions  all under 0.003g. | 
|-|-|


## Looking at the assignments

Throughout the assignments the tool calculates the total emission of the program, but also enables the user to set certain points in the program and measure the code executed between ```tracker.start_task("TASK NAME")``` & ```tracker.stop_task()```.

The reason for this approach rather than the decorator option [documentation here!](https://mlco2.github.io/codecarbon/examples.html) is due to decorators behaviour around functions called in for-loops. If you use decorator on a function which is called in for-loop it will initiate the tracker for every iteration, which results in immense performance issues for no gain relative to measuring the code with one tracking instance.

Throughout the tracking ```tracker.start_task("TASK NAME")``` & ```tracker.stop_task()``` is used in the ```main()``` function of the scripts. For optimal tracking some rewritting of the scripts could be done breaking up parts of the code, which would give better monitization of the programs, I have opted out of this option.


### Assignment 1

![Relative Frequencies across seasons](out/assignment1_emissions.png?raw=true)

Loading spacy's en_core_web_md does not require much ressources. The model is 40mb, the model comes in three sizes 12, 40, 560 mb. [documentation here](https://spacy.io/models/en) The model is used on the whole dataset, which makes it far more ressource intensive than loading the model, unlike in assignment 3. 

### Assignment 2

![Relative Frequencies across seasons](out/assignment2_emissions.png?raw=true)

As mentioned in the Assignment 2 Readme the performance of MLP and LR are almost identical therefore codecarbon can give valuable insights to performance.

 > 3.7545852661132812(MLP) divided by 0.08067202568054199(LP) ≈ 46.583


*The calculation show that MLP makes 46.5 times more emission. Which roughly translates to requiring 46.5 more computing power (in that specific run).*

Therefore LR is much more efficient to solve the task at classifying fake/real news. The explanation for this is MLP requires a training a neural network, which requires finetuning all the weights, creating a web of information streams, this is computationaly much more requirering than training a logistic regression classifier. 

### Assignment 3

![Relative Frequencies across seasons](out/assignment3_emissions.png?raw=true)

In this assignment loading the model is the most ressource intensive. Unlike the other models this model is only applied to one word (the chosen word), which results in very fast predictions. Then sorting through the csv using Polars, which is a lot faster than Pandas also helps keeping the usage of processing the query down, as well as loading the csv. If Pandas was used the scores might be a little higher, as loading CSV's is typically less ressource intensive than using models, if you were to load images the amount of data is a lot higher and thus requires more ressources.


### Assignment 4

![Relative Frequencies across seasons](out/assignment4_emissions.png?raw=true)

In assignment 4 loading and applying the model uses by far the most ressources. When the program is run loading the model goes quite fast (under 30 seconds) but applying the model on all the lines in the script. While applying the model took 35.5 minutes (2134 seconds), the two other task both took under 1 sec to complete for reference, this data comes from assignment4.csv in the out folder of this repository.

The model is predicting +23,000 lines which is a lot of predictions to be made, this explains the ressource intensiveness.


## Is code-carbon tracking reliable?

the cloud setting is F





## Usage




So why go through all the trouble of setting up a copy system, instead of using makedirs for all the files and then using shutil's copytree? Because it does not tell you anything in the console. By setting it up myself i can be sure it works exactly as I wish, but also i can add tqdm progress bar.