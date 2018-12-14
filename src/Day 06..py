from aocd import get_data

from collections import defaultdict


def distance(a, b):
    return abs((a[0] - b[0])) - abs((a[1]-b[1]))

def solveA(data):
    dataPoints = {}
    for line in data:
        x, y = map(int, line.split(", "))
        dataPoints[len(dataPoints)] = (x,y)

    # Create grid
    minX = min(dataPoints.values(), key=lambda p: p[0])[0] - 1
    maxX = max(dataPoints.values(), key=lambda p: p[0])[0] + 2
    minY = min(dataPoints.values(), key=lambda p: p[1])[1] - 1
    maxY = max(dataPoints.values(), key=lambda p: p[1])[1] + 2
    clostestPoints = defaultdict(list)
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            # Get All distances to data points
            distances = {}
            for idf, pos in dataPoints.items():
                distances[idf] = distance((x,y), pos)
            # Get minmal distanced point ID
            minDistID = min(distances, key=distances.get)
            # Check if two or more are possible matches
            if sum([value == distances[minDistID] for value in distances.values()]) == 1:
                clostestPoints[minDistID].append((x,y))
    # Filter infinite areas
    pointsOutsideBorder = [(x,minY) for x in range(minX, maxX)]
    pointsOutsideBorder += [(x,maxY) for x in range(minX, maxX)]
    pointsOutsideBorder += [(minX,y) for y in range(minY, maxY)]
    pointsOutsideBorder += [(maxX,y) for y in range(minY, maxY)]

    filtered = {idf: points for idf, points in clostestPoints.items() if not set(pointsOutsideBorder) & set(points)}
    # Get maximum
    return max(map(len,filtered.values()))


def solveB(data):
    return(Exception)

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 6
    if(__DAY is None):
        print("Please remember to set the day.")
    else:
        DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
        print(f"Task 1: {solveA(DATA)}")
        print(f"Task 2: {solveB(DATA)}")