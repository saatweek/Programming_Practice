# The Question

# Write a program that takes a single line of input, representing an arithmetic expression. The expression will consist
# of numeric digits (0-9), the plus operator (+) and the multiplication operator (*). The given expression will be a
# valid arithmetic expression (i.e., "*2++" is not valid).
#
# Your task is to evaluate the arithmetic expression, following the normal rules of operator precedence, and print the
# result without any leading or trailing whitespace.
#
# The resulting number will fit in a normal integer.
#
# Note: Solutions such as "eval()" in python are elegant, but not what we are looking for here. Please evaluate the
# expressions with your own code :)

def get_expr(expression):
    expr = []
    num = 0
    for i in expression:
        if (i != "+") and (i != "*"):
            num = (num * 10) + int(i)
        elif (i == "+") or (i == "*"):
            expr.append(num)
            expr.append(i)
            num = 0

    expr.append(num)

    return expr


def evaluate_expr(expr):
    for i, n in enumerate(expr):
        if n == "*":
            prod = expr[i - 1] * expr[i + 1]
            expr.pop(i + 1)
            expr.pop(i)
            expr[i - 1] = prod

    final_sum = 0
    for i, n in enumerate(expr):
        if n != "+":
            final_sum += n

    print(final_sum)


if __name__ == "__main__":
    expression = input("Input an Arithmetic Expression : ")
    expr = get_expr(expression)
    evaluate_expr(expr)
