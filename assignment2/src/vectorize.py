from helperfunctions import work_here
from assignment2 import tfidf_vect

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
                default=os.path.join('..', 'model', 'tfidf_vectorizor' + '.joblib'),
                help="overwrite full save path for model. Needs to be a string and end with .joblib   Example: ../model/tfidf_vectorizor.joblib")

        parser.add_argument(
                "-d",
                "--data_input_path",
                default=os.path.join(  '..', 'in', 'fake_or_real_news.csv' ),
                help="input path for csv-file to be vectorized. Example: ../in/fake_or_real_news.csv")
        
        
        return parser.parse_args()


def main():

    #Set working directory to this .py file (then no need to cd into python file when pressing the "play button" in Visual Studio gui):
    work_here()

    tfidf_vect( X_name = argument_collection().X_name,
                    y_name = argument_collection().y_name,
                    save_model_path = argument_collection().overwrite_save_path,
                    training_split_value_percent = argument_collection().training_test_split,
                    shuffle_seed = argument_collection().shuffle_seed,
                    data_file_path = argument_collection().data_input_path)


if __name__ == "__main__":
    main()

