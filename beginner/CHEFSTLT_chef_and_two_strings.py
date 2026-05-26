# CodeChef: Chef and Two Strings (CHEFSTLT)
# https://www.codechef.com/problems/CHEFSTLT

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    mn = mx = 0
    for a, b in zip(s1, s2):
        if a == '?' or b == '?':
            mx += 1            # always free to make them differ
        else:
            if a != b:
                mn += 1
                mx += 1
    print(mn, mx)
