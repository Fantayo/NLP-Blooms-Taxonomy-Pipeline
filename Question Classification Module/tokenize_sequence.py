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

f