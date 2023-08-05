import numpy as np
import string
class LSTM:
    def __init__(self, corpus_file):
        # define the corpus
        corpus = open(corpus_file).read().lower().translate(str.maketrans('', '', string.punctuation)).split()

        # create the word-to-index and index-to-word mappings
        self.vocab = sorted(set(corpus))
        self.word2idx = {w: i for i, w in enumerate(self.vocab)}
        self.idx2word = {i: w for i, w in enumerate(self.vocab)}

        # create the training data
        self.WINDOW_SIZE = 2
        self.train_data = []
        for i in range(len(corpus) - self.WINDOW_SIZE):
            self.train_data.append(([corpus[j] for j in range(i, i + self.WINDOW_SIZE)], corpus[i + self.WINDOW_SIZE]))

        # initialize weights
        self.INPUT_SIZE = len(self.vocab)
        self.HIDDEN_SIZE = 100
        self.OUTPUT_SIZE = len(self.vocab)
        self.LEARNING_RATE = 0.1
        self.U = np.random.randn(self.INPUT_SIZE, self.HIDDEN_SIZE) * 0.01
        self.V = np.random.randn(self.HIDDEN_SIZE, self.OUTPUT_SIZE) * 0.01
        self.W = np.random.randn(self.HIDDEN_SIZE, self.HIDDEN_SIZE) * 0.01
        self.bh = np.zeros((1, self.HIDDEN_SIZE))
        self.by = np.zeros((1, self.OUTPUT_SIZE))

    def train(self, epochs):
        for epoch in range(epochs):
            loss = 0
            for X, y in self.train_data:
                # convert words to indices
                x_idx = [self.word2idx[w] for w in X]
                y_idx = self.word2idx[y]

                # initialize input and hidden states
                h = np.zeros((1, self.HIDDEN_SIZE))
                inputs = np.zeros((1, self.INPUT_SIZE))
                for i in x_idx:
                    inputs[0, i] = 1

                # forward pass
                h = np.tanh(np.dot(inputs, self.U) + np.dot(h, self.W) + self.bh)
                y_hat = np.exp(np.dot(h, self.V) + self.by) / np.sum(np.exp(np.dot(h, self.V) + self.by))

                # calculate loss
                loss += -np.log(y_hat[0, y_idx])

                # backward pass
                dy = np.copy(y_hat)
                dy[0, y_idx] -= 1
                dV = np.dot(h.T, dy)
                dby = dy
                dh = np.dot(dy, self.V.T)
                dg = (1 - h ** 2) * dh
                dU = np.dot(inputs.T, dg)
                dbh = dg

                # update weights
                self.U -= self.LEARNING_RATE * dU
                self.V -= self.LEARNING_RATE * dV
                self.W -= self.LEARNING_RATE * dh
                self.bh -= self.LEARNING_RATE * dbh
                self.by -= self.LEARNING_RATE * dby
            correct_count = 0
            total_count = 0
            for X, y in self.train_data:
                x_idx = [self.word2idx[w] for w in X]
                y_idx = self.word2idx[y]
                h = np.zeros((1, self.HIDDEN_SIZE))
                inputs = np.zeros((1, self.INPUT_SIZE))
                for i in x_idx:
                    inputs[0, i] = 1
                # forward pass
                h = np.tanh(np.dot(inputs, self.U) + np.dot(h, self.W) + self.bh)
                y_hat = np.exp(np.dot(h, self.V) + self.by) / np.sum(np.exp(np.dot(h, self.V) + self.by))

                # check if predicted word is correct
                if np.argmax(y_hat) == y_idx:
                    correct_count += 1
                total_count += 1

            # calculate accuracy and loss for epoch
            accuracy = correct_count / total_count
            loss /= len(self.train_data)

            # print progress
            print(f"Epoch {epoch + 1}: Loss = {loss:.4f}, Accuracy = {accuracy:.4f}")
    def predict(self,seed,len1=10,len2=20):
        seed = seed
        for i in range(len1):
            x = np.zeros((1, self.INPUT_SIZE))
            x[0, self.word2idx[seed]] = 1
            h = np.zeros((1, self.HIDDEN_SIZE))
            sentence = [seed]
            for j in range(len2):
                h = np.tanh(np.dot(x, self.U) + np.dot(h, self.W) + self.bh)
                y = np.dot(h, self.V) + self.by
                p = np.exp(y) / np.sum(np.exp(y))
                idx = np.random.choice(range(len(self.vocab)), p=p.ravel())
                if self.idx2word[idx] == '.':
                    sentence.append('.')
                    break
                sentence.append(self.idx2word[idx])
                x = np.zeros((1, self.INPUT_SIZE))
                x[0, idx] = 1
                return ' '.join(sentence)
# create an instance of the LSTM class
lstm_model = LSTM('data.txt')

# train the model for 10 epochs
lstm_model.train(10)

# predict the next word given two input words
v = "the quick brown fox "
y_pred = lstm_model.predict(v,len1=10,len2=10)

# print the predicted word
print(y_pred)
