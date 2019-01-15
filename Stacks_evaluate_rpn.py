




def evaluate(expression):
    intermediate_result = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }



    for token in expression.split(DELIMITER):
        print(token)
        if token in OPERATORS:
            intermediate_result.append(OPERATORS[token](intermediate_result.pop(), intermediate_result.pop()))
            #print(token)
        else: # token is a number.
            intermediate_result.append(int(token))


    return intermediate_result[-1]


input = "3,4,+,5,*"

print(evaluate(input))

