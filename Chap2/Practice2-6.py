Number = eval(input("0과 1000 사이의 숫자를 입력하세요: "))

Numberofthirdplace = Number // 100
NumberofSecondplace = (Number - Numberofthirdplace * 100) // 10
Numberoffirstplace = (Number - Numberofthirdplace * 100 - NumberofSecondplace * 10) % 10

SumofNumber = Numberofthirdplace + NumberofSecondplace + Numberoffirstplace

print("각 자릿수의 합은 ", SumofNumber, "입니다.")