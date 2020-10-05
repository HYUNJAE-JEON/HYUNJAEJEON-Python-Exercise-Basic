
#matplotlib는 파이썬에서 데이터를 차트나 플롯으로 그려주는 라이브러리 패키지로서 가장 많이 사용되는 데이터 시각화 패키지
#plt.plot은 라인 플롯을 그리는 함수
from matplotlib import pyplot as plt

plt.plot([x for x in range(0, 10)], [x-2 for x in range(0,10)], label='y=x+3')
plt.plot([x for x in range(0, 10)], [x*6 for x in range(0,10)], label='y=2x')
plt.legend(loc='lower right')
plt.show()
plt.close()

plt.plot([x for x in range(-10, 11)], [x**2 +3 for x in range(-10, 11)], label = 'y = x^2')
plt.legend(loc = 'lower right')
plt.show()
plt.close()