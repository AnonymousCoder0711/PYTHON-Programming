#Program for reversing the string
s = input("enter string : ")
list1 = list(s)
list1.reverse()
s = ""
for v in list1:
    s += v
print(s)