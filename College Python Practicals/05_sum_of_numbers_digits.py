#Finding the sum of the digits of the number
num = int(input("Enter a number : "))
s = 0
while(num > 0):
    r = num % 10
    s += r
    num = num // 10

print(s)