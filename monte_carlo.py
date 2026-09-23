from random import random

def prob_char(p: int):
    if p <= 0:
        return 0
    elif p <= 73:
        return 0.006
    elif p <= 89:
        return 0.006 + 0.06 * (p - 73)
    else:
        return 1

def prob_weap(p: int):
    if p <= 0:
        return 0
    elif p <= 62:
        return 0.007
    elif p <= 76:
        return 0.007 + 0.07 * (p - 62)
    else:
        return 1

def run_char():
    pity_flag = False
    c = 0
    n = 1

    while True:
        if random() < prob_A(n):
            if (random() < 0.5) or pity_flag:
                return n + c
            else:
                c = n
                n = 1
                pity_flag = True
        else:
            n += 1

def run_weap():
    

def loop(n_iter):
    d = dict()

    for _ in range(n_iter):
        i = run()
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return d

def write(n_iter):
    data = loop(n_iter)
    with open("output.txt", "w", encoding="utf-8") as file:
        for key in sorted(data.keys()):
            file.write(f"{key}: {data[key]}\n")

write(10_000)
