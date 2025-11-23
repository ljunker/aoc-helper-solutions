from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY=0

def part2(data):
    return 0

def part1(data):
    return 0

if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)

    answer = part1(data)
    result = client.submit_answer(2017, DAY, level=1, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 1 Correct!")

    answer = part2(data)
    result = client.submit_answer(2017, DAY, level=2, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 2 Correct!")

