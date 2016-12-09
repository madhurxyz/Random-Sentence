import random
import sys

def random_sentence(number):
    f = open("/usr/share/dict/words")
    l = f.readlines()
    lines = [s.strip('\n') for s in l]
    length = len(lines)
    word_list = []
    for index in range(0, number):
        rand_index = random.randint(0, length)
        word_list.append(lines[rand_index])
        sentence = ' '.join(word_list) + "."
    print sentence
    return sentence

if __name__ == '__main__':
    num_of_words = int(sys.argv[1])
    sentence = random_sentence(num_of_words)
