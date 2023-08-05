import numpy as np
import string


def model(corpus,seed,len1=10,len2=20,learning_rate=0.1,hidden_size=100,epochs=10,save="save.npz",traintype="cpu",pretrain="False",pretrain_file="save.npz"):
    corpus = open(corpus).read().lower().translate(str.maketrans('', '', string.punctuation)).split()
    if traintype=="cpu":
        xp = np
    elif traintype=="gpu":
        import cupy as cp
        xp = cp
    elif traintype=="CPU":
        xp = np
    elif traintype=="GPU":
        import cupy as cp
        xp = cp
    else:
        xp=np

    vocab = sorted(set(corpus))
    word2idx = {w: i for i, w in enumerate(vocab)}
    idx2word = {i: w for i, w in enumerate(vocab)}


    WINDOW_SIZE = 2
    train_data = []
    for i in range(len(corpus) - WINDOW_SIZE):
        train_data.append(([corpus[j] for j in range(i, i + WINDOW_SIZE)], corpus[i + WINDOW_SIZE]))


    INPUT_SIZE = len(vocab)
    HIDDEN_SIZE = hidden_size
    OUTPUT_SIZE = len(vocab)
    LEARNING_RATE = learning_rate

    if pretrain == "True":
        data = xp.load(pretrain_file)
        U = data['U']
        V = data['V']
        W = data['W']
        bh = data['bh']
        by = data['by']

    elif pretrain == "False":
        U = xp.random.randn(INPUT_SIZE, HIDDEN_SIZE) * 0.01
        V = xp.random.randn(HIDDEN_SIZE, OUTPUT_SIZE) * 0.01
        W = xp.random.randn(HIDDEN_SIZE, HIDDEN_SIZE) * 0.01
        bh = xp.zeros((1, HIDDEN_SIZE))
        by = xp.zeros((1, OUTPUT_SIZE))
    else:
        U = xp.random.randn(INPUT_SIZE, HIDDEN_SIZE) * 0.01
        V = xp.random.randn(HIDDEN_SIZE, OUTPUT_SIZE) * 0.01
        W = xp.random.randn(HIDDEN_SIZE, HIDDEN_SIZE) * 0.01
        bh = xp.zeros((1, HIDDEN_SIZE))
        by = xp.zeros((1, OUTPUT_SIZE))


    for epoch in range(epochs):
        loss = 0
        for X, y in train_data:

            x_idx = [word2idx[w] for w in X]
            y_idx = word2idx[y]


            h = xp.zeros((1, HIDDEN_SIZE))
            inputs = xp.zeros((1, INPUT_SIZE))
            for i in x_idx:
                inputs[0, i] = 1


            h = xp.tanh(xp.dot(inputs, U) + xp.dot(h, W) + bh)
            y_hat = xp.exp(xp.dot(h, V) + by) / xp.sum(xp.exp(xp.dot(h, V) + by))


            loss += -xp.log(y_hat[0, y_idx])


            dy = xp.copy(y_hat)
            dy[0, y_idx] -= 1
            dV = xp.dot(h.T, dy)
            dby = dy
            dh = xp.dot(dy, V.T)
            dg = (1 - h ** 2) * dh
            dU = xp.dot(inputs.T, dg)
            dbh = dg


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
            h = xp.zeros((1, HIDDEN_SIZE))
            inputs = xp.zeros((1, INPUT_SIZE))
            for i in x_idx:
                inputs[0, i] = 1
            h = xp.tanh(xp.dot(inputs, U) + xp.dot(h, W) + bh)
            y_hat = xp.exp(xp.dot(h, V) + by) / xp.sum(xp.exp(xp.dot(h, V) + by))
            predicted_idx = xp.argmax(y_hat)
            if predicted_idx == y_idx:
                correct_count += 1
            total_count += 1
        accuracy = correct_count / total_count
        print('Epoch:', epoch+ 1, '/ ', epochs, ' \n Loss:', loss, 'Accuracy:', accuracy )

    for i in range(len1):
        x = xp.zeros((1, INPUT_SIZE))
        x[0, word2idx[seed]] = 1
        h = xp.zeros((1, HIDDEN_SIZE))
        sentence = [seed]
        for j in range(len2):
            h = xp.tanh(xp.dot(x, U) + xp.dot(h, W) + bh)
            y = xp.dot(h, V) + by
            p = xp.exp(y) / xp.sum(xp.exp(y))
            idx = xp.random.choice(range(len(vocab)), p=p.ravel())
            if idx2word[idx] == '.':
                sentence.append('.')
                break
            sentence.append(idx2word[idx])
            x = xp.zeros((1, INPUT_SIZE))
            x[0, idx] = 1
            xp.savez(save, U=U, V=V, W=W, bh=bh, by=by,word2idx=word2idx,idx2word=idx2word)
        return  ' '.join(sentence)
print(model("internet_archive_scifi_v3.txt","the",epochs=100,hidden_size=50,learning_rate=0.1))
