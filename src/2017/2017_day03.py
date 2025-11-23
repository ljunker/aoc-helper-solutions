from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY=3

def part2(data):
    # https://oeis.org/A141481
    return 0

def part1(data):
    # find closest square
    n = 1
    while n*n < data:
        n += 2
    n2 = n*n
    dist = n2 - data
    arms = dist // (n-1)
    arms_rest = dist % (n-1)

    x = (n-1)//2
    y = abs((n-1)//2 - arms_rest)
    return x + y

if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)
    data = int(data)
    # data = 20

    answer = part1(data)
    print(answer)
    result = client.submit_answer(2017, DAY, level=1, answer=answer)
    print(result.status, result.message)
    if result.status == SubmissionStatus.CORRECT:
        print("🎉 Part 1 Correct!")
    #
    # answer = part2(data)
    # result = client.submit_answer(2017, DAY, level=2, answer=answer)
    # print(result.status, result.message)
    # if result.status == SubmissionStatus.CORRECT:
    #     print("🎉 Part 2 Correct!")

