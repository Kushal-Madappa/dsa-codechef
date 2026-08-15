# CodeChef: Qualify the round (QUALIFY)
# https://www.codechef.com/problems/QUALIFY
t = int(input())
for _ in range(t):
    x, a, b = map(int, input().split())
    print("Qualify" if a + 2 * b >= x else "NotQualify")
