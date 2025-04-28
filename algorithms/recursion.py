def sum(n):
    # base case
    if n == 0:
        return 0
    # body + recursive call
    return n + sum(n - 1)