# CodeChef: Little Elephant and Permutations (LEPERMUT)
# https://www.codechef.com/problems/LEPERMUT
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    good = True
    max_so_far = a[0] if n > 0 else 0
    for j in range(2, n):
        if max_so_far > a[j]:
            good = False
            break
        if a[j - 1] > max_so_far:
            max_so_far = a[j - 1]
    print("YES" if good else "NO")
