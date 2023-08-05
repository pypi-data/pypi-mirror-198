import numpy as np

# Sample list of words
word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear']


def complete_word(user_input):
    # Get all words that start with the user input
    matches = [word for word in word_list if word.startswith(user_input)]

    if not matches:
        return None  # No matches found

    # Calculate the frequency of each letter following the user input
    freqs = np.zeros((len(matches), 26))  # 26 letters in the alphabet
    for i, word in enumerate(matches):
        for j in range(len(user_input), len(word)):
            letter_idx = ord(word[j]) - ord('a')
            freqs[i, letter_idx] += 1
    freqs /= freqs.sum(axis=1, keepdims=True)  # Normalize by row sum

    # Use the most common letter to predict the next character
    next_char_freq = freqs.mean(axis=0)
    next_char_idx = np.argmax(next_char_freq)
    next_char = chr(next_char_idx + ord('a'))

    return user_input + next_char


# Example usage
user_input = 'b'
predicted_word = complete_word(user_input)
print(predicted_word)
