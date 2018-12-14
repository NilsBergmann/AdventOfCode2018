from aocd import get_data

from collections import defaultdict


def solve(data):
    parsed = parseSleepTimes(data)
    sleptMinutes = defaultdict(lambda: defaultdict(int))
    sumSlept = {}
    for guardID in parsed.keys():
        for start, end in parsed[guardID]:
            for minute in range(start, end):
                sleptMinutes[guardID][minute] += 1
        sumSlept[guardID] = sum(sleptMinutes[guardID].values())

    # Part 1
    # - Get ID of guard that sleeps the most
    sleptMostID = max(sumSlept, key=sumSlept.get)
    # - Get the minute he sleeps most often
    sleptMostMinute = max(sleptMinutes[sleptMostID], key=sleptMinutes[sleptMostID].get)
    resultA = sleptMostID * sleptMostMinute
    print(f"Part 1: {resultA}")

    # Part 2
    # - Get list of most slept minutes by guard and which minute he slept most
    minutes = {}
    minutesValue = {}
    for guardID, sleepLog in sleptMinutes.items():
        maxID = max(sleepLog, key=sleepLog.get)
        minutes[guardID] = maxID
        minutesValue[guardID] = sleepLog[maxID]
    # - Get guard with most same minutes slept
    guardID = max(minutesValue, key=minutesValue.get)
    resultB = guardID * minutes[guardID]
    print(f"Part 2: {resultB}")

def getTime(line):
    splitted = line.split()
    time = splitted[1][:-1]
    minutes = int(time.split(":")[1])
    return minutes

def parseSleepTimes(data):
    id, start, end = None, None, None
    guardSleepTimes = defaultdict(list)
    for line in data:
        splitted = line.split()
        time = getTime(line)
        if splitted[2] == "Guard":
            id = int(splitted[3][1:])
        elif splitted[2] == "wakes":
            end = time
            guardSleepTimes[id].append((start, end))
        elif splitted[2] == "falls":
            start = time
        else:
            print(f"ERROR: Unexpected line type in '{line}'")
            return None
    return guardSleepTimes

if __name__ == "__main__":
    # Get Data
    from aocd import get_data
    __COOKIE = "53616c7465645f5f2ae1fb21c897471d470aacfb8fa8109036f925d674714d14fc3c04392623f7d216921d91e2d7f23d"
    __YEAR = 2018
    __DAY = 4
    if(__DAY is None):
        print("Please remember to set the day.")
    else:
        DATA = get_data(__COOKIE, __DAY, __YEAR).split("\n")
        DATA.sort()
        solve(DATA)