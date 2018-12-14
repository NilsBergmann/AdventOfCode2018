from aocd import get_data

from collections import defaultdict


def solveA(data):
    rules = [lineToTuple(x) for x in data]
    steps = set([r[0] for r in rules] + [r[1] for r in rules])

    order = ""
    while steps:
        candidates = getAvailable(steps, rules)
        candidates.sort()
        current = candidates[0]
        order += current
        steps.remove(current)
        rules = [(x,y) for (x,y) in rules if x != current]
    return(order)

def getAvailable(steps, rules):
    return [letter for letter in steps if all([y != letter for (x,y) in rules])]

def solveB(data):
    return(Exception)

def lineToTuple(line):
    splitted = line.split()
    return (splitted[1], splitted[7])

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 7
    if(__DAY is None):
        print("Please remember to set the day.")
    else:
        DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
        print(f"Task 1: {solveA(DATA)}")
        print(f"Task 2: {solveB(DATA)}")