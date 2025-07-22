# Project: Word Frequency Counter
import re # Importing the regular expression module

# 1. Create a function that takes a string of text as input.
def word_frequency_counter(text):
  # 3. Use conditional sentences to handle special cases (e.g., empty input).
  if not text:
    return {}

  # Split the text into words using regular expression and convert to lowercase
  words = re.findall(r'\b\w+\b', text.lower())

  # 2. Create a dictionary to store the frequency of each word in the text.
  frequency = {}

  # 4. Use loops to iterate over the words in the text.
  for word in words:
    # Update the frequency count for the word
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
  return frequency

# 5. Use a recursive function to process the text and update the word frequency dictionary
def recursive_word_counter(text, frequency=None):
  if frequency is None:
    frequency = {}

  if not text.strip():
    return frequency

  match = re.match(r'(\b\w+\b)\W(.*)', text.lower())

  if not match: # If no more words are found, return frequency dictionary
    return frequency
    
  # Extract the word and remaining text
  word = match.group(1)
  remaining_text = match.group(2).strip()

  # Update the frequency count for the word 
  frequency[word] = frequency.get(word, 0) + 1

  return recursive_word_counter(remaining_text, frequency)

text_input = 'Hello world! This is a test. Hello again.'

# Example usage of the word frequency counter
print(word_frequency_counter(text_input))  
# Example usage of the recursive word frequency counter
print(recursive_word_counter(text_input))
# Example usage of the recursive word frequency counter with a different text
another_text_input = 'Python is great. Python is fun. Python is powerful.'
print(recursive_word_counter(another_text_input))
# Example usage of the recursive word frequency counter with an empty string
empty_text_input = ''
print(recursive_word_counter(empty_text_input))