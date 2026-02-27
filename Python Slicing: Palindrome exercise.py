# Ask the user to enter a word
word = input("Enter a word: ")

# Convert to lowercase for case-insensitive comparison
word_lower = word.lower()

# Check if the word is a palindrome
if word_lower == word_lower[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
