n = int(input("Enter number of rows : "))
pascal_list = []

for i in range(n):
    temp_list = []
    for j in range(i+1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
    pascal_list.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2"),end="")
    for j in range(i+1):
        print(format(pascal_list[i][j],"<3"),end=" " )
    print()                        