""" Simple preprocessing """

import re

def preprocess_text(sentence):

  # Remove punctuations
  sentence = re.sub('[^a-zA-Z0-9]', ' ', sentence)
  # Removing multiple spaces
  sentence = re.sub(r'\s+', ' ', sentence)
  return sentence.lower()
