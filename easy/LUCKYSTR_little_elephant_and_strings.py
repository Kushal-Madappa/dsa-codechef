# CodeChef: Little Elephant and Strings (LUCKYSTR)
# https://www.codechef.com/problems/LUCKYSTR
k, n = map(int, input().split())
favs = [input().strip() for _ in range(k)]
for _ in range(n):
    s = input().strip()
    if len(s) >= 47 or any(f in s for f in favs):
        print("Good")
    else:
        print("Bad")
