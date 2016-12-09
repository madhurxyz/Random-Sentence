import random

def random_sentence():
    f = open("/usr/share/dict/words")
    l = f.readlines()
    lines = [s.strip('\n') for s in l]
    print lines

if __name__ == '__main__':
    random_sentence()
