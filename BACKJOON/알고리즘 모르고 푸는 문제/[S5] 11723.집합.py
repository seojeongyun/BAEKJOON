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
    answ = []

    # [0] 입력
    M = int(input().strip())
    S = set()

    #  remove  toggle  empty
    for _ in range(M):
        instruction = input().strip()
        # check
        if instruction[0] == 'c':
            if int(instruction[-2:]) in S:
                # answ.append(1)
                print(1)
            else:
                # answ.append(0)
                print(0)

        if instruction[0] == 'a':
            # add x
            if len(instruction) > 3:
                if int(instruction[-2:]) not in S:
                    S.add(int(instruction[-2:]))
            # all
            else:
                S = set(range(1,21))

        # remove
        if instruction[0] == 'r':
            if int(instruction[-2:]) in S:
                S.remove(int(instruction[-2:]))

        # toggle
        if instruction[0] == 't':
            if int(instruction[-2:]) in S:
                S.remove(int(instruction[-2:]))
            else:
                S.add(int(instruction[-2:]))

        if instruction[0] == 'e':
            S = set()

    # for a in answ:
    #     print(a)
# if __name__ == '__main__':
#     M = int(input().strip())
#     instructions = [input().strip() for _ in range(M)]
#
#     heap = heapq.heapify([])
#
#     for inst in instructions:
#         # check
#         if inst[0] == 'c':
#             if int(inst[-2:]) in S:
#                 print(1)
#             else:
#                 print(0)
#
#         if inst[0] == 'a':
#             # add x
#             if len(inst) > 3:
#                 if int(inst[-2:]) not in S:
#                     heapq.heappush(heap, int(inst[-2:]))
#             # all
#             else:
#                 heap = heapq.heapify([range(1,21)])
#
#         # remove
#         if inst[0] == 'r':
#             if int(inst[-2:]) in S:
#                 heapq.heappop(heap, int(inst[-2:]))
#                 # S.remove(int(inst[-2:]))
#
#         # toggle
#         if inst[0] == 't':
#             if int(inst[-2:]) in S:
#                 heapq.heappop(heap, int(inst[-2:]))
#             else:
#                 heapq.heappush(heap, int(inst[-2:]))
#
#         if inst[0] == 'e':
#             heap = heapq.heapify([])


'''
1
0
1
0
1
0
1
0
0
0
0
0
0
1
0

1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0

'''