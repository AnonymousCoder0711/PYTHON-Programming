#Printing Fibonacci series using generator

def generator_function(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

n = int(input("Enter number of values of fibbonacci series : "))
for value in generator_function(n):
    print(value,end=' ')  