import string
import re

# Sample paragraph
paragraph = open("input.txt", "r").read()

# Convert to lowercase
lowercase_paragraph = paragraph.lower()

# Remove punctuation using regex
clean_paragraph = re.sub(f"[{re.escape(string.punctuation)}]", "", lowercase_paragraph)

# Print results
print("\nLowercase & Punctuation Removed:\n")
print(clean_paragraph)
