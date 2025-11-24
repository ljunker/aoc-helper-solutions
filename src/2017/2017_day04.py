from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY=4

def part2(data):
    sum = 0
    rows = data.splitlines()
    for row in rows:
        words = row.split()
        set_words = set()
        for word in words:
            set_words.add(''.join(sorted(list(word))))
        sum += 1 if len(words) == len(set_words) else 0
    return sum

def part1(data):
    rows = data.split("\n")
    sum = 0
    for row in rows:
        words = row.split()
        set_words = set(words)
        sum += 1 if len(words) == len(set_words) else 0
    return sum

if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)
#     data = """abcde fghij
# abcde xyz ecdab
# a ab abc abd abf abj
# iiii oiii ooii oooi oooo
# oiii ioii iioi iiio"""

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

