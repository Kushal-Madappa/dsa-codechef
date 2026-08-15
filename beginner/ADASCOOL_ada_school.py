# CodeChef: Ada School (ADASCOOL)
# https://www.codechef.com/problems/ADASCOOL
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if (n * m) % 2 == 0 else "NO")
