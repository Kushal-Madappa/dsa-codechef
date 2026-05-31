# CodeChef: Cleaning Up (CLEANUP)
# https://www.codechef.com/problems/CLEANUP
for _ in range(int(input())):
    n, m = map(int, input().split())
    done = set(map(int, input().split())) if m else set()
    rem = [i for i in range(1, n + 1) if i not in done]
    print(*rem[0::2])
    print(*rem[1::2])
