UserMinutes = eval(input("분에 대한 숫자를 입력하세요: "))

Hours = UserMinutes // 60
Days = Hours // 24
Years = Days // 365
RemainDays = Days % 365

print(UserMinutes, "분은 약 ", Years, "년", RemainDays, "일입니다.")