from aocd import get_data

def solveA(data:str):
    return len(completeReaction(data))

def solveB(data:str):
    letters = set([letter.upper() for letter in data])
    lengths = []
    for letter in letters:
        trimmed = data.replace(letter, "").replace(letter.lower(), "")
        lengths.append(solveA(trimmed))
    return min(lengths)

def react(a:chr,b:chr)->bool:
    return a.upper() == b.upper() and not a == b

def completeReaction(data)->list:
    stack = ["$"] #Init with one element to simplify loop
    for letter in data:
        if react(letter, stack[-1]):
            stack.pop()
        else:
            stack.append(letter)
    return stack[1:]


if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 5
    if(__DAY is None):
        print("Please remember to set the day.")
    else:
        DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
        print(f"Task 1: {solveA(DATA[0].strip())}")
        print(f"Task 2: {solveB(DATA[0].strip())}")