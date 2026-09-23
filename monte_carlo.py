from random import random

NUM_ITER = 1_000_000

# C6R5
CONS = 6 # from 0 to 6
REFI = 5 # from 0 to 5

def prob(p: int):
    if p <= 0:
        return 0
    elif p <= 73:
        return 0.006
    elif p <= 89:
        return 0.006 + 0.06 * (p - 73)
    else:
        return 1

def run():
    pity_flag = False
    c = 0
    n = 1

    while True:
        if random() < prob(n):
            if (random() < 0.5) or pity_flag:
                return n + c
            else:
                c = n
                n = 1
                pity_flag = True
        else:
            n += 1

def loop():
    d = dict()

    for _ in range(NUM_ITER):
        
        i = 0
        for _ in range(CONS + REFI + 1):
            i += run()
            
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return d

def write():
    data = loop()
    with open("output.txt", "w", encoding="utf-8") as file:
        for key in sorted(data.keys()):
            file.write(f"{key}: {data[key]}\n")

write(1_000_000)
