def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)


def factorial_while(n):
    # Initialize result to 1
    result = 1
    
    # Multiply result by each number from n down to 1
    while n > 0:
        result = result * n
        n = n - 1
    
    return result

# Test both versions
print(factorial(5))        # Recursive version: 120
print(factorial_while(5))  # While loop version: 120




# bot = factorial(5) # Output: 120
# print(bot)
i = 0 
def m1():
    global i 
    while i < 998:
        print("krish is a bot "+ str(i))
        i = i + 1 
        m1()# ← Calls itself again... forever!


m1()
