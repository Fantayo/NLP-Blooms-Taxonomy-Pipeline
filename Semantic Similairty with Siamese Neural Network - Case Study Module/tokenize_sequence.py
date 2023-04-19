
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

#Custom function to obtain the length of largest string in corpus :
def get_max_seq_l