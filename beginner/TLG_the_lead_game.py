"""
CodeChef TLG — The Lead Game
Difficulty: Beginner
Topics: Simulation, Running State

Problem (summary)
-----------------
Two players play N rounds of a game. In round i, player 1 scores S1_i,
player 2 scores S2_i. The "lead" in round i is |running_total_1 -
running_total_2|, but credited to whichever player is currently ahead.
The *winner* is the player with the maximum single-round lead across
all N rounds. Print the winner (1 or 2) and that maximum lead.

Approach
--------
Maintain two running totals. After each round compute the absolute
difference, track the largest such difference and which player owned
it at that moment.

I/O
---
Single test case (no T). First line N, then N lines of "s1 s2".

Complexity
----------
Time:   O(N)
Space:  O(1)  (besides the input)
"""
from __future__ import annotations
import sys


def solve(rounds: list[tuple[int, int]]) -> tuple[int, int]:
    """Return (winner, max_lead) given the per-round scores."""
    total1 = total2 = 0
    best_lead = 0
    winner = 0
    for s1, s2 in rounds:
        total1 += s1
        total2 += s2
        lead = abs(total1 - total2)
        if lead > best_lead:
            best_lead = lead
            winner = 1 if total1 > total2 else 2
    return winner, best_lead


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    rounds = []
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        rounds.append((a, b))
    winner, lead = solve(rounds)
    sys.stdout.write(f"{winner} {lead}\n")


# ----------------------------- self-tests ---------------------------------
if __name__ == "__main__":
    # Sample from CodeChef:
    # 4
    # 140 82       -> totals (140, 82),  lead=58 to P1
    # 89 134       -> totals (229,216),  lead=13 to P1
    # 90 110       -> totals (319,326),  lead= 7 to P2
    # 112 106      -> totals (431,432),  lead= 1 to P2
    # Expected: "1 58"
    sample = [(140, 82), (89, 134), (90, 110), (112, 106)]
    assert solve(sample) == (1, 58)

    # All rounds tied -> lead stays 0, winner sentinel 0
    assert solve([(5, 5), (10, 10)]) == (0, 0)

    # Single round, P2 wins
    assert solve([(0, 7)]) == (2, 7)

    # Lead changes hands across rounds — biggest swing decides
    # R1: 10 vs  2 -> lead 8 to P1
    # R2:  1 vs 20 -> totals (11,22) -> lead 11 to P2  (largest)
    # R3: 50 vs  0 -> totals (61,22) -> lead 39 to P1  (new largest)
    assert solve([(10, 2), (1, 20), (50, 0)]) == (1, 39)

    print("All tests passed for TLG.")

    # If you'd like to run the I/O path locally:
    #   echo -e "4\n140 82\n89 134\n90 110\n112 106" | python3 TLG_the_lead_game.py
