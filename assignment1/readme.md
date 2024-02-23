# Assignment 1 
###### Victor Rasmussen, Langauge Analytics, Aarhus University
-----

This project include a assignment1.py files that go through txt and extracts: relative frequency of nouns, verbs, adjective, and adverbs per 10,000 words, aswell as total number of unique PER, LOC, ORGS per text, using spaCy.

More information and download link for data (Beware of terms of usage!): [click here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457)

#### Project Structure

>Assignment 1/
├── in/
│   └── USEcorpus/
│       ├── a1
│       ├── a2
│       ├── a3
│       └── and so on
├── tables
├── src/
│   └── assignment1.py
├── readme.md
├── requirements.txt
└── start.sh

#### Dependencies

Either use ```./start.sh``` or type ```python -m spacy download en_core_web_md``` &
```pip install spacy pandas tqdm``` in console

<br>
<br>

#### Usage
Insert data from USEcorpus to match what is shown i project structure or change the value of ```directory``` (shown below) if you follow forementioned structure also "cd" into the "Assignment 1"-folder **to avoid path problems.**


1. run ```./start.sh``` in console and accept
2. run ```python src\assignment1.py```

<br>
<br>

### These settings can be changed in  ```main()```:


Change the input path: 
```directory = os.path.join('..','in','USEcorpus')```

Change the output path:
 ```save_tables_location = os.path.join('..','tables') ```

Remove metadata from .txt-files, its removing anything between '<' &'>' :```meta_data_remove=True```

When counting words for relative frequency, disregard punctuation: ```exclude_punctuation=True```

Total frequency, used to calculate relative frequency: ```relative_frequency_count = 10000```