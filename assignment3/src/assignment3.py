import pandas as pd
import os
from helperfunctions import work_here, colorbank
import gensim.downloader as api


print('downloading & loading gensim pretrained model: glove-wiki-gigaword-50')
model = api.load("glove-wiki-gigaword-50")
print(colorbank.hackergreen + 'model loaded' + colorbank.default)


work_here()

data_file_path = os.path.join('..', 'in', 'Spotify Million Song Dataset_exported.csv')

data = pd.read_csv(data_file_path)

target_word = "night"

print(model.most_similar(target_word, topn=3))