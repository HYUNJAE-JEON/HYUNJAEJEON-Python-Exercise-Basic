countofrows = eval(input("행의 개수를 입력해주세요: "))
#
# for i in range(countofrows):
#     for j in range(countofrows // 2):
#         print(" ")
#
#
#
# print(format(59832, "10d"))
# print(format(59832, "<10d"))
#
# for i in range(0,2*countofrows,-2):
#     2*countofrows
#     print("{0^")

# for x in range(1, countofrows+1):
#     print(end="")
#     for y in range(1, x+1):
#         y = str(y)
#         print(y.ljust(countofrows+1))

# for i in range(1, countofrows+1):
#     for j in range(1,i):
#         print(' '*(countofrows-i), print(j))
#
for i in range(1,countofrows+1):
    x = countofrows
    print(end=" ")
    for j in range(1,i):
        print(str(j), end="")
    print()


# n = int(input())
# for i in range(1, n+1):
#     for j in range(0, i):
#         print('*', end='')
#     print()
# for i in range(n-1, 0, -1):
#     for j in range(0, i):
#         print('*', end='')
#     print()