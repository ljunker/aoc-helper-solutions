from collections import defaultdict
from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY=6

def part2(data):
    configs = []
    membanks = [int(x) for x in data.split()]
    conf = str(membanks)
    configs.append(conf)
    while True:
        # make step
        max_bank = max(membanks)
        # if max_bank < len(membanks):
        current = membanks.index(max_bank)
        membanks[current] = 0
        while max_bank > 0:
            current = (current + 1) % len(membanks)
            membanks[current] += 1
            max_bank -= 1

        conf = str(membanks)
        if conf in configs:
            return len(configs) - configs.index(conf)
        configs.append(conf)

def part1(data):
    configs = []
    membanks = [int(x) for x in data.split()]
    conf = str(membanks)
    configs.append(conf)
    while True:
        # make step
        max_bank = max(membanks)
        # if max_bank < len(membanks):
        current = membanks.index(max_bank)
        membanks[current] = 0
        while max_bank > 0:
            current = (current + 1) % len(membanks)
            membanks[current] += 1
            max_bank -= 1

        conf = str(membanks)
        if conf in configs:
            return len(configs)
        configs.append(conf)

if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)

    # data = "0 2 7 0"

    answer = part1(data)
    print(answer)
    result = client.submit_answer(2017, DAY, level=1, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 1 Correct!")

    answer = part2(data)
    print(answer)
    result = client.submit_answer(2017, DAY, level=2, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 2 Correct!")

