import numpy as np


#Imp PARAMS :
maxsentence_length=sentence_length
embedding_dim=100
max_num_words=50000
hiddendim=128   



word_index = tokenizer.word_index
glove_dir = 'path/Glove Embeddings/glove.6B.100d.txt'
embeddings_index = {}


f = open('/path/Glove Embeddings/glove.6B.100d.txt')
for line in f:
    values = line.s