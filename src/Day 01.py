import operator as op

def solveA(data):
    cumSum = 0
    for line in data:
        operator = line[0]
        number = int(line[1:])
        cumSum = operators[operator](cumSum, number)
    return(cumSum)

def solveB(data):
    cumSums = [0]
    while(True):
        print("loop")
        for line in data:
            operator = line[0]
            number = int(line[1:])
            newSum = operators[operator](cumSums[-1], number)
            if newSum in cumSums:
                return newSum
            else:
                cumSums.append(newSum)

operators = {
    "+": op.add,
    "-": op.sub
    }

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 1
    if(__DAY is None):
        print("Please remember to set the day.")
    DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
    print(f"Task 1: {solveA(DATA)}")
    print(f"Task 2: {solveB(DATA)}")