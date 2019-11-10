import random

runes = ["I", "O"]

def scribe(list):
    x = random.randrange(0,2)
    return list[x]

i = 0

while i < 4:
    print(scribe(runes) + "\t" + scribe(runes))
    i += 1