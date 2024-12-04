def part1(filePath):
    l1 = []
    l2 = []

    with open(filePath, "r") as file:
        for line in file.readlines():
            pair = (line.strip()).split()
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))
    
    distance = sum([abs(x - y) for x, y in zip(sorted(l1),sorted(l2))])

    return distance

def part2(filePath):
    l1 = []
    l2 = []

    with open(filePath, "r") as file:
        for line in file.readlines():
            pair = (line.strip()).split()
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))

    similarityScore = (sum([(l1.count(x) * x) for x in l2]))
    return similarityScore

print(f"part 1 answer: {part1("C:\\Users\\nikol\\Desktop\\aoc24\\day01\\data.txt")}")
print(f"part 2 answer: {part2("C:\\Users\\nikol\\Desktop\\aoc24\\day01\\data.txt")}")