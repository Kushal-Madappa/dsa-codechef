# CodeChef: Valid Triangles (FLOW013)
# https://www.codechef.com/problems/FLOW013
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print("YES" if a + b + c == 180 and a > 0 and b > 0 and c > 0 else "NO")
