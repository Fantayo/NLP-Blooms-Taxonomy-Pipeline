
def create_test_data(tokenizer, test_sentences_pair, max_sequence_length):


  test_sentences1 = [x[0].lower() for x in test_sentences_pair]
  test_sentences2 = [x[1].lower() for x in test_sentences_pair]

  test_sequences_1 = tokenizer.texts_to_sequences(test_sentences1)
  test_sequences_2 = tokenizer.texts_to_sequences(test_sentences2)


  test_data_1 = pad_sequences(test_sequences_1, maxlen=max_sequence_length)
  test_data_2 = pad_sequences(test_sequences_2, maxlen=max_sequence_length)

  return test_data_1, test_data_2

def get_predictions(test_data_1,test_data_2,model):
  preds = list(model.predict([test_data_1, test_data_2], verbose=1).ravel())
  results = [(x, y) for (x, y) in zip(test_sentence_pairs, preds)]
  results.sort(reverse=True)  

  return results


#Enter any custom pair of question texts in test_sentence_pairs :
test_sentence_pairs = [
                       ('What can make Physics easy to learn?','How can you make physics easy to learn?'),
                       ('How many times a day do a clocks hands overlap?','What does it mean that every time I look 