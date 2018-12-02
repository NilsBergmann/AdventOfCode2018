import operator as op

DATA = "Day01/Data.txt"

def a():
    cumSum = 0
    with open(DATA) as file:
        for line in file:
            operator = line[0]
            number = int(line[1:])
            cumSum = operators[operator](cumSum, number)
    return(cumSum)

def b():
    cumSums = [0]
    while(True):
        print("loop")
        with open(DATA) as file:
            for line in file:
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

if __name__== "__main__":
    print(a())
    print(b())