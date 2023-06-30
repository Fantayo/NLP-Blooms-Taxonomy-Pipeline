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

    