import re

# Sample paragraph
paragraph = open("input.txt", "r").read()

# Remove special characters (keeping only letters, numbers, and spaces)
clean_paragraph = re.sub(r"[^a-zA-Z0-9\s]", "", paragraph)

# Remove extra whitespace (leading, trailing, and multiple spaces)
clean_paragraph = re.sub(r"\s+", " ", clean_paragraph).strip()

# Print results
print("\nCleaned Paragraph:\n")
print(clean_paragraph)