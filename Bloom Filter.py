""" PYTHON IMPLEMENTATION OF BLOOM FILTER """

import mmh3 #MurmurHash3, set of fast and robust hash functions.
from bitarray import bitarray

#we have taken the size of bit array as 64 and using 3 hash functions
filter=bitarray(64) 
filter.setall(0)
no_of_hash=3

def add(item):
    for i in range(no_of_hash):
        index=mmh3.hash(item,i)%64
        filter[index]=1

def find(item):
    for i in range(no_of_hash):
        index=mmh3.hash(item,i)%64
        if filter[index]==0:
            return False
    return True

animals = ['dog', 'cat', 'giraffe', 'horse', 'eagle', 'bird', 'lion',
           'butterfly', 'ant', 'anaconda', 'bear', 'chicken', 'dolphin',
           'donkey', 'crow', 'crocodile']

#ADDING ANIMALS
for animal in animals:
    add(animal)

animals_to_check = ['dog', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                 'whale', 'shark', 'lion', 'donkey', 'crow', 'crocodile']

# MEMBERSHIP TESTING
for animal in animals_to_check:
    if find(animal):
        print('{} already exist'.format(animal))
    else:
        print('{} not present'.format(animal))
