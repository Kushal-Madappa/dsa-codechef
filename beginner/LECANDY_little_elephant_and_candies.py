# CodeChef: Little Elephant and Candies (LECANDY)
# https://www.codechef.com/problems/LECANDY
t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if sum(a) <= c else "No")
