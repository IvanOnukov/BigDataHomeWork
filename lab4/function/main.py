from datetime import datetime as time


# task 1 function
def calcul(operator, a, b=2):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "%":
        return a / 100
    elif operator == "*":
        return a * b
    elif operator == "**":
        return a ** b


if __name__ == '__main__':
    print(calcul("+", 1, 9))
    print(calcul("%", 100))
    print(calcul("**", 4))
    print(calcul("**", 9, 3))
