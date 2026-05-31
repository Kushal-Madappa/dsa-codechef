# CodeChef: Chef and his Daily Routine (CHEFROUT)
# https://www.codechef.com/problems/CHEFROUT
t = int(input())
for _ in range(t):
    s = input().strip()
    bad = any(b in s for b in ("EC", "SE", "SC"))
    print("no" if bad else "yes")
