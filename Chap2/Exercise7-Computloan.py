annualInterestRate = eval(input("연이율을 입력하세요(예. 7.25): "))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("상환년수를 입력하세요(예.5): "))
loanAmount = eval(input("대출금을 입력하세요(예.120000950): "))

# 실수 나눗셈은 / 입니다. 정수 나눗셈은 // 입니다.
Ammountofmonthlyrepayment = loanAmount * monthlyInterestRate / (1- 1 / (1+monthlyInterestRate)**(numberOfYears*12))
Ammountoftotalrepayment = Ammountofmonthlyrepayment * numberOfYears * 12

print("월상환액은 ", int(Ammountofmonthlyrepayment*100)/100 , "이고 총상환액은 ", int(Ammountoftotalrepayment*100)/100, "입니다." )

