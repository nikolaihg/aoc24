filePath = "C:\\Users\\nikol\\Desktop\\aoc24\\day01\\data.txt"

def part1(fp):
    l1 = []
    l2 = []

    with open(fp, "r") as file:
        for line in file.readlines():
            pair = (line.strip()).split()
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))
    
    distance = sum([abs(x - y) for x, y in zip(sorted(l1),sorted(l2))])

    return distance

def part2(fp):
    l1 = []
    l2 = []

    with open(fp, "r") as file:
        for line in file.readlines():
            pair = (line.strip()).split()
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))

    similarityScore = (sum([(l1.count(x) * x) for x in l2]))
    return similarityScore

print(f"part 1 answer: {part1(filePath)}")
print(f"part 2 answer: {part2(filePath)}")