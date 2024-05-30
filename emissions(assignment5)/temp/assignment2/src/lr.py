from codecarbon import EmissionsTracker
tracker = EmissionsTracker(project_name="lr.py", experiment_id="lr.py")

import vrashelper as vh
from assignment2 import lr
import argparse
import os

def argument_collection():

        parser = argparse.ArgumentParser()
   
        parser.add_argument(
            "-m",
            "--model_path",
            default=os.path.join('..','models','tfidf_vectorizor.joblib'),
            help="file path to obtain model .joblib file. (must be string) Example '../models/tfidf_vectorizor.joblib'")

        parser.add_argument(
            "-i",
            "--input_path",
            default=os.path.join('..','fitted_data','fitted_variables'),
            help="file path to obtain fitted data (must be string) Example '../fitted_data/fitted_variables'")

            
        parser.add_argument(
            "-o",
            "--out_path",
            default=os.path.join('..','out','lr_classifier_metrics.txt'),
            help="file path to save lr-classifier metrics (must be string and end with .txt) Example '../out/lr_classifier_metrics.txt'")

        parser.add_argument(
            "-s",
            "--shuffle_seed",
            default=42,
            help="Functions like seed does in perlin noise, the number corresponds to a specific shuffle in this sense.")

        parser.add_argument(
            "-d",
            "--dump_model_path",
            default='../models/lr_classifier_model.joblib',
            help="file path to save lr-classifier model (must be string and end with .joblib) Example '../models/lr_classifier_model.joblib")

        
        return parser.parse_args()




def main():
    
    vh.work_here()
    tracker.start_task("applying lr")
    lr( argument_collection().model_path,
        argument_collection().input_path,
        argument_collection().out_path,
        argument_collection().shuffle_seed,
        argument_collection().dump_model_path)
    tracker.stop_task()
if __name__ == "__main__":
    main()


tracker.stop()