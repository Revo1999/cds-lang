#Assignment 1
#Made by: Albin & Victor :))

#  pip install spacy pandas tqdm
#  python -m spacy download en_core_web_md

#Important!!!  change directory to this "assignment1" folder

def main():

    import os
    import spacy
    import pandas as pd
    from collections import Counter
    import warnings
    from tqdm import tqdm
    import re

    warnings.simplefilter(action='ignore', category=FutureWarning)

    nlp = spacy.load("en_core_web_md")

    #directory is the location of the USEcorpus
    directory = os.path.join('in',
                            'USEcorpus')

    for folder in os.listdir(directory):
        folderpath = os.path.join(directory, folder)
        print(f'processing folder: {folder}')
        df = pd.DataFrame()
        for file in tqdm(os.listdir(folderpath)):
            filename = file
            filepath = os.path.join(folderpath, filename)

            #we use latin1 / ISO-8859-1 because the text is encoded with finnish characters
            with open(filepath, encoding='latin1') as f:
                text = f.read()

            #cleaning the text by removing anything between '<' and '>'
            cleaned_text = re.sub(r'<[^>]+>', '', text)

            doc = nlp(cleaned_text)

            pos_counts = []

            for token in doc:
                pos_counts.append(token.pos_)

            #counting words in doc, not counting punctuation
            num_words = sum(1 for token in doc if not token.is_punct)

            noun_freq = round(pos_counts.count('NOUN')/num_words*10000, 2)
            verb_freq = round(pos_counts.count('VERB')/num_words*10000, 2)
            adj_freq = round(pos_counts.count('ADJ')/num_words*10000, 2)
            adv_freq = round(pos_counts.count('ADV')/num_words*10000, 2)

            ent_per = set()
            ent_loc = set()
            ent_org = set()

            #"per" is apparently supposed to be "person" label?
            for entity in doc.ents:
                if entity.label_ == 'PERSON':
                    ent_per.add(str(entity))
                elif entity.label_ == 'LOC':
                    ent_loc.add(str(entity))
                elif entity.label_ == 'ORG':
                    ent_org.add(str(entity))
                else:
                    pass
            
            write_row = pd.DataFrame({'Filename': [filename], 'RelFreq NOUN': [noun_freq], 'RelFreq VERB': [verb_freq], 'RelFreq ADJ': [adj_freq], 'RelFreq ADV': [adv_freq], 'Unique PER': [len(ent_per)], 'Unique LOC':[len(ent_loc)], 'Unique ORG':[len(ent_org)]})

            df = pd.concat([df, write_row], ignore_index=True)

        df.to_csv(f"tables/{folder}_table.csv", index=False)
        
if __name__ == "__main__":
    main()
