'''
Assignment 5 code
'''

import os
import vrashelper as vh
import tqdm
import shutil
import time
from subprocess import call
import ast
import glob

def list_files(directory, exclude_subfolders=None):
    if exclude_subfolders is None:
        exclude_subfolders = []

    exclude_subfolders = [os.path.abspath(os.path.join(directory, subfolder)) for subfolder in exclude_subfolders]

    file_paths = []
    
    for root, dirs, files in os.walk(directory):
        # Remove subfolders that should be excluded
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) not in exclude_subfolders]
        
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
    mkdir_list = make_a_folder_req_list(files)

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

        for i in tqdm.tqdm(range(len(from_list)), desc=f"Copying: {os.path.split(directory_to_copy)[-1]}", colour="green"):
                if not os.path.exists(to_list[i]):
                    shutil.copy(from_list[i], to_list[i])
                else:
                    print(f"File {to_list[i]} already exists and will not be overwritten. (Is expected for py-files in src)")
    
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
        new_sh = sh_content.replace("pip install -r requirements.txt", "pip install -r requirements.txt\n\npip install codecarbon==2.4.2")

        # Saves modifications
        with open(full_file, 'w') as file:
            file.write(new_sh)
    
    # This directory
    this_directory = os.getcwd()

    for file in run_list:
        file_to_call = os.path.join("..", "temp", file)

        script_directory = os.path.dirname(file_to_call)

        os.chdir(script_directory)
        
        # Add execute permission if not already set
        os.chmod(os.path.split(file_to_call)[-1], 0o755)
        
        # Execute the script with its full path
        call(str("bash " + os.path.split(file_to_call)[-1]), shell=True)
        
        # Revert back to the original directory
        os.chdir(this_directory)

def copy_py_files(directory_to_copy):

    if os.path.exists(directory_to_copy):
        destination_directory = os.path.join("..", "temp", os.path.split(directory_to_copy)[-1])
        
        file_list = list_files(directory_to_copy)

        # Sort for src files
        src_list = []

        for filepath in file_list:
            if filepath.startswith("src") and filepath.endswith(".py"):
                src_list.append(filepath)

        from_list = create_from_list(directory_to_copy, src_list)

        to_list = create_to_list(destination_directory, files=src_list)

        # Destination folders created
        make_folders(to_list)

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

    with open(py_path, 'w') as file:
        file.write(new_py_file)

def press_anything_to_continue():

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
        
        # Add execute permission if not already set
        os.chmod(os.path.split(file_to_call)[-1], 0o755)
        
        # Execute the script with its full path
        call(str("bash " + os.path.split(file_to_call)[-1]), shell=True)
        
        # Revert back to the original directory
        os.chdir(this_directory)

def copy_emission_csv(directory, to_directory):
        
        file_list = list_files(directory)
        
        # Sort for src files
        csv_list = []
        
        for filepath in file_list:
            if os.path.normpath(filepath).split(os.sep)[1] == "src" and filepath.endswith(".csv"):
                csv_list.append(filepath)

        from_list = create_from_list(directory, csv_list)

        new_csv_list = []
        for paths in csv_list:
            new_csv_list.append(os.path.normpath(paths).split(os.sep)[-1])
        
        print(new_csv_list)
        to_list = create_to_list(to_directory, files=new_csv_list)
        
        print(csv_list)
        for i in tqdm.tqdm(range(len(from_list)), desc=f"Copying: {os.path.split(directory)[-1]}", colour="green"):
            shutil.copy(from_list[i], to_list[i])


    

vh.work_here()

directory_to_search = ["../../assignment1"]
#directory_to_search = ["../../assignment1","../../assignment2"]
exclude_folders = ["assignment1_venv", "assignment2_venv", "assignment3_venv", "assignment4_venv"]
createVEnv_filename = "createVEnv.sh"
run_filename = "run.sh"

# Copies python files from /src in assignment folders

for directory in directory_to_search:
    copy_py_files(directory)


for root, dirs, files in os.walk(os.path.join("..", "temp")):
    if 'src' in dirs:
        src_folder = os.path.join(root, 'src')

        py_files = glob.glob(os.path.join(src_folder, '*.py'))
        print(py_files)

        for py_file in py_files:
            py_editor(py_file)

press_anything_to_continue()

for directory in directory_to_search:
    copy_project_folder(directory, subfolders_to_exclude=exclude_folders)

# Runs all venv files, adding codecarbon, works across all directories in "temp" therefore this file must have the same name in all directories
run_venv_scripts(directory=os.path.join("..", "temp"), venv_filename=createVEnv_filename)
run_run_scripts(directory=os.path.join("..", "temp"), run_filename=run_filename)

copy_emission_csv(directory=os.path.join("..", "temp"), to_directory=os.path.join("..", "csv"))


# Visualization







'''
copy_project_folder(directory_to_search, exclude_folders)

# Runs all venv files
run_venv_scripts(directory=os.path.join("..", "temp"), venv_filename=createVEnv_filename)
'''

'''
def create_function_list(py_file_path):

    contents = read_py_file(py_file_path)

    parsed_py_file = ast.parse(contents)

    # Creates empty variable
    main_function_node = None

    for node in parsed_py_file.body:
        if isinstance(node, ast.FunctionDef):
            if node.name == 'main':
                main_function_node = node
                break



    # Thanks to: https://stackoverflow.com/questions/37217823/how-to-find-detect-if-a-build-in-function-is-used-in-python-ast 
    # Also check "ast" documentation: https://docs.python.org/3.8/library/ast.html#abstract-grammar to see different things ast can search in python file for (here it checks for functions)

    # Extracts the content of the main function
    if main_function_node:
        main_function_code = ast.unparse(main_function_node)  # Unparse the code to text again
    else:
        print("No main function found.")

    return main_function_code

'''    



