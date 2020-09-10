
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




data='DEFINE THE DATA PATH HERE'
df=pd.read_csv(data)


#To get the length of max longest string
df.Text.str.len()
df.Text.str.len().max()

vocab_size=10000
embedding_dim=128
max_length=40

# Truncate and padding options
trunc_type = 'post'
padding_type = 'post'