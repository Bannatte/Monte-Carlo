from random import random

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

def loop(n_iter):
    d = dict()

    for _ in range(n_iter):
        i = run() + run() + run() + run() + run() + run() + run() + run() + run() + run() + run() + run()
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

write(1_000_000)
