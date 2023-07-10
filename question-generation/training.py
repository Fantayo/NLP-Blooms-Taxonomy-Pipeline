import argparse
import glob
import json
import time
import logging 
import random
import re
from itertools import chain
from string import punctuation

import pandas as pd
import numpy as np

import torch
from torch.utils.data import Dataset, DataLoader

from termcolor import colored
import textwrap

from transformers import AdamW 
from transformers import T5ForConditionalGeneration
from transformers import T5Tokenizer
from transformers import get_linear_schedule_with_warmup
import pytorch_lightning as pl

from tqdm.notebook import tqdm
import copy

pl.seed_everything(42)


t5_tokenizer = T5Tokenizer.from_pretrained('t5-base')
t5_model = T5ForConditionalGeneration.from_pretrained('t5-base')

class QuestionGenerationDataset(Dataset):

    def __init__(self, tokenizer, filepath, max_len_inp=512,max_len_out=96):

        self.path = filepath
        self.passage_column = "context"
        self.answer = "text"
        self.question = "question"

        self.data = pd.read_csv(self.path , nrows = 1000)

        self.max_len_input = max_len_inp
        self.max_len_output = max_len_out
        self.tokenizer = tokenizer
        self.inputs = []
        self.targets = []
        self.skippedcount =0

        self._build()

    def __len__(self