def sum_even_fibonacci(limit):
    a, b = 0, 1
    even_sum = 0

    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b

    return even_sum

limit = 4000000
print("Sum of even-valued Fibonacci terms up to", limit, "is:", sum_even_fibonacci(limit))
