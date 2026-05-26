# CodeChef: Turbo Sort (TSORT)
# https://www.codechef.com/problems/TSORT
import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
nums = list(map(int, data[1:1 + n]))
nums.sort()
sys.stdout.write("\n".join(map(str, nums)))
