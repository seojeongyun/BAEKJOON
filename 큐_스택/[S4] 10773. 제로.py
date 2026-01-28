'''
    입력으로 0이 들어오면 쓴 수를 지운다.

    출력: 받아 적은 수의 합
'''

# [알고리즘]
# LIFO 구조이므로 STACK 사용

# [시간복잡도]
# Stack의 pop은 O(1)
# 입력 K에 따라서 반복 수가 달라지므로 O(K)



# [0] 입력
K = int(input())

# [1] stack 선언
STK = []

# [2] K개 줄에 정수 한 개 씩 주어짐
for i in range(K):
    num = int(input())
    if num == 0:    # [3] 0이 들어오면 가장 최근에 쓴 수를 지운다.
        STK.pop()
    else:   # 0은 append되면 안됨.
        STK.append(num)

# [3] 출력
print(sum(STK))
