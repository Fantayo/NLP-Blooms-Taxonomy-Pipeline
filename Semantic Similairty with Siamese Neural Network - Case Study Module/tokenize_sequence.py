
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

#Custom function to obtain the length of largest string in corpus :
def get_max_seq_len(corpus):
  corpus_len=[]

  for question in corpus:
    question_list=(str(question)).split()
    corpus_len.append(len