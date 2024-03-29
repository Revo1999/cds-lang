from helperfunctions import work_here
from assignment2 import mlp

import argparse
import os

def argument_collection():

        parser = argparse.ArgumentParser()
   
        parser.add_argument(
            "-m",
            "--model_path",
            default=os.path.join('..','model','tfidf_vectorizor.joblib'),
            help="file path to obtain model .joblib file. (must be string) Example '../model/tfidf_vectorizor.joblib'")

        parser.add_argument(
            "-i",
            "--input_path",
            default=os.path.join('..','fitted_data','fitted_variables'),
            help="file path to obtain fitted data (must be string) Example '../fitted_data/fitted_variables'")

            
        parser.add_argument(
            "-o",
            "--out_path",
            default=os.path.join('..','out','mlp_classifier_metrics.txt'),
            help="file path to save lr-classifier metrics (must be string and end with .txt) Example '../out/mlp_classifier_metrics.txt'")

        parser.add_argument(
            "-s",
            "--shuffle_seed",
            default=42,
            help="Functions like seed does in perlin noise, the number corresponds to a specific shuffle in this sense.")

        parser.add_argument(
            "-d",
            "--dump_model_path",
            default='../model/mlp_classifier_model.joblib',
            help="file path to save lr-classifier model (must be string and end with .joblib) Example '../model/mlp_classifier_model.joblib")


        parser.add_argument(
            "-mi",
            "--max_iterations",
            default=500,
            help="max iterations parameter for MLP")

        parser.add_argument(
            "-hl",
            "--hidden_layers",
            default=15,
            help="max iterations parameter for MLP")

        return parser.parse_args()




def main():
    
    work_here()
    
    mlp(argument_collection().model_path,
        argument_collection().input_path,
        argument_collection().out_path,
        argument_collection().shuffle_seed,
        argument_collection().dump_model_path,
        argument_collection().hidden_layers,
        argument_collection().max_iterations)

if __name__ == "__main__":
    main()