from src.aocfw import AdventOfCodeClient

client = AdventOfCodeClient()

board = client.get_leaderboard(2025, 4254161)
for member_id in board.get('members'):
    member = board.get('members').get(member_id)
    print(f"{str(member.get('local_score')).zfill(3)}: {member.get('name')}")