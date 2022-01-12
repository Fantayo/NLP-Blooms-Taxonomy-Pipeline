import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Conv1D,LSTM,Bidirectional,Embedding,GlobalMaxPooling1D,Dropout,Flatten,MaxPool1D,MaxPooling1D
from tensorflow.keras.callbacks import ReduceLROnPlateau,EarlyStopping

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

from nltk.stem import PorterStemmer
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

#Importing Tokenizer to break down raw text into tokens with unique IDs :
tokenizer=Tokenizer(num_words=vocab_size,oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)

#For Word Vocab:
word_index=tokenizer.word_index
word_index

len(word_index)


#Coverting The Unique Tokens obatined from tokenizer to Sequences :
train_seq=tokenizer.texts_to_sequences(X_train)
train_padded=pad_sequences(train_seq,maxlen=max_length,padding=padding_type,truncating=trunc_type)

validation_seq=tokenizer.texts_to_sequences(