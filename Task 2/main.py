import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Sample paragraph
paragraph = open("input.txt", "r").read()

# Tokenize the paragraph into words
words = word_tokenize(paragraph)

# Load English stopwords
stop_words = set(stopwords.words("english"))

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Print results
print("Filtered Words (Without Stopwords):", filtered_words)