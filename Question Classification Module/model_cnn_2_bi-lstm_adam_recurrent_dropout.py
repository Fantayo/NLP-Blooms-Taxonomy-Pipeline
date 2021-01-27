import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Conv1D,LSTM,Bidirectional,Embedding,GlobalMaxPooling1D,Dropout,Flatten,MaxPool1D,MaxPooling1D
from tensorflow.keras.callbacks import EarlyStopping


vocab_size=10000
embedding_dim=128
max_length=40

tf.keras.backend.clear_session()
model=Sequential()
m