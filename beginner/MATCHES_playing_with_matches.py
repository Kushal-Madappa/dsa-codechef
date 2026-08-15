# CodeChef: Playing with Matches (MATCHES)
# https://www.codechef.com/problems/MATCHES
m = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = str(a + b)
    print(sum(m[int(d)] for d in s))
