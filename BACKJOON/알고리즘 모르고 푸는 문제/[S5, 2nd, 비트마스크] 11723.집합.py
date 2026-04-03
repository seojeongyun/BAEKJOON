'''
    https://www.acmicpc.net/problem/11723

    1.5 / 4

    공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램 작성
        - add x: S에 x가 없는 경우 x 추가
        - remove x: S에 x가 있는 경우 제거
        - check x: S에 x가 있으면 1, 없으면 0 출력
        - toggle x: S에 x가 있으면 제거하고, 없으면 추가한다.
        - all: S를 {1, 2, .. 20}으로 바꾼다.
        - empty: S를 공집합으로 바꾼다.

    입력:
        - 수행해야되는 연산의 수 M
        - M개의 줄에 걸쳐 연산이 주어짐

    출력:
        - check 연산이 주어질 때 마다 결과 출력
'''

import sys
import heapq

# 시간 초과
if __name__ == '__main__':
    input = sys.stdin.readline

    # 집합 내 속한 1부터 20까지의 숫자를 비트의 각 자리로 매칭
    # 예를 들어 {1, 2, 5, 6}이라면 110011으로 표기하여 1,2,5,6번째에만 1을 넣어주어 집합에 포함되어 있는 수를 표현
    # 그래서 문제에서 주어진 연산은 다음과 같이 구현할 수 있다.
    # all : 1부터 20까지의 자리에 1을 넣어준다.
    # empty : 비트의 모든 자리를 0으로 만든다.
    # add : 비트의 해당 자리를 1로 만든다.
    # remove : 비트의 해당 자리를 0으로 만든다.
    # check : 비트의 해당자리가 1인지 0인지 확인한다.
    # toggle : 비트의 해당 자리 수를 바꾼다 ( 1 ->0 / 0 -> 1 )

    M = int(input().strip())
    bit = 0

    for i in range(M):
        instruction = input().strip().split()
        if instruction[0] == 'all':
            bit = (1 << 20) - 1
        elif instruction[0] == 'empty':
            bit = 0
        else:
            op = instruction[0]
            num = int(instruction[1]) - 1

            if op == 'add':
                bit |= (1 << num)
            elif op == 'remove':
                bit &= ~(1 << num)
            elif op == 'check':
                if bit & (1 << num) == 0:
                    print(0)
                else:
                    print(1)

            elif op == 'toggle':
                bit ^= (1 << num)


