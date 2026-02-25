'''
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
'''

A = list(map(int, input().split()))
# B = [map(int, input().split())]
for i in range(len(A)):
    print(A[i])

'''
공백을 두고 입력된 정수를 입력받을 때

1. 여러 변수에 입력받는 경우
    -> A, B = map(int, input().split())

2.하나의 변수에 list로 저장하는 경우
    -> A = list(map(int, input().split()))
'''