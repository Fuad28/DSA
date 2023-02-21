# #1
# def sum_of_digits(n):
#     assert n >= 0 and type(n) == int, "n can only be a positive integer"

#     if n < 10: return n
#     else: return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(-4))

#2
# def power(base, exp):
#     """returns base**n"""

#     assert exp >= 0 and type(exp) == int, "n can only be a positive integer"

#     if exp == 1: return base
#     else: return base * power(base, exp - 1)

# print(power(-3.2, 4))

#3
# def gcd(num1, num2):
# #     """returns greatest common divisor between two numbers using the euclidean algorithm"""

#     assert type(num1) == int, "paramters can only be integers"
#     assert type(num2) == int, "paramters can only be integers"

#     num1, num2= abs(num1), abs(num2)

#     if num2 == 0: return num1
#     else: return gcd(num2, num1%num2)

# print(gcd(12, 8))

#4
# def dec_to_bin(dec):
#     assert dec >= 0 and type(dec) == int, "dec can only be a positive integer"

#     if dec == 1: return "1"
#     return dec_to_bin(dec//2) + str(dec%2)


# print(dec_to_bin(-13))

def f(n):
    if n <= 1: return n
    else: return f(n - 1) + f(n - 1)

print(f(4))