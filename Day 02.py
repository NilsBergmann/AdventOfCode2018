from itertools import combinations

from collections import Counter

def solveA(data):
    countDoubles = 0
    countTriples = 0
    for line in data:
        hasDoubles = False
        hasTriples = False
        counts = Counter(line)
        for character, count in counts.items():
            hasDoubles |= (count == 2)
            hasTriples |= (count == 3)
        countDoubles += int(hasDoubles)
        countTriples += int(hasTriples)
    return(countDoubles * countTriples)

def solveB(data):
    for lineA, lineB in combinations(data, 2):
        diff = [a == b for a, b in zip(lineA, lineB)]
        if sum(diff) == len(lineA) - 1:
            commonChars = [a for a,b in zip(lineA, diff) if b]
            return "".join(commonChars)
    return(Exception)

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 2
    if(__DAY is None):
        print("Please remember to set the day.")
    DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
    print(f"Task 1: {solveA(DATA)}")
    print(f"Task 2: {solveB(DATA)}")