def solveA(data):
    letters = list(data[0])
    last = ''
    for a, b in zip(letters, letters[1:]):
        print(a,b)


def solveB(data):
    return(Exception)

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
        print(f"Task 1: {solveA(DATA)}")
        print(f"Task 2: {solveB(DATA)}")