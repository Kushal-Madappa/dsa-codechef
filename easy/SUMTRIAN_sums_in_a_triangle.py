# CodeChef: Sums in a Triangle (SUMTRIAN)
# https://www.codechef.com/problems/SUMTRIAN
# Bottom-up DP: replace each cell with itself + max of its two children.
# Answer is the top cell after one full pass.

t = int(input())
for _ in range(t):
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])
    print(tri[0][0])
