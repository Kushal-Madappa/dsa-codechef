# CodeChef: Gregorian Calendar (FLOW015)
# https://www.codechef.com/problems/FLOW015
from datetime import date

t = int(input())
for _ in range(t):
    y = int(input())
    print(date(y, 1, 1).strftime("%A").lower())
