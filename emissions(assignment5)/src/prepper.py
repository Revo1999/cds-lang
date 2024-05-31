'''
Assignment 5
    Victor Rasmussen
        Language Analytics, Aarhus University
            31-05-2024
'''

import os
import vrashelper as vh
import tqdm
import shutil
import time
from subprocess import call
import glob
import polars as pl
import altair as alt
import vegafusion as vf


def list_files(directory, exclude_subfolders=None):
    # If theres is no folder to exclude make list empty
    if exclude_subfolders is None:
        exclude_subfolders = []

    # Get every value in list
    exclude_subfolders = [os.path.abspath(os.path.join(directory, subfolder)) for subfolder in exclude_subfolders]

    file_paths = []
    

    for root, dirs, files in os.walk(directory):
        # Remove subfolders that should be excluded
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) not in exclude_subfolders]
        
        # Creates file paths for the directory
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            file_paths.append(relative_path)
    
    return file_paths

def create_from_list(directory_to_search, files):
    
    filepaths = files
    
    from_list = []

    for path in filepaths:
        from_list.append(os.path.join(directory_to_search, path))

    return  from_list

def create_to_list(directory_to_place, files):
    
    filepaths = files
    
    to_list = []

    for path in filepaths:
        to_list.append(os.path.join(directory_to_place, path))

    return  to_list

def make_a_folder_req_list(files):

    dir_list = []

    # Makes list of the directories
    for filepaths in files:
        dir_list.append(os.path.dirname(filepaths))
    
    # Removes duplicates
    dir_to_create = list(set(dir_list))

    return dir_to_create

def make_folders(files):
    # List directories
    mkdir_list = make_a_folder_req_list(files)

    # Creates the folders needed
    for paths in mkdir_list:
        os.makedirs(paths, exist_ok=True)

def copy_project_folder(directory_to_copy, subfolders_to_exclude):


    if os.path.exists(directory_to_copy):
        destination_directory = os.path.join("..", "temp", os.path.split(directory_to_copy)[-1])
        
        file_list = list_files(directory_to_copy, subfolders_to_exclude)

        from_list = create_from_list(directory_to_copy, file_list)

        to_list = create_to_list(destination_directory, files=file_list)

        # Destination folders created
        make_folders(to_list)

        # Copies all from the from_list, to their new destination which is listed in the to_list
        for i in tqdm.tqdm(range(len(from_list)), desc=f"Copying: {os.path.split(directory_to_copy)[-1]}", colour="green"):
                if not os.path.exists(to_list[i]):
                    shutil.copy(from_list[i], to_list[i])
                else:
                    print(f"File {to_list[i]} already exists and will not be overwritten. (Is expected for py-files in src)")
    # If error occur
    else:
        print(vh.colorbank.error_red + f"The folder you are trying to copy does not exist. {directory_to_copy}. If the filepath looks right be sure that you are running this through run.sh or that you changed directory into src folder" + vh.colorbank.default)
        quit()

def run_venv_scripts(venv_filename, directory):
    

    # Just give a little time to see what the program is going to do next
    print((vh.colorbank.hackergreen + "Now executing all Virtual environment files" + vh.colorbank.default + vh.ctext.nline)*10) 
    time.sleep(2)
    
    
    file_list = list_files(directory)
    run_list = []

    # Finds all files to be run
    for file in file_list:
        if os.path.split(file)[-1] == venv_filename:
            run_list.append(file)

    # Reads sh file
    for script in run_list:

        full_file = os.path.join("..", "temp", script)

        # Reads sh file
        with open(full_file, 'r') as file:
            sh_content = file.read()

        # Adds a pip install codecarbon line
        new_sh = sh_content.replace("pip install -r requirements.txt", "pip install -r requirements.txt\n\npip install codecarbon==2.4.2 setuptools==70.0.0")

        # Saves modifications
        with open(full_file, 'w') as file:
            file.write(new_sh)
    
    # This directory
    this_directory = os.getcwd()

    for file in run_list:
        file_to_call = os.path.join("..", "temp", file)

        # This directory
        script_directory = os.path.dirname(file_to_call)

        # Changes dir to "this directory" 
        os.chdir(script_directory)
        
        # Adds execute permission if not already set
        os.chmod(os.path.split(file_to_call)[-1], 0o755)
        
        # Executes the script with its full path
        call(str("bash " + os.path.split(file_to_call)[-1]), shell=True)
        
        # Reverts back to the original directory
        os.chdir(this_directory)

