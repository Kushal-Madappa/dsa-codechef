# CodeChef: Chef and Feedback (ERROR)
# https://www.codechef.com/problems/ERROR
t = int(input())
for _ in range(t):
    s = input()
    print("Good" if "010" in s or "101" in s else "Bad")
