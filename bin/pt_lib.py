import random

#Read variables and values from ini file and return them as a dictionary
def read_ini ():
    reader = open('pt.ini', 'r')
    counter = 0
    d = {}
    try:
        for line in reader:
            k,v = line.split("=")
            v = v.strip("\n")
            v = v.strip("'")
            d[k] = v
    finally:
        return d
        reader.close()
    
def shuffle_cards (deck):
    rnl = random.shuffle(deck)
    return rnl

