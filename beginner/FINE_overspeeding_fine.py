# CodeChef: Overspeeding Fine (FINE)
# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FINE
for _ in range(int(input())):
    x = int(input())
    if x <= 70:
        print(0)
    elif x <= 100:
        print(500)
    else:
        print(2000)
