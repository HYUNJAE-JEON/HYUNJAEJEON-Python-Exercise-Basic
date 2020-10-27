# countofrows = eval(input("행의 개수를 입력해주세요: "))
#
# for i in range(1,countofrows+1):
#     for j in range(countofrows-i,0,-1):
#         print("    "),
#     for j in range(i,0,-1):
#         print(format(j, "4d")),
#     for j in range(2, i+1):
#         print(format(j,"4d")),
#     print()
#
#
num = eval(input("1부터 15까지의 숫자를 입력해주세요: "))


space = " "

if num <= 15:

    for i in range(1, num+1):
        for num_of_spaces in range(i+1, 1, -num):
            x = (i-1)
            if i <= 9:
                spaces = space*(num-x+7)
            if (i >9) and (i <=15):
                spaces = space * (num - x-(i%9)+7)
            print(spaces, end="")
        for inv_rec in range(i, 1, -1):
            print(inv_rec,end="")
        for rec in range(1, i+1):
            print(rec, end="")
        print("")


else:
    print("15 이하의 숫자를 입력해주세요!")