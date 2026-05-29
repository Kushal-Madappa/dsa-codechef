# CodeChef: Ambiguous Permutations (PERMUT2)
# https://www.codechef.com/problems/PERMUT2
while True:
    n = int(input())
    if n == 0:
        break
    p = list(map(int, input().split()))
    # ambiguous iff p[p[i]-1] == i+1 for all i (0-indexed)
    ok = all(p[p[i] - 1] == i + 1 for i in range(n))
    print("ambiguous" if ok else "not ambiguous")
