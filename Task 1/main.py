
from nltk.tokenize import sent_tokenize, word_tokenize

# Sample paragraph
text = open("input.txt").read()

# Sentence Tokenization
sentences = sent_tokenize(text)
print("\nSentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWords:", words)