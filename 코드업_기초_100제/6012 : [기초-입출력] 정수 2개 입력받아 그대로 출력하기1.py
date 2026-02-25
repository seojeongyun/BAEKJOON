'''
줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자
'''

a = list(int(input()) for _ in range(2))
# 두 줄에 걸쳐 입력받는 것. 1 2 처럼 한 번에 입력주면 안됨

for i in range(2):
    print(a[i])
# print(a[i] for i in range(2)) 처럼 하면 안됨. 객체만 반환됨.
