filePath = "C:\\Users\\nikol\\Desktop\\aoc24\\day01\\data.txt"

def part1(fp):
    distance = 0
    l1 = []
    l2 = []

    with open(fp, "r") as file:
        for line in file.readlines():
            pair = (line.strip()).split()
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))
        distance = sum([abs(x - y) for x, y in zip(sorted(l1),sorted(l2))])
        
    return distance

print(part1(filePath))