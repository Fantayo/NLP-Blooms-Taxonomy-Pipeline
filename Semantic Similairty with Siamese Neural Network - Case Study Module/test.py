
def create_test_data(tokenizer, test_sentences_pair, max_sequence_length):


  test_sentences1 = [x[0].lower() for x in test_sentences_pair]
  test_sentences2 = [x[1].lower() for x in test_sentences_pair]

  test_sequences_1 = tokenizer.texts_to_sequences(test_sentences1)
  test_sequences_2 = tokenizer.texts_to_sequences(test_sentences2)


  test_data_1 = pad_sequences(test_sequences_1, maxlen=max_sequence_length)
  test_data_2 = pad_sequences(test_sequenc