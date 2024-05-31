# Assignment 5: Evaluating environmental impact of your exam portfolio

###### Victor Rasmussen, Language Analytics, Aarhus University 
<br>

This assignment is part of a course at Aarhus University called Language Analytics. Access the Assignment instructions on this [Github page](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment5) 

In this assignment we were asked make to track the emission of Assignment 1-4


## Tracking Tool

I've created a script for tracking projects with CodeCarbon running them in a temparary folder. The tool is made to make Emission tracking easy to use as well as the running automatic, enabling job-queueing.

<u>How to use the script is detailed in usage section</u>


## Overview



|![Relative Frequencies across seasons](out/Assignments_emissions.png?raw=true)| Assignment 4 uses a large pre-trained language model had highest emissions (0.022g) due to the models complexity. <br> Assignments 1-3 involving lighter tasks like linguistic feature extraction, text classification models, and word embeddings had low emissions  all under 0.003g. | 
|-|-|

|emissions (in kg)            |name       |
|----------------------|-----------|
|0.0021603640275246693 |assignment1|
|0.0001479467840897473 |assignment3|
|0.00016542819000933651|assignment2|
|0.021796148513386928  |assignment4|


## Looking at the assignments

Throughout the assignments the tool calculates the total emission of the program, but also enables the user to set certain points in the program and measure the code executed between ```tracker.start_task("TASK NAME")``` & ```tracker.stop_task()```.

The reason for this approach rather than the decorator option [documentation here!](https://mlco2.github.io/codecarbon/examples.html) is due to decorators behaviour around functions called in for-loops. If you use decorator on a function which is called in for-loop it will initiate the tracker (and the hardware check) for every iteration, which results in immense performance issues for no gain relative to measuring the code with one tracking instance.

Throughout the tracking ```tracker.start_task("TASK NAME")``` & ```tracker.stop_task()``` is used in the ```main()``` function of the scripts. For optimal tracking some rewritting of the scripts could be done breaking up parts of the code, which would give better monitization of the programs, I have opted out of this option. The tool also auto inserts a tracker for the whole program. This way the whole program is tracked as well as some individual subtask, which is the comprimise of not rewriting code, as well as having an overall idea about the emissions of the code.


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

Looking into to the data gathered in all of the csv's produced by codecarbon the "on_cloud" column says "N", this leads me to believe that codecarbon does not recognize u-cloud (a cloud platform on which all of the code is ran). Furthermore u-cloud uses a cpu, running on custom Ghz, but u-cloud does also not have the current cpu in their data-base instead they give a constant for their measurements. I imagine that in reality u-cloud's setup is more energy efficient than the average home computing setup, therefore the estimation have the risk of being too high.

Other than that the overall results seem to align well with the amount of time each sections of the programs takes to run.

I would also like to add that codecarbon does not include the computing power of setting up the virtual environment.

## Usage

**<u> The program is written for Python v.3.12.3 & for systems using Bash, other versions or congfigurations might not function or produce unexpected behaviour. </u>**

1. Clone the repository

    ``` sh
    git clone  https://github.com/Revo1999/cds-lang.git
    ```

<br><br>

2. Change the settings in ```prepper.py``` to match your repository the settings is set for the repository analyzed above:

    ``` py
    # The directories for the programs which will be tracked
    directory_to_search = ["../../assignment1","../../assignment2", "../../assignment3", "../../assignment4"]

    # Exclude these folder (input all your Virtual environment folder here)
    exclude_folders = ["assignment1_venv", "assignment2_venv", "assignment3_venv", "assignment4_venv"]

    # The name of the bash file used to setup Virtual environments.
    createVEnv_filename = "createVEnv.sh"

    # The name of the bash files that executes your program
    run_filename = "run.sh"

    # Exclude the tool to edit these with tracker (if py files is in src but does not have any code executed directly within it)
    py_exclude = ["assignment2.py"]
    ```

<br><br>

4. Setup virtual environment containing the packages needed to run both programs. <br>
    ``` sh
    bash createVEnv.sh
    ```

<br><br>

5. Runs ```prepper.py``` by activating the virtual environment, and after the program has ran it will close the environment again.<br>
    ``` sh
    bash run.sh
    ```

 <br><br>

6. The program will copy the py files from the src folders into a the temp folder in the repository (and create the import and overall tracking) and tell you in the console to edit your py-files: Then edit all the py-files in the temp folder and add ```tracker.start_task("TASK NAME")``` & ```tracker.stop_task()``` to the py files, to the sub-task you want to measure.

    **If the files do not show up at this stage be sure to refresh the explorer!**

    ```
    temp/
    ├── assignment1/
    │   └── src/
    │       └── spacy_extract.py
    ├── assignment2/
    │   └── src/
    │       ├── assignment2.py
    │       ├── lr.py
    │       ├── mlp.py
    │       └── vectorize.py
    ├── assignment3/
    │   └── src/
    │       └── query_expansions.py
    └── assignment4/
        └── src/
            └── predicter.py
    ```

<br><br>

7. The program will copy the rest of the directories, the executes the VEnv creation bash files specified in settings, while also adding codecarbon to the installation, afterwards it will run all the py-files(not the excluded ones), it will then collect all emission reports, and copy them into the csv-folder, hereafter it will automatically visualize the data, naming the visualizations after the root folder for each assignment.

<br>
