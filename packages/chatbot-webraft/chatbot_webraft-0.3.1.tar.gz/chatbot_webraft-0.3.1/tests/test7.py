import numpy as np

# Sample list of sentences
sentence_list = ['I like apples', 'I like bananas', 'I love cherries', 'Grapes are my favorite fruit', 'Oranges are juicy', 'Pears are delicious','hello bro how are you bro']

# Define vocabulary
vocab = set()
for sentence in sentence_list:
    vocab.update(sentence.lower().split())
vocab = sorted(list(vocab))
vocab_size = len(vocab)

# Create mapping from words to indices
word2idx = {word: i for i, word in enumerate(vocab)}
idx2word = {i: word for word, i in word2idx.items()}

# Convert sentences to sequences of word indices
sequences = []
for sentence in sentence_list:
    sequence = [word2idx[word] for word in sentence.lower().split()]
    sequences.append(sequence)

# Define neural network model
input_size = 19
hidden_size = 19
output_size = vocab_size

Wxh = np.random.randn(hidden_size, input_size) * 0.01
Whh = np.random.randn(hidden_size, hidden_size) * 0.01
Why = np.random.randn(output_size, hidden_size) * 0.01
bh = np.zeros((hidden_size, 1))
by = np.zeros((output_size, 1))

def rnn_step(x, h_prev):
    h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h_prev) + bh)
    y = np.dot(Why, h) + by
    return h, y

def rnn_forward(sequence):
    xs, hs, ys = {}, {}, {}
    hs[-1] = np.zeros((hidden_size, 1))
    for t in range(len(sequence)):
        xs[t] = np.zeros((vocab_size, 1))
        xs[t][sequence[t]] = 1
        hs[t], ys[t] = rnn_step(xs[t], hs[t-1])
    return xs, hs, ys

# Define function to complete sentence
def complete_sentence(user_input):
    # Convert user input to sequence of word indices
    input_words = user_input.lower().split()
    input_sequence = [word2idx[word] for word in input_words]
    # Generate next word predictions using RNN
    # Initialize hidden state
    h_prev = np.zeros((hidden_size, 1))

    # Iterate over input sequence and update hidden state
    for idx in input_sequence:
        x = np.zeros((vocab_size, 1))
        x[idx] = 1
        h_prev, _ = rnn_step(x, h_prev)

    # Generate output sequence
    output_sequence = []
    x = np.zeros((vocab_size, 1))
    for _ in range(5):  # Generate 20 words
        h_prev, y = rnn_step(x, h_prev)
        p = np.exp(y) / np.sum(np.exp(y))  # Softmax activation
        idx = np.random.choice(range(vocab_size), p=p.ravel())
        x = np.zeros((vocab_size, 1))
        x[idx] = 1
        output_sequence.append(idx)

    # Convert output sequence to sentence
    output_words = [idx2word[idx] for idx in output_sequence]
    output_sentence = ' '.join(output_words)

    return output_sentence


print(complete_sentence("I like"))