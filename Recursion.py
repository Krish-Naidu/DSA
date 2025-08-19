def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

bot = factorial(5) # Output: 120
print(bot)