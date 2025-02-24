from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Sample text
text = open("input.txt", "r").read()

# Tokenize words
words = word_tokenize(text)

# Initialize Stemmer and Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Apply stemming and lemmatization
stemmed_words = [stemmer.stem(word) for word in words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print results
print("\nStemmed Words:        ", stemmed_words)
print("\nLemmatized Words:     ", lemmatized_words)
