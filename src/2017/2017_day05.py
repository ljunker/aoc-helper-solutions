from functools import reduce

from src.aocfw import AdventOfCodeClient, SubmissionStatus

DAY = 5


def part2(data):
    program = [int(x) for x in (data.split("\n"))]
    current = 0
    instr = program[current]
    steps = 0
    while not_outside(program, current):
        old_pos = current
        instr = program[current]
        program[old_pos] += -1 if instr >= 3 else 1
        current += instr
        steps += 1
    return steps


def part1(data):
    program = [int(x) for x in (data.split("\n"))]
    current = 0
    instr = program[current]
    steps = 0
    while not_outside(program, current):
        old_pos = current
        instr = program[current]
        program[old_pos] = program[old_pos] + 1
        current += instr
        steps += 1
    return steps


def not_outside(program, position):
    return 0 <= position < len(program)


if __name__ == "__main__":
    client = AdventOfCodeClient()
    data = client.get_input(2017, DAY)
#     data = """0
# 3
# 0
# 1
# -3"""

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
