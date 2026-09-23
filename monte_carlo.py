from random import random

def prob_A(p: int):
    if 0 <= p <= 73:
        return 0.006
    elif p <= 89:
        return 0.008 + 0.06 * (p - 73)
    elif p == 90:
        return 1
    else:
        return 0

def run():
    pity_flag = False
    c = 0
    n = 0

    while True:
        if prob_A(n) < random():
            if (random() < 0.5) or pity_flag:
                return n + c
            else:
                c = n
                n = 1
                pity_flag = True
        else:
            n += 1

def loop(n_iter):
    d = {}

    for _ in range(n_iter):
        n = run()
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    
    return sorted(d.keys())

print(loop(10_000))
