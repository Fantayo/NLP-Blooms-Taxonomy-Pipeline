
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

#Main Mode