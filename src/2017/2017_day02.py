import itertools
from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY=2

def part2(data):
    rows = data.split("\n")
    sum = 0
    for row in rows:
        cols = sorted([int(x) for x in row.split()], reverse=True)
        combis = list(itertools.combinations(cols, 2))
        for comb in combis:
            sum += comb[0] // comb[1] if comb[0] % comb[1] == 0 else 0
    return sum

def part1(data):
    rows = data.split("\n")
    sum = 0
    for row in rows:
        cols = sorted([int(x) for x in row.split()])
        sum += cols[-1] - cols[0]
    return sum

if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)
#     data = """5 9 2 8
# 9 4 7 3
# 3 8 6 5"""

    # answer = part1(data)
    # print(answer)
    # result = client.submit_answer(2017, DAY, level=1, answer=answer)
    # print(result.status, result.message)
    # if result.status == SubmissionStatus.CORRECT:
    #     print("🎉 Part 1 Correct!")

    answer = part2(data)
    print(answer)
    result = client.submit_answer(2017, DAY, level=2, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 2 Correct!")

