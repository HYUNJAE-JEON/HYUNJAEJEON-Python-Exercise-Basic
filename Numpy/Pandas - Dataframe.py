import pandas as pd
import plotly.express as px


fruit_df = pd.DataFrame(
    columns=['농장', '당도' , '수분함유량', '등급(정답)'],

    data=[['농장A', 35.2, 16.3, '1등급'],
          ['농장A', 16.9, 6.5, '3등급'],
          ['농장B', 18.4, 44.5, '1등급'],
          ['농장C', 27.4, 18.1, '2등급'],
          ['농장D', 24.0, 25.2, '2등급']]
)

print (fruit_df.head())
#fruit_df.head()로만 출력하면 제대로 안되어서 print를 붙여주면 안전하게 출력이 가능하다.

from copy import deepcopy

farm_map = {'농장A':0, '농장B':1, '농장C':2, '농장D':3}
rating_map = {'1등급':0, '2등급':1, '3등급':2}

new_fruit_df = deepcopy(fruit_df)
new_fruit_df['농장'] = fruit_df['농장'].map(farm_map)
new_fruit_df['등급(정답)'] = fruit_df['등급(정답)'].map(rating_map)

print(new_fruit_df.head(10))

from matplotlib import pyplot as plt

def get_fruit(idx):
    return [0, new_fruit_df['당도'][idx]], [0, new_fruit_df['수분함유량'][idx]]

colors = ['r', 'g', 'b']
plt.plot(*get_fruit(0), label='fruit_0')
plt.plot(*get_fruit(1), label='fruit_1')
plt.plot(*get_fruit(2), label='fruit_2')
plt.plot(*get_fruit(3), label='fruit_3')
plt.plot(*get_fruit(4), label='fruit_4')

plt.grid(True)
plt.xlabel('sugar')
plt.ylabel('moisture')
plt.title('Fruit Figure')
plt.legend()
#그래프의 구분을 주기 위한 라벨명 출력
plt.show()
plt.close()
