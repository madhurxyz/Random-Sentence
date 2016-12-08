import random
import time
import sys

def random_sentence(number):
    

if __name__ == '__main__':
    t0 = time.time()
    num_of_words = int(sys.argv[1])
    sentence = random_sentence(num_of_words)
    t1 = time.time()
    print(t1- t0)
