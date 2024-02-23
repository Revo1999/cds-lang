'''
Assignment 1
    Victor Rasmussen
        Language Analytics, Aarhus University
            23-02-2024
'''

import os                           
import spacy                          
import pandas as pd
from collections import Counter
import warnings    
from tqdm import tqdm
import re


def read_file_to_doc(filepath, meta_data_remove):
    #This function reads .txt, removes anything from text that in between '<' & '>' and applies applies en_core_web_md on text

    #we use latin1 / ISO-8859-1 because the text is encoded with swedish characters
    with open(filepath, encoding='latin1') as f:
        text = f.read()

    #cleaning the text by removing anything between '<' and '>' if meta_data_remove is True
    if meta_data_remove == True:
        cleaned_text = re.sub(r'<[^>]+>', '', text)

    doc = nlp(cleaned_text)

    return doc


def calculate_relative_frequencies(doc, exclude_punctuation):
            pos_counts = []

            for token in doc:
                pos_counts.append(token.pos_)

            #counting words in doc, not counting punctuation if exclude_punctuation is true
            if exclude_punctuation == True:
                num_words = sum(1 for token in doc if not token.is_punct)
            else:
                num_words = sum(1 for token in doc)

            noun_freq = round(pos_counts.count('NOUN')/num_words*10000, 2)
            verb_freq = round(pos_counts.count('VERB')/num_words*10000, 2)
            adj_freq = round(pos_counts.count('ADJ')/num_words*10000, 2)
            adv_freq = round(pos_counts.count('ADV')/num_words*10000, 2)
            
            return noun_freq, verb_freq, adj_freq, adv_freq




def calculate_unique_entities(doc):
   
    ent_per = set()
    ent_loc = set()
    ent_org = set()

     # Person is labeled with Person in spaCy and not per
    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            ent_per.add(str(entity))
        elif entity.label_ == 'LOC':
            ent_loc.add(str(entity))
        elif entity.label_ == 'ORG':
            ent_org.add(str(entity))
        else:
            pass

    return ent_per, ent_loc, ent_org




def processor():
    df = pd.DataFrame()
    
    for folder in os.listdir(directory):
        folderpath = os.path.join(directory, folder)
        
        print(f'processing folder: {folder}')
        
        for file in tqdm(os.listdir(folderpath), colour='green'): #tqdm creates a process bar in console
            filename = file
            filepath = os.path.join(folderpath, filename)

            # Reads file, removes meta data, apply spacy's en_core_web_md
            doc = read_file_to_doc(filepath, meta_data_remove)

            #Calculates relative frequencies
            noun_freq, verb_freq, adj_freq, adv_freq = calculate_relative_frequencies(doc, exclude_punctuation)
           
           #Calculating unique entities
            ent_per, ent_loc, ent_org = calculate_unique_entities(doc)
            
            write_row = pd.DataFrame({'Filename': [filename], 'RelFreq NOUN': [noun_freq], 'RelFreq VERB': [verb_freq], 'RelFreq ADJ': [adj_freq], 'RelFreq ADV': [adv_freq], 'Unique PER': [len(ent_per)], 'Unique LOC':[len(ent_loc)], 'Unique ORG':[len(ent_org)]})
            
            df = pd.concat([df, write_row], ignore_index=True)

        df.to_csv(f"{save_tables_location}/{folder}_table.csv", index=False)
        
if __name__ == "__main__":

    # Simply ingores pandas' py-arrow future warning
    warnings.simplefilter(action='ignore', category=FutureWarning)

    #Loading spaCy en_core_web model into python
    nlp = spacy.load("en_core_web_md")

    #directory is the input folders
    directory = os.path.join('in',
                                'USEcorpus')
    
    #Name of the folder to save output tables in. The code is written so the folder is in the "assignment1" folder. (But can be changed to other locations) Look project structure for guidance.
    save_tables_location = "tables"
    
    #Remove metadata between '<' & '>' from input text-files
    meta_data_remove=True

    #When counting words dont count punctuation
    exclude_punctuation=True

    processor()