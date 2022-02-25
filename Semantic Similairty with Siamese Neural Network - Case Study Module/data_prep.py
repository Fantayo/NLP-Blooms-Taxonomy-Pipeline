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
i