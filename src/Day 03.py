from typing import collections

from aocd import get_data


def solveA(data):
    claimed = []
    for line in data:
        print(line)
        claim = Claim.fromDataLine(line)
        print(claim)
        for point in claim.points:
            claimed.append(point)
    count = collections.Counter(claimed)
    claimedTwice = len([1 for pos, count in count.items() if count >= 2])
    return claimedTwice

def solveB(data):
    claims = [Claim.fromDataLine(line) for line in data]
    for claim in claims:
        intersects = False
        for other in claims:
            if other == claim:
                continue
            print(f"Comparing {claim.id} and {other.id}")
            intersects |= bool(set(claim.points) & set(other.points))
            if intersects:
                break
        if not intersects:
            return claim.id

class Claim:
    def __init__(self, ID, posX, posY, height, width):
        self.id = ID
        self.x = posX
        self.y = posY
        self.h = height
        self.w = width
        self.points = []
        for currH in range(0,self.h):
            for currW in range(0,self.w):
                self.points.append((self.x+currW, self.y+currH))

    @classmethod
    def fromDataLine(cls, line):
        __id, _, __pos, __size = line.split()
        claimID = int(__id[1:])
        posX, posY = [int(x) for x in __pos[:-1].split(",")]
        width, height = [int(x) for x in __size.split("x")]
        return Claim(claimID, posX, posY, height, width)

    def __str__(self):
        return f"{self.id}: ({self.x},{self.y}) {self.w}x{self.h}"

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 3
    if(__DAY is None):
        print("Please remember to set the day.")
    else:
        DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
        print(f"Task 1: {solveA(DATA)}")
        print(f"Task 2: {solveB(DATA)}")