import keras
import numpy as np


path = keras.utils.get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")

text = open(path).read().lower()

print('말뭉치 크기', len(text))

# 3D Numpy Array
maxlen = 60
step = 3

sentences = []
next_char = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i+maxlen])
    next_char.append(text[i + maxlen])

    print('Sequences Number: ', len(sentences))

    chars = sorted(list(set(text)))
    print('Unique Chars: ', len(chars))

    char_indices = dict((char, chars.index(char)) for char in chars)

    x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
    y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            x[i, t, char_indices[char]] = 1
        y[i, char_indices[next_char[i]]] = 1
