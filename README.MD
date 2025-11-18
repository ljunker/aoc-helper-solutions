# Advent of Code with Helper (aocfw)

Tiny helper framework for Advent of Code.

## Setup

1. Install dependencies:
```bash
uv add requests
```
2. Get you AoC session cookie:
   * Log into https://adventofcode.com
   * Open browser dev tools -> Storage/Cookies
   * Copy the value of the `session` cookie
3. Set it as env variable:
```bash
export AOC_SESION="your session cookie here"
```

## Python usage:
```python
from aocfw import AdventOfCodeClient, SubmissionStatus

client = AdventOfCodeClient()

# Get puzzle input (cached to .aoc_cache/2025/day01.txt)
data = client.get_input(2025, 1)

# Solve...
answer = 42

# Submit part 1
result = client.submit_answer(2025, 1, level=1, answer=answer)

print(result.status, result.message)
if result.status == SubmissionStatus.CORRECT:
    print("🎉 Correct!")
```