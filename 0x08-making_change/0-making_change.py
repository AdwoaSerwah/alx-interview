#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        # Use as many of this coin as possible
        count += total // coin
        total %= coin

    # If total is not zero, return -1 (not possible to meet the total)
    return count if total == 0 else -1
