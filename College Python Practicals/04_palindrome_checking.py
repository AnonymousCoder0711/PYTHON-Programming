#Program for checking if given number is Palindrome or not
def check_pal(n):
    temp = n
    s = 0
    while(temp > 0):#123
        r = temp % 10 #3,2,1
        s = (s * 10) + r#3
        temp = temp // 10#12
    if s == n:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")        

n = int(input("Enter number : "))
check_pal(n)               





