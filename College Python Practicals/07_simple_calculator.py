#Simple calculator in python
sum = lambda a, b : a+b #1
sub = lambda a, b : a-b #2
mul = lambda a, b : a*b #3
div = lambda a, b : a/b #4


print('''
Choose one operation from: 
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit''')
a, b = 0, 0
def inp():
 global a,b   
 a, b = int(input("Enter first number : ")), int(input("Enter second number : "))
while(True):
 n = int(input("Enter your choice : "))
 if n == 1:
    inp()
    print(sum(a,b))
 elif n == 2:
    inp()
    print(sub(a,b))
 elif n == 3:
    inp()
    print(mul(a,b))
 elif n == 4:
    inp()
    print(div(a,b))
 else:
    exit(0)                