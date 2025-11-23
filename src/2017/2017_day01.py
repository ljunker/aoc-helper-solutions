from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

def part2(data):
    length = len(data)

    # get all digits that match the next digits
    digit_pairs = [(data[i], data[(i + (length // 2)) % length]) for i in range(len(data) - 1)]
    digit_pairs.append((data[-1], data[length // 2 - 1]))
    answer = reduce(lambda x, y: int(x) + int(y),
                    list(map(lambda x: x[0], filter(lambda x: x[0] == x[1], digit_pairs))), 0)
    return answer

def part1(data):
    digit_pairs = [(data[i], data[i + 1]) for i in range(len(data) - 1)]
    digit_pairs.append((data[-1], data[0]))
    answer = reduce(lambda x, y: int(x) + int(y),
                    list(map(lambda x: x[0], filter(lambda x: x[0] == x[1], digit_pairs))), 0)
    return answer

client = AdventOfCodeClient()

# Get puzzle input (cached to .aoc_cache/2025/day01.txt)
data = client.get_input(2017, 1)

# data = "91212129"

# answer = part1(data)

# Submit part 1
# result = client.submit_answer(2017, 1, level=1, answer=answer)
#
# print(result.status, result.message)
# if result.status == SubmissionStatus.CORRECT:
#     print("🎉 Correct!")

answer = part2(data)
result = client.submit_answer(2017, 1, level=2, answer=answer)
print(result.status, result.message)
if result.status == SubmissionStatus.CORRECT:
    print("🎉 Correct!")

# tests:
assert 6 == part2("1212")
assert 0 == part2("1221")
assert 4 == part2("123425")
assert 12 == part2("123123")
assert 4 == part2("12131415")

