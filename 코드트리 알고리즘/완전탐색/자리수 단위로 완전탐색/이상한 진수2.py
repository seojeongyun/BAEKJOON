'''
    0 이상의 정수 N을 2진법으로 나타냅니다. 이 표현에서 정확히 한 자리의 숫자만 바꾸어 만든 문자열 a가 주어집니다. 가능한 정수 N 중 최댓값을 찾는 프로그램을 작성해보세요.

    첫번째 줄에 문자열 a가 주어진다.

    TC1
    입력 1010
    출력 14
'''

# 0이상의 정수 N을 2진법으로 나타낸다.
# 여기서 한 자리 숫자만 바꿔 만든 문자열 a가 주어짐
# 가능한 정수 N중 최댓값을 찾는 프로그램

import sys

input = sys.stdin.readline

vector = list(map(int, input().strip()))

answer = -sys.maxsize

for i in range(len(vector)):
    sum = 0
    #
    vector_cpy = vector[::]
    vector_cpy[i] = vector[i] ^ 1

    for i in range(len(vector_cpy) - 1, -1, -1):
        if vector_cpy[i] == 1:
            sum += 1 << (len(vector_cpy) - i - 1)

    answer = max(answer, sum)
print(answer)

# 0을 1로 바꾸는 전략을 쓰면 쉽게 해결될듯 하지만, 0이 입력으로 주어지지 않는 경우에 대해서도 생각해봐야함
# 이런 경우 완전 탐색이 좋을 수 있음.