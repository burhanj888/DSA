
def factorial(n):
    fact = 0
    if n <= 1:
        fact = 1
        print(fact)
        return fact
    fact = n * factorial(n-1)
    print(fact)
    return fact

factorial(4)
