# Ask user to input a complete statement, print the number of words.

statement = input("Enter a complete statement: ")
# Split by whitespace and count non-empty parts
words = statement.split()
word_count = len(words)
print(word_count)