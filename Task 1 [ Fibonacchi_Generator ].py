                                                                # Fibonacchi_Generator

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Accept input from the user
n = int(input("\nEnter The Number Of Fibonacci Numbers To Generate: "))
fib = fibonacci_generator()
fib_list = []

for _ in range(n):
    fib_list.append(next(fib))

print("\nNumber Of First ",n,"Fibonacci Numbers Is : ", fib_list)
print("")
