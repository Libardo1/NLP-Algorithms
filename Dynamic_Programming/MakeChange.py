def make_change(coins=[], value=0):
    """Given a list of coins, find the minimum number of coins and which ones.
    Use dynamic programming.
    
    >>> make_change([1,5, 10], 10)
    (1, [10]) # 1 coin, 10 denomination
    
    >>> make_change([1,5, 10], 15)
    (2, [10, 5]) # 2 coins, 10 and 5 in denomination
    
    >>> make_change([5, 10], 3)
    No solution possible
    """
    results = []
    if value in coins:
        return (1, [value])
 
    for coin in coins:
        if coin <= value:
            coin_tuple = make_change(coins, value - coin)          
            if isinstance(coin_tuple, tuple):
                (num_coins, coin_used) = coin_tuple
            else:
                return "Not Possible!"
            coin_used.append(coin)
            results.append((num_coins + 1, coin_used ))
    if results:
        return sorted(results, key=lambda t: t[0])[0]
    else:
        return "Not Possible!"