def copy_py_files(directory_to_copy):

    if os.path.exists(directory_to_copy):
        destination_directory = os.path.join("..", "temp", os.path.split(directory_to_copy)[-1])
        
        file_list = list_files(directory_to_copy)

        # Sort for src files
        src_list = []

        # Only copy the files in src folder ending with .py
        for filepath in file_list:
            if filepath.startswith("src") and filepath.endswith(".py"):
                src_list.append(filepath)

        from_list = create_from_list(directory_to_copy, src_list)

        to_list = create_to_list(destination_directory, files=src_list)

        # Destination folders created
        make_folders(to_list)

        # Copies
        for i in tqdm.tqdm(range(len(from_list)), desc=f"Copying: {os.path.split(directory_to_copy)[-1]}", colour="green"):
            shutil.copy(from_list[i], to_list[i])
    
    else:
        print(vh.colorbank.error_red + f"The folder you are trying to copy does not exist. {directory_to_copy}. If the filepath looks right be sure that you are running this through run.sh or that you changed directory into src folder" + vh.colorbank.default)
        quit()

def read_py_file(file_path):
    with open(file_path, 'r') as file:
        py_file_content = file.read()
    return py_file_content

def py_editor(py_path):

    import_lines = "from codecarbon import EmissionsTracker\n"

    tracker_lines = f'tracker = EmissionsTracker(project_name="{os.path.split(py_path)[-1]}", experiment_id="{os.path.split(py_path)[-1]}")\n\n'
    content = (read_py_file(py_path))
    last_line = "\n\n\ntracker.stop()"

    new_py_file = import_lines + tracker_lines + content + last_line

    # Writes the modified py-file
    with open(py_path, 'w') as file:
        file.write(new_py_file)

def press_anything_to_continue():
    # Press enter to continue having an input which is never used anywhere
    print('\n\ngo to temp folder an add tracker.start_task("TASK NAME") and tracker.stop_task() to all assignment in python code\nPress enter to continue...')
    user_input = input()

def run_run_scripts(run_filename, directory):
    

    # Just give a little time to see what the program is going to do next
    print((vh.colorbank.hackergreen + "Now running all py scripts" + vh.colorbank.default + vh.ctext.nline)*10) 
    time.sleep(2)
    
    
    file_list = list_files(directory)
    run_list = []

    # Finds all files to be run
    for file in file_list:
        if os.path.split(file)[-1] == run_filename:
            run_list.append(file)

    # Reads sh file
    for script in run_list:

        full_file = os.path.join("..", "temp", script)
    
    # This directory
    this_directory = os.getcwd()

    for file in run_list:
        file_to_call = os.path.join("..", "temp", file)

        script_directory = os.path.dirname(file_to_call)

        os.chdir(script_directory)
        
        # Adds execute permission if not already set
        os.chmod(os.path.split(file_to_call)[-1], 0o755)
        
        # Executes the script with its full path
        call(str("bash " + os.path.split(file_to_call)[-1]), shell=True)
        
        # Reverts back to the original directory
        os.chdir(this_directory)

def copy_emission_csv(directory, to_directory):
        
        file_list = list_files(directory)
        
        # Sorts for src files
        csv_list = []
        
        # if in src folders and end with csv (which is the emissions files)
        for filepath in file_list:
            if os.path.normpath(filepath).split(os.sep)[1] == "src" and filepath.endswith(".csv"):
                csv_list.append(filepath)

        from_list = create_from_list(directory, csv_list)

        new_csv_list = []
        for paths in csv_list:
            new_csv_list.append(os.path.normpath(paths).split(os.sep)[-1])
        
        
        to_list = create_to_list(to_directory, files=new_csv_list)
        
        # Copy selected files - from from_list to to_list
        for i in tqdm.tqdm(range(len(from_list)), desc="Copying Emission CSV's", colour="green"):
            directory, filename = os.path.split(to_list[i])
            new_filename = f"{os.path.join(directory, str(os.path.normpath(from_list[i]).split(os.sep)[-3]) + filename)}" # If filenames are the same i add the index to the filename
            shutil.copy(from_list[i],  new_filename)


def read_csv_with_filename(file_path):
    
    # Reads csv
    data = pl.read_csv(file_path)
    
    # Assign filename
    filename = os.path.basename(file_path)
    
    # Adds filename column
    data = data.with_columns(pl.lit(filename).alias("filename"))
    return data

