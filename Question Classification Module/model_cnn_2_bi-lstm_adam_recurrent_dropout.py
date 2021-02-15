import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Conv1D,LSTM,Bidirectional,Embedding,GlobalMaxPooling1D,Dropout,Flatten,MaxPool1D,MaxPooling1D
from tensorflow.keras.callbacks import EarlyStopping


vocab_size=10000
embedding_dim=128
max_length=40

tf.keras.backend.clear_session()
model=Sequential()
model.add(Embedding(vocab_size,256,input_length=train_padded.shape[1]))

model.add(Conv1D(256,3,activation='relu',padding='valid'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.1))

model.add(Bidirectional(LSTM(256,return_sequences=True)))
model.add(Bidirectional(LSTM(128,recurrent_dropout=0.1)))
model.add(Dropout(0.1))
model.add(Fl