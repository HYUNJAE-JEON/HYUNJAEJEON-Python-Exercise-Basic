numberlist = []
num = eval(input("숫자를 입력하세요(0은 입력 종료): "))
numberlist.append(num)
while num != 0:
    num = eval(input("숫자를 입력하세요(0은 입력 종료): "))
    numberlist.append(num)
numberlist.sort(reverse=True)
maxnumber = numberlist[0]
countmaxnumber = numberlist.count(maxnumber)
print("가장 큰 수는 ",maxnumber,"입니다.")
print("가장 큰 수가 나타난 빈도수는", countmaxnumber, "번입니다.")






# elif Num == 0:
#     print("가장 큰 수는 ",)