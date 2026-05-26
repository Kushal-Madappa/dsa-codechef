# CodeChef: Tanu and Head-bob (HEADBOB)
# https://www.codechef.com/problems/HEADBOB
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if 'I' in s:
        print("INDIAN")
    elif 'Y' in s:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
