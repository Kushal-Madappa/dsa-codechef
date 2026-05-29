# CodeChef: Laddu (LADDU)
# https://www.codechef.com/problems/LADDU
t = int(input())
for _ in range(t):
    m, origin = input().split()
    m = int(m)
    total = 0
    for _ in range(m):
        parts = input().split()
        act = parts[0]
        if act == "CONTEST_WON":
            rank = int(parts[1])
            total += 300 + max(20 - rank, 0)
        elif act == "TOP_CONTRIBUTOR":
            total += 300
        elif act == "BUG_FOUND":
            total += int(parts[1])
        elif act == "CONTEST_HOSTED":
            total += 50
    per = 200 if origin == "INDIAN" else 400
    print(total // per)
