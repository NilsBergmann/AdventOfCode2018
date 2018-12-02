from itertools import combinations

from collections import Counter


DATA = "Day02/Data.txt"

def a():
    with open(DATA) as file:
        countDoubles = 0
        countTriples = 0
        for line in file:
            hasDoubles = False
            hasTriples = False
            counts = Counter(line)
            for character, count in counts.items():
                hasDoubles |= (count == 2)
                hasTriples |= (count == 3)
            countDoubles += int(hasDoubles) # False -> 0, True -> 1
            countTriples += int(hasTriples)
        return(countDoubles * countTriples)

def b():
    with open(DATA) as file:
        for lineA, lineB in combinations(file, 2):
            diff = [a == b for a, b in zip(lineA, lineB)]
            if sum(diff) == len(lineA) - 1:
                commonChars = [a for a,b in zip(lineA, diff) if b]
                return "".join(commonChars)
    return(Exception)

if __name__== "__main__":
    print(a())
    print(b())