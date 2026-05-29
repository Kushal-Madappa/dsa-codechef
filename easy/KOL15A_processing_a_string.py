# CodeChef: Processing a String (KOL15A)
# https://www.codechef.com/problems/KOL15A
t = int(input())
for _ in range(t):
    s = input()
    print(sum(int(ch) for ch in s if ch.isdigit()))
