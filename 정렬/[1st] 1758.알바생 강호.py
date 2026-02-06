'''
    https://www.acmicpc.net/problem/1758

    2 / 128

    커피를 받는 순서에 따라 팁을 다른 액수로 준다.
        - 팁: 원래 주려고 생각했던 돈 - (받은 등수 - 1)
        - 음수인 경우는 0원으로 간주

    순서를 적절히 바꿨을 때 받을 수 있는 팁의 최댓값

    * 사람의 수 N : <= 100,000
    * 팁: <= 100,000
'''

import sys

def calc_tip(lst):
    result = 0
    for i, tip in enumerate(lst):
        result += tip - i if tip - i > 0 else 0

    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력
    N = int(input().strip())
    for i in range(N):
        answ.append(int(input().strip()))

    # [1] 정렬
    answ.sort(key=lambda x: -1*x)

    # [2] 최댓값 출력
    print(calc_tip(answ))
