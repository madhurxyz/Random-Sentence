import random

def random_sentence():
    f = open("/usr/share/dict/words")
    l = f.readlines()
    lines = [s.strip('\n') for s in l]
    length = len(lines)
    rand_index = random.randint(0, length)
    print lines[rand_index]

if __name__ == '__main__':
    random_sentence()
