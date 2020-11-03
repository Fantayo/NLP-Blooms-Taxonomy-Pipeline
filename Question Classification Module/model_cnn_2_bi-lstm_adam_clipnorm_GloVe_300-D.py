import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Conv1D,LSTM,Bidirectional,Embedding,GlobalMaxPooling1D,Dropout,Flatten,MaxPool1D,MaxPooling1D
from tensorflow.keras.callbacks import EarlyStopping


vocab_size=10000
embedding_dim=128
max_length=40

path='PATH TO GLOVE EMBEDDINGS'
#Using Word Embeddings :
word_index = tokenizer.word_index
glove_dir = 'path/Glove Embeddings/glove.6B.300d.txt'
embeddings_index = {}


f = open('path/Glove Embeddings/glove.6B.300d.txt')
for line in f:
    values = line.split