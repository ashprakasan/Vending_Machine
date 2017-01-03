def coin_change(coins, V):
    arr = []
    coin_change_arr = [[] for each in range(V + 1)]
    dp_table = [[0] * (V + 1) for i in range(len(coins))]
    for i in range(len(coins)):
        dp_table[i][0] = 1
    for i in range(V + 1):
        if coins[0] == i:
            dp_table[0][i] = 1
            coin_change_arr[i].append(coins[0])
        else:
            dp_table[0][i] = 0
    dp_table[0][0] = 1
    for i in range(1, len(coins)):
        for j in range(1, V + 1):
            if j - coins[i] >= 0:
                if dp_table[i - 1][j - coins[i]] > 0:
                    coin_change_arr[j] = coin_change_arr[j - coins[i]][:]
                    coin_change_arr[j].append(coins[i])
                    dp_table[i][j] = dp_table[i - 1][j - coins[i]] + dp_table[i - 1][j]
                else:
                    dp_table[i][j] = dp_table[i - 1][j]

    return coin_change_arr[V]