def load_emissions(emission_folder):
    
    full_program_emissions = []
    task_emissions = []
    

    # Use string length to determine whether its a emission base csv or normal emission csv
    for csv_file in glob.glob(emission_folder):
        if csv_file.endswith("emissions.csv"):
            full_program_emissions.append(csv_file)
        else:
            task_emissions.append(csv_file)


    full_program_emissions_read = [read_csv_with_filename(csv_file) for csv_file in full_program_emissions]

    task_emissions_read = [read_csv_with_filename(csv_file) for csv_file in task_emissions]


    # Combines the csv's into one for each category
    full_program_emissions_all = pl.concat(full_program_emissions_read)
    task_emissions_all = pl.concat(task_emissions_read)

    return full_program_emissions_all, task_emissions_all

def bar_chart(data, x_name, y_name, graph_title):

    x_values = str(x_name) + ":N"
    y_values = str(y_name) + ":Q"
    g_title = str(graph_title)

    chart = alt.Chart(data).mark_bar().encode(
    x=x_values,
    y=y_values
    ).properties(
    title=g_title, width=300, height=300
    )

    # From: https://altair-viz.github.io/gallery/simple_bar_chart.html 
    return chart

def visualize_emissions():
    vf.enable()

    # Get csv's loaded
    full_program_emissions_all, task_emissions_all = load_emissions(os.path.join("..", "csv", "*"))

    bar_chart(data = full_program_emissions_all, x_name="project_name", y_name="emissions", graph_title="Py files Emissions").save(os.path.join("..", "out", "Emissions2.png"))

    unique_reports = full_program_emissions_all['filename'].unique().to_list()

    # Create report with all programs full emissions
    full_program_emissions = []
    for reports in unique_reports:
        visualize_this_df = full_program_emissions_all.filter(pl.col("filename") == reports)
        visualize_this_df = visualize_this_df.select(pl.sum("emissions"))
        visualize_this_df = visualize_this_df.with_columns(pl.lit(reports.replace("emissions.csv", "")).alias("name"))
        full_program_emissions.append(visualize_this_df)
    
    full_program_emissions_done = pl.concat(full_program_emissions)
    full_program_emissions_done.write_csv(os.path.join("..", "out", "Full_program_emissions.csv")) # Write the csv
    
    # Visualize beforementioned csv
    bar_chart(data = full_program_emissions_done, x_name="name", y_name="emissions", graph_title="Assignment Emissions").save(os.path.join("..", "out", "Assignments_emissions.png"))

    assignment_emissions = []

    # Visualize tasks for every report name
    for directory in directory_to_search:
        try:
             part_to_match = os.path.normpath(directory).split(os.sep)[-1]
             visualize_this_df = task_emissions_all.filter(pl.col("filename").str.contains(part_to_match))
             bar_chart(data = visualize_this_df, x_name="task_name", y_name="emissions", graph_title=f"{part_to_match}").save(os.path.join("..", "out", f"{part_to_match}_emissions.png"))
             visualize_this_df.write_csv(os.path.join("..", "out", f"{part_to_match}.csv"))
        except:
            print("No match in csv")










# SETTINGS!

vh.work_here()

directory_to_search = ["../../assignment1","../../assignment2", "../../assignment3", "../../assignment4"]
exclude_folders = ["assignment1_venv", "assignment2_venv", "assignment3_venv", "assignment4_venv"]
createVEnv_filename = "createVEnv.sh"

run_filename = "run.sh"
py_exclude = ["assignment2.py"]


# Runs all the stuff

# Copies python files from /src in assignment folders

for directory in directory_to_search:
    copy_py_files(directory)


for root, dirs, files in os.walk(os.path.join("..", "temp")):
    if 'src' in dirs:
        src_folder = os.path.join(root, 'src')

        py_files = glob.glob(os.path.join(src_folder, '*.py'))
        print(py_files)

        for py_file in py_files:
            if os.path.normpath(py_file).split(os.sep)[-1] not in py_exclude:
                py_editor(py_file)

# Press enter to continue gives the user time to edit their py files
press_anything_to_continue()

# Copies the rest
for directory in directory_to_search:
    copy_project_folder(directory, subfolders_to_exclude=exclude_folders)

# Runs all venv files, adding codecarbon, works across all directories in "temp" therefore this file must have the same name in all directories
run_venv_scripts(directory=os.path.join("..", "temp"), venv_filename=createVEnv_filename)
run_run_scripts(directory=os.path.join("..", "temp"), run_filename=run_filename)

# Copies emissions csv from temp folder to csv-folder
copy_emission_csv(directory=os.path.join("..", "temp"), to_directory=os.path.join("..", "csv"))

# Visualizes the csv's
visualize_emissions()