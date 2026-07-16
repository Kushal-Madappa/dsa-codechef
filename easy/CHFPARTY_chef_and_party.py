# CodeChef: Chef and Party (CHFPARTY)
# https://www.codechef.com/problems/CHFPARTY
t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    joined = 0
    for x in a:
        if x <= joined:
            joined += 1
    print(joined)
