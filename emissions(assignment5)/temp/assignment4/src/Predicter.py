from codecarbon import EmissionsTracker
tracker = EmissionsTracker(project_name="query_expansion.py", experiment_id="query_expansion.py")

import vrashelper as vh
import polars as pl
import os
import glob
from transformers import pipeline, logging
import tensorflow as tf
import altair as alt
import vegafusion as vf #Altair dont support polars dataframes, vegafusion adds this support, and avoids having to convert polars to pandas for visualization

def load_csv_pl(path_as_list):
    data_file_path = os.path.join(*path_as_list)
    data = pl.read_csv(data_file_path).drop("Release")

    return data


def load_model():
    classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      top_k=1)


    return classifier

def data_for_plotter(data_to_process, index_column, input_column, data, classifier):

    text_to_predict = data.select([input_column]).to_series().to_list() #Select columns index and input

    data_processed = classifier(text_to_predict)

    # Convert classification results to a Polars Series
    predictions_series = pl.Series("Predictions", data_processed)
    
    # Add the predictions as a new column to the DataFrame
    data_done = data.with_columns([predictions_series])

    data_done = data_done.with_columns(
    data_done["Predictions"]
        .map_elements(lambda first_value: list(first_value[0].values())[0])  # Extract the value from the first struct
        .alias("Predictions")
    )



    return data_done
    
def dataprocessor():
    
    data_path = ["..","in", "Game_of_Thrones_Script.csv"]
    data = load_csv_pl(data_path)

    classifier= load_model()

    print("Beginning using classifier")
    data_processed = data_for_plotter(data_to_process=data, index_column="Season", input_column="Sentence", data=data, classifier=classifier)

    data_processed.write_csv("../out/with_predictions.csv", separator=",")

    return data_processed


def visualize_line_chart(data):

    data = data.filter(pl.col("Predictions") != "neutral") #Filter out neutral from plot

    # Base for the plot
    base = alt.Chart(data).encode(
        alt.Color("Predictions").legend(None)
    ).properties(
        width=600,
        height=500
    )

    # Encoding the line, with x = season and y = relative frequency
    line = base.mark_line().encode(
        x=alt.X("Season:N", title="Season"),
        y=alt.Y("Relative_frequency:Q", title="Relative Frequency")
    )

    # Locating last point in the line
    last_point = base.mark_circle().encode(
        x=alt.X("Season:O"),
        y=alt.Y("Relative_frequency:Q")
    ).transform_filter(
        alt.datum.Season == 'Season 8'
    )

    # Emotion name using text marks for labeling the last points
    emotion_name = last_point.mark_text(
        align="left", dx=8
    ).encode(
        text="Predictions"
    )

    
    chart = (line + last_point + emotion_name) # Combining all to one

    return chart


def bar_chart(data_counts):
    chart = alt.Chart(data_counts).mark_bar().encode(
    x='Predictions',
    y='count').properties(
        width=200,
        height=300
    )

    return chart
    

def main():
    vh.work_here() # Can use play button without the need to be in this directory

    tracker.start_task("load and apply model")
    
    
    data = dataprocessor()
    
    tracker.stop_task()
    


    tracker.start_task("calculating on model data")
    season_occur_counts = data['Season'].value_counts().sort(by="Season") #Creates a dataframe with seasons and the counts of all emotions
    season_counts = data.group_by(['Season', 'Predictions']).count().sort(by="Season") #Creates a dataframe with seasons and the counts of each emotion
    combined_season_data = season_occur_counts.join(season_counts, on='Season', how='left') #Joins the dataframes so the columns are Season, Season_count, Predictions, Predictions_counts_for_that_season
    relative_frequencies = combined_season_data.with_columns((pl.col('count_right') / pl.col('count')).alias('Relative_frequency')).select(['Season', 'Predictions', 'Relative_frequency']) #Calculating relative frequency
    value_counts = data["Predictions"].value_counts().sort(by="count")
    tracker.stop_task()

    tracker.start_task("visualize data")
    vf.enable() # Enables vegafusion to convert polars dataframes to altair, otherwise it would copy a polars dataframe turn it into pandas and then give it to altair

    visualize_line_chart(relative_frequencies).save("../out/LineChart.png")
    bar_chart(value_counts).save("../out/BarChart.png")

    

    print(relative_frequencies)
    print(value_counts)
    tracker.stop_task()

if __name__ == "__main__":
    main()

tracker.stop()