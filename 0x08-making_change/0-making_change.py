#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    arr = [total + 1] * (total  + 1)
    arr[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                value = amount - coin
                low = min(arr[amount - coin] + 1, total + 1)
                arr[amount] = low

    return -1 if arr[total] > total else arr[total]
