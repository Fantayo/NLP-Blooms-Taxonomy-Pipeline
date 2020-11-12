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
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))
print(word_index)

embedding_dim = 300
max_words = vocab_size              

#Preparing Word Embedding Matrix with GloVe 100-D :
embedding_matrix2 = np.zeros((