
list1 = [122, 110, 320, 550, 130, 600, 120, 160, 240]

def buy_and_sell_stock_once(prices):

    min_price_so_far, max_profit = float('inf'), 0.0

    for price in prices:

        max_profit_sell_today = price - min_price_so_far

        max_profit = max(max_profit, max_profit_sell_today)

        min_price_so_far = min(min_price_so_far, price)

    return max_profit


result = buy_and_sell_stock_once(list1)


print(result)
