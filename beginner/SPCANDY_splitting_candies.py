# CodeChef: Splitting Candies (SPCANDY)
# https://www.codechef.com/problems/SPCANDY
import sys

data = sys.stdin.read().split()
t = int(data[0])
idx = 1
out = []
for _ in range(t):
    n = int(data[idx]); k = int(data[idx+1]); idx += 2
    if k == 0:
        out.append(f"0 {n}")
    else:
        out.append(f"{n // k} {n % k}")
print("\n".join(out))
