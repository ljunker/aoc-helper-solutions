from src.aocfw import AdventOfCodeClient, SubmissionStatus

def part1(part_data):
    return len(part_data)

def part2(part_data):
    return len(part_data)

client = AdventOfCodeClient()

data = client.get_input(2025, 1)

# data = "91212129"

answer = part1(data)

# Submit part 1
result = client.submit_answer(2025, 1, level=1, answer=answer)

print(result.status, result.message)
if result.status == SubmissionStatus.CORRECT:
    print("🎉 Correct!")

answer = part2(data)
result = client.submit_answer(2025, 1, level=2, answer=answer)
print(result.status, result.message)
if result.status == SubmissionStatus.CORRECT:
    print("🎉 Correct!")