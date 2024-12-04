def part1(filePath):
    reports = []
    with open(filePath, "r") as file:
        for line in file.readlines():
            reports.append(line.strip())

    return reports
        

def part2(filePath):
    pass

print(f"part 1 answer: {part1("C:\\Users\\nikol\\Desktop\\aoc24\\day02\\example.txt")}")
print(f"part 2 answer: {part2("C:\\Users\\nikol\\Desktop\\aoc24\\day02\\data.txt")}")