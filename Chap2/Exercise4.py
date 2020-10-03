Seconds = eval(input("초를 입력해주세요: "))

minutes = Seconds // 60
remainingseconds = Seconds % 60

print(Seconds, "초는", minutes, "분", remainingseconds, "초입니다.")
