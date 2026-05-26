# CodeChef: Ciel and A-B Problem (CIELAB)
# https://www.codechef.com/problems/CIELAB
# Print any positive integer with the same digit-count as A-B and exactly
# one digit different. Trick: just tweak the last digit by +/- 1.
#  - if last digit < 9: c + 1 (last digit changes, no carry, digit-count preserved)
#  - if last digit = 9: c - 1 (e.g. 4629 -> 4628; avoids overflow into a new digit)

a, b = map(int, input().split())
c = a - b
print(c - 1 if c % 10 == 9 else c + 1)
