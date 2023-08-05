import numpy as np
import string


# define the corpus
corpus = open('data.txt').read().lower().translate(str.maketrans('', '', string.punctuation)).split()

# create the word-to-index and index-to-word mappings
vocab = sorted(set(corpus))
word2idx = {w: i for i, w in enumerate(vocab)}
idx2word = {i: w for i, w in enumerate(vocab)}

# create the training data
WINDOW_SIZE = 2
train_data = []
for i in range(len(corpus) - WINDOW_SIZE):
    train_data.append(([corpus[j] for j in range(i, i + WINDOW_SIZE)], corpus[i + WINDOW_SIZE]))

# create the LSTM model
INPUT_SIZE = len(vocab)
HIDDEN_SIZE = 100
OUTPUT_SIZE = len(vocab)
LEARNING_RATE = 0.1

# initialize weights
U = np.random.randn(INPUT_SIZE, HIDDEN_SIZE) * 0.01
V = np.random.randn(HIDDEN_SIZE, OUTPUT_SIZE) * 0.01
W = np.random.randn(HIDDEN_SIZE, HIDDEN_SIZE) * 0.01
bh = np.zeros((1, HIDDEN_SIZE))
by = np.zeros((1, OUTPUT_SIZE))

# train the LSTM model
for epoch in range(50000):
    loss = 0
    for X, y in train_data:
        # convert words to indices
        x_idx = [word2idx[w] for w in X]
        y_idx = word2idx[y]

        # initialize input and hidden states
        h = np.zeros((1, HIDDEN_SIZE))
        inputs = np.zeros((1, INPUT_SIZE))
        for i in x_idx:
            inputs[0, i] = 1

        # forward pass
        h = np.tanh(np.dot(inputs, U) + np.dot(h, W) + bh)
        y_hat = np.exp(np.dot(h, V) + by) / np.sum(np.exp(np.dot(h, V) + by))

        # calculate loss
        loss += -np.log(y_hat[0, y_idx])

        # backward pass
        dy = np.copy(y_hat)
        dy[0, y_idx] -= 1
        dV = np.dot(h.T, dy)
        dby = dy
        dh = np.dot(dy, V.T)
        dg = (1 - h ** 2) * dh
        dU = np.dot(inputs.T, dg)
        dbh = dg

        # update weights
        U -= LEARNING_RATE * dU
        V -= LEARNING_RATE * dV
        W -= LEARNING_RATE * dh
        bh -= LEARNING_RATE * dbh
        by -= LEARNING_RATE * dby
    correct_count = 0
    total_count = 0
    for X, y in train_data:
        x_idx = [word2idx[w] for w in X]
        y_idx = word2idx[y]
        h = np.zeros((1, HIDDEN_SIZE))
        inputs = np.zeros((1, INPUT_SIZE))
        for i in x_idx:
            inputs[0, i] = 1
        h = np.tanh(np.dot(inputs, U) + np.dot(h, W) + bh)
        y_hat = np.exp(np.dot(h, V) + by) / np.sum(np.exp(np.dot(h, V) + by))
        predicted_idx = np.argmax(y_hat)
        if predicted_idx == y_idx:
            correct_count += 1
        total_count += 1
    accuracy = correct_count / total_count
    print('Epoch:', epoch, '/ 5000' ,' \n Loss:', loss, 'Accuracy:', accuracy)


# generate sentences
seed = 'the'
for i in range(10):
    x = np.zeros((1, INPUT_SIZE))
    x[0, word2idx[seed]] = 1
    h = np.zeros((1, HIDDEN_SIZE))
    sentence = [seed]
    for j in range(20):
        h = np.tanh(np.dot(x, U) + np.dot(h, W) + bh)
        y = np.dot(h, V) + by
        p = np.exp(y) / np.sum(np.exp(y))
        idx = np.random.choice(range(len(vocab)), p=p.ravel())
        if idx2word[idx] == '.':
            sentence.append('.')
            break
        sentence.append(idx2word[idx])
        x = np.zeros((1, INPUT_SIZE))
        x[0, idx] = 1
        print(' '.join(sentence))
print('U:', U)
print('V:', V)
print('W:', W)
print('bh:', bh)
print('by:', by)

np.savez('weights.npz', U=U, V=V, W=W, bh=bh, by=by)
