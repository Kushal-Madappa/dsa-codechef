# CodeChef: Bytelandian Gold Coins (COINS)
# https://www.codechef.com/problems/COINS
import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def best(n):
    if n < 12:
        return n
    return max(n, best(n // 2) + best(n // 3) + best(n // 4))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(best(int(line)))
