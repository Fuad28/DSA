"""
1. Recursion uses stack memory which uses the Last In first out principle: LIFO
2. Any problem that can be solved using recursion can be solved iteratively.
3. Recursion comes with time and space overheads due to its utilization of stack memory.
4. Point 3 above are exactly where iteration beats recursion. While recursion wins when it comes to ease of writing code.
5. Recursion steps
    a. Recursive case - the flow
    b. base case - the stopping criteria
    c. unintentional case - the constraint (more like handling errors) 
"""


#1
# def firstMethod():
#     secondMethod()
#     print("I am the first Method")

# def secondMethod():
#     thirdMethod()
#     print("I am the second Method")

# def thirdMethod():
#     fourthMethod()
#     print("I am the third Method")

# def fourthMethod():
#     print("I am the fourth Method")


# firstMethod()

#2
# def recursiveMethod(n):
#     if n < 1: print("n is less than 1")
#     else:
#         recursiveMethod(n-1)
#         print(n)
    
# recursiveMethod(5)


#3
# def factorial(n):
#     assert n >= 0 and type(n) == int, "Factorial can only be evaluated for positive integers"
#     if n in [0, 1]: return 1
#     else: return n * factorial(n - 1)

# print(factorial(-10))

#4
def fibonacci(n):
    """returns nth fibonacci number"""
    assert n >= 1 and type(n) == int, "Fibonacci can only be evaluated for positive integers"

    if n in [1, 2]: return n - 1
    return fibonacci(n - 1) + fibonacci (n - 2)

print(fibonacci(7))