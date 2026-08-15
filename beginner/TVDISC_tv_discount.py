# CodeChef: TV Discount (TVDISC)
# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TVDISC
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    p1, p2 = a - c, b - d
    if p1 < p2:
        print("First")
    elif p2 < p1:
        print("Second")
    else:
        print("Any")
