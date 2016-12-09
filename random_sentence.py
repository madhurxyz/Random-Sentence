import random

def random_sentence(number):
    f = open("/usr/share/dict/words")
    l = f.readlines()
    lines = [s.strip('\n') for s in l]
    length = len(lines)
    word_list = []
    for index in range(0, number):
        rand_index = random.randint(0, length)
        word_list.append(lines[rand_index])
    print word_list
    return word_list

if __name__ == '__main__':
    random_sentence(5)
