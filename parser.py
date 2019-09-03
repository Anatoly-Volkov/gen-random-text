import pickle
import random
import re


class model:
    data = dict()
    words = []
    # key (first word, second word)
    # value (array of possible words)

    def __init__(self, data, words):
        self.data = data
        self.words = words

    def fit(self, file_name):
        f_r = open(file_name, "r")
        text = f_r.read()
        f_r.close()
        text = text.lower()
        reg = re.compile("[^a-z'. ]")
        text = reg.sub('', text)
        sent = text.split('.')
        for elem in sent:
            now = elem.split(' ')
            L = len(now)
            for w in now:
                self.words.append(w)
            for i in range(L - 2):
                w1 = now[i]
                w2 = now[i + 1]
                w3 = now[i + 2]
                if (self.data.get((w1, w2)) is None):
                    self.data[(w1, w2)] = []
                self.data[(w1, w2)].append(w3)

    def gen(self, L):
        arr = []
        while (L > 0):
            w1 = random.choice(self.words)
            w2 = random.choice(self.words)
            while (self.data.get((w1, w2)) is None):
                w1 = random.choice(self.words)
                w2 = random.choice(self.words)
            L -= 2
            print(w1[:1].upper() + w1[1:], end=' ')
            print(w2, end=' ')
            while (L > 0 and self.data.get((w1, w2)) is not None):
                w3 = random.choice(self.data[(w1, w2)])
                print(w3, end=' ')
                L -= 1
                w1, w2 = w2, w3
            print('.')

d1 = dict()
w = []
A = model(d1, w)

with open('model_small.pickle', 'rb') as f:
    A = pickle.load(f)

# A.fit("SW_EpisodeIV.txt")
# A.fit("HP1.txt")
# A.fit("wiki_small.txt")

with open('model_small.pickle', 'wb') as f:
    pickle.dump(A, f)
