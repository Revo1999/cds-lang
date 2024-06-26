'''
Assignment 2
    Victor Rasmussen
        Language Analytics, Aarhus University
            31-05-2024
'''
from assignment2 import tfidf_vect #Imports tfidf_vect function from assignment2.py
import vrashelper as vh #Imports the package i've made for setting working directory automatically and enabling certain console text properties
import os
import argparse

def argument_collection():

        parser = argparse.ArgumentParser()
   
        parser.add_argument(
            "-X",
            "--X_name",
            default="text",
            help="Name of the X value columns in dataset")

        parser.add_argument(
            "-y",
            "--y_name",
            default="label",
            help="Name of the y value columns in dataset")

        parser.add_argument(
            "-t",
            "--training_test_split",
            default=80,
            help="Decides the split, default value is 80, meaning a split of 80/20")

        parser.add_argument(
            "-s",
            "--shuffle_seed",
            default=42,
            help="Functions like seed does in perlin noise, the number corresponds to a specific shuffle in this sense.")

        parser.add_argument(
                "-o",
                "--overwrite_save_path",
                default=os.path.join('..', 'models', 'tfidf_vectorizor' + '.joblib'),
                help="overwrite full save path for model. Needs to be a string and end with .joblib   Example: ../models/tfidf_vectorizor.joblib")

        parser.add_argument(
                "-d",
                "--data_input_path",
                default=os.path.join(  '..', 'in', 'fake_or_real_news.csv' ),
                help="input path for csv-file to be vectorized. Example: ../in/fake_or_real_news.csv")
        
        parser.add_argument(
                "-f",
                "--file_path_save_fitted_data",
                default='../fitted_data/fitted_variables',
                help="changes directory of saving fitted data (must be a string!). Example: '../fitted_data/fitted_variables'")

        
        return parser.parse_args()


def main():

    #Set working directory to this .py file (then no need to cd into python file when pressing the "play button" in Visual Studio gui):
    vh.work_here()

    tfidf_vect( X_name = argument_collection().X_name,
                    y_name = argument_collection().y_name,
                    save_model_path = argument_collection().overwrite_save_path,
                    training_split_value_percent = argument_collection().training_test_split,
                    shuffle_seed = argument_collection().shuffle_seed,
                    data_file_path = argument_collection().data_input_path,
                    file_path_save_fitted_data = argument_collection().file_path_save_fitted_data)


if __name__ == "__main__":
    main()