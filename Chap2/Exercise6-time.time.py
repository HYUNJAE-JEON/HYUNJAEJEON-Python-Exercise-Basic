import time

#time.time()은 1970년 1월 1일을 00:00:00 시간으로 하여 이 시간부터 현재 시간까지 경과된 시간을 밀리초 단위로 반환한다.
#그리니치 평균시이다.
currentTime = time.time()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60

currentHours = totalHours % 24

print("현재 시간은", currentHours, ":", currentMinutes, ":", currentSeconds, "GMT입니다.")

