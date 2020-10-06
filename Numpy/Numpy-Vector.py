import numpy as np

vec_x = [35.2, 16.3]

npvec_x = np.array(vec_x)
print(npvec_x)

npvec_v = np.array([1,2])
npvec_w = np.array([3,-1])
npvec_addition = npvec_v + npvec_w

print(npvec_addition)

scalar = 2

npvec_multiplication = npvec_v * scalar

print(npvec_multiplication)

#선형대수에서 다루는 시스템인 직선이 선형성을 유지해야하기 때문에 벡터 합과 스칼라 곱이 중요하다.

vec_a =np.array([2,1])
vec_b =np.array([3,2])

print(vec_a @ vec_b)

vec_c = np.array([[1],
                 [-2]])
print(vec_c.shape)

matrix_a = np.array([[1,1],
                     [-2,0]])
matrix_b = np.array([[1,1],
                     [2,3]])
print(matrix_a + matrix_b)

print(matrix_a * matrix_b)


