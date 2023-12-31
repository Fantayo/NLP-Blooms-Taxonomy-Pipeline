
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
glove_dir = 'path/Glove Embeddings/glove.6B.100d.txt'
embeddings_index = {}


f = open('path/Glove Embeddings/glove.6B.100d.txt')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))
print(word_index)

embedding_dim = 100
max_words = vocab_size              

#Preparing Word Embedding Matrix with GloVe 100-D :
embedding_matrix = np.zeros((max_words, embedding_dim))

for word, i in word_index.items():
  if i < max_words:

    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector


tf.keras.backend.clear_session()
optim=tf.keras.optimizers.Adam(clipnorm=1.25)
model=Sequential()
model.add(Embedding(vocab_size,100,weights=[embedding_matrix],input_length=train_padded.shape[1]))

model.add(Conv1D(256,3,activation='relu',padding='valid'))
model.add(MaxPooling1D(pool_size=2))

model.add(Bidirectional(LSTM(256,return_sequences=True)))
model.add(Bidirectional(LSTM(128)))


model.add(Dense(6,activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=optim, metrics=['accuracy'])

epochs = 30
batch_size = 8
model.summary()


history = model.fit(train_padded, train_labels, shuffle=True ,
                    epochs=epochs, batch_size=batch_size, 
                    validation_data=(validation_padded,valid_labels),
                    callbacks=[EarlyStopping(monitor='val_accuracy',patience=5)],verbose=1)


# Results For This Model :
#Accuracy -> 73.33 % 
#Loss ->  1.28