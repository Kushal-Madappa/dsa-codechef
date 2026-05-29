# CodeChef: That Is My Score! (WATSCORE)
# https://www.codechef.com/problems/WATSCORE
t = int(input())
for _ in range(t):
    n = int(input())
    mx = [0] * 12  # indices 1..11
    for _ in range(n):
        p, s = map(int, input().split())
        if s > mx[p]:
            mx[p] = s
    print(sum(mx[1:9]))
