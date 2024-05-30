from codecarbon import EmissionsTracker
tracker = EmissionsTracker(project_name="query_expansion.py", experiment_id="query_expansion.py")

import vrashelper as vh
import polars as pl
import os
import gensim.downloader as api
import argparse

def load_glove_wiki_gigaword50():
    #From my understanding it downloads in a specific place, when downloaded it will not download again.
    print('loading gensim pretrained model: glove-wiki-gigaword-50')
    return api.load("glove-wiki-gigaword-50")
    print(vh.colorbank.hackergreen + 'model loaded' + vh.colorbank.default)

def load_spotify_csv():
    data_file_path = os.path.join('..', 'in', 'Spotify Million Song Dataset_exported.csv')

    #Loads csv and drops link column, as this will not be used
    data = pl.read_csv(data_file_path).drop("link")

    #Fixing a mistake in the data set
    data = data.with_columns(artist=pl.col("artist").replace("'n Sync", "N Sync"))

    return data


def input_check(input):
    if input.lower() in data['artist'].str.lower().to_list():
        return True
    else:
        print('Artist is not in dataset')
        return False



def create_search_words(word_input, model, words_result_amount):
    model_words = model.most_similar(word_input.lower(), topn=words_result_amount)
    output_words = []

    # Extend instead of append
    output_words.extend(model_words)

    concat_words = ""

    for words, _ in output_words:
        # Use 'words' directly instead of indexing 'output_words'
        concat_words = concat_words + "|" + words

    return word_input.lower() + concat_words

def processor(word, model, data, words_result_amount, artist, extended_info):
    concated_search = create_search_words(word_input=word, model=model, words_result_amount=words_result_amount)

    if extended_info == True:
        print(f"Your extended search is: {concated_search}")


    compare = result = data.filter(
        #Must be correct otherwise ABBA would also return Black S-ABBA-th
        (data['artist'].str.to_lowercase() == artist.lower()))

    result = data.filter(
        #Must be correct otherwise ABBA would also return Black S-ABBA-th
        (data['artist'].str.to_lowercase() == artist.lower()) &
        #Looks all the text to see if it contains. Might result in false positives ('lovesick' contains 'love')
        (data['text'].str.to_lowercase().str.contains(concated_search.lower()))
    )

    procentage_hit, artist_cased, searched_word = round(result.shape[0]/compare.shape[0]*100, 1), result[0,0], word.lower()

    #Prints answer to console
    print(vh.ctext.bold + f"{procentage_hit}% of {artist_cased}'s songs contain words related to {searched_word}" + vh.colorbank.default)

def argument_collection():

        parser = argparse.ArgumentParser()
   
        parser.add_argument(
            "-m",
            "--model_words_amount",
            default=3,
            help="How many words most similar supplies")

        parser.add_argument(
            "-a",
            "--artist",
            default="pHiL CoLlins",
            help="Name of the artist")

        parser.add_argument(
            "-w",
            "--word",
            default="AiR",
            help="The word you're searching for")

        parser.add_argument(
            "-e",
            "--extended_search",
            default=False,
            help="Provides a printed list of the most similar words that extend your search")
        
        return parser.parse_args()

def main():
    # Gets parsed args
    words_result_amount = int(argument_collection().model_words_amount)
    artist = argument_collection().artist
    word = argument_collection().word
    extended_info = argument_collection().extended_search

    tracker.start_task("load model")
    # Loads model and data
    model = load_glove_wiki_gigaword50()
    tracker.stop_task()

    tracker.start_task("load spotify csv")
    data = load_spotify_csv()
    tracker.stop_task()

    tracker.start_task("Process Query")
    # Applies logic
    processor(word=word, model=model, data=data, words_result_amount=words_result_amount, artist=artist, extended_info=extended_info)
    tracker.stop_task()

if __name__ == "__main__":
    main()




tracker.stop()