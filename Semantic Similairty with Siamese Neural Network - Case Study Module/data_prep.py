import numpy as np
import pandas as pd
import tensorflow as tf

import nltk
import re

nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import tensorflow.keras.backend as K


from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, LSTM,Bidirectional,Concatenate,BatchNormalization
import tensorflow.keras.backend as K
from tensorflow.keras.optimizers import Adadelta,Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import LeakyReLU,Dense,Dropout,Lambda
from tensorflow.keras import metrics

import time

#Link to data :
data_path='/content//data/Quora/train.csv'
data=pd.read_csv(data_path)

#To Get Data Length :
data_length=len(data)

#PREPROCESS THE TEXT
import nltk 
import re 
def process_text(text):
   text = re.