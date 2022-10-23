
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import tensorflow.keras.backend as K


from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, LSTM
import tensorflow.keras.backend as K
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Lambda

#Imp PARAMS :
maxsentence_length=sentence_length
embedding_dim=100
max_num_words=50000
hiddendim=128   

#Main Model:
def manhattandistance(l1,l2):
		return K.exp(-K.sum(K.abs(l1-l2), axis=1, keepdims=True))

def siamese_manhattan_network(embed_mat_weights):


	ques1 = Input(shape=(maxsentence_length,))
	ques2 = Input(shape=(maxsentence_length,))

	embedding_layer = Embedding(input_dim=max_num_words,output_dim=embedding_dim,weights=[embed_mat_weights],
    		trainable=False,input_length=maxsentence_length)

	ques1_embed = embedding_layer(ques1)
	ques2_embed = embedding_layer(ques2)

	lstm = LSTM(hiddendim,return_