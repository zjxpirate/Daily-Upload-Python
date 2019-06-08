

# 7. compute the binomial coefficient

def compute_binomial_coefficient(n, k):

    def compute_x_choose_y(x, y):

        if y in (0, x):
            return 1

        if x_choose_y[x][y] == 0:
            without_y = compute_x_choose_y(x - 1, y)
            with_y = compute_x_choose_y(x - 1, y - 1)
            x_choose_y[x][y] = without_y + with_y

        return x_choose_y[x][y]
    
    x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]
    return compute_x_choose_y(n, k)


print(compute_binomial_coefficient(6, 2))

