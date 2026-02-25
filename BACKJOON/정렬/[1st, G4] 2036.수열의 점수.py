'''
    https://www.acmicpc.net/problem/2036

    2 / 128

    n개의 정수로 이루어진 수열
        - 한 정수를 제거하거나, 또는 두 정수를 제거할 수 있다.
            - 하나 제거: 그 정수가 점수가 됨
            - 둘 제거 : 정수의 곱이 점수

    수열에 아무 수도 남지 않았을 때, 점수의 총 합이 최대가 되는 프로그램

    예시:
        수열: -1, 5, -3, 5, 1
        1 -> 5와 5 제거 -> -1과 -3 제거 -> 29로 최대

    입력:
        - 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)
        - 다음 n개의 줄에는 절댓값이 1,000,000을 넘지 않는 정수가 n개
'''

import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())
    seq = [int(input()) for _ in range(N)]

    # [1] 정렬
    # -4 -2 -1 1 1 2 3 4
    # 음수는 작은 순서대로 두 개 씩 빼고, 양수는 큰 순서대로 두 개 씩 뺌. 양수 중 1은 하나만 뺌

    seq.sort()
    copied_seq = seq[:]
    #
    neg_lst = deque()
    pos_lst = deque()
    #
    # 정렬: O(NlogN)
    for i in range(len(seq)):
        if seq[i] < 0 or seq[i] == 0:
            neg_lst.append(seq[i])
        elif seq[i] == 1:
            answ += 1
        else:
            pos_lst.append(seq[i])

    # O(N)
    while neg_lst:
        score = 1
        if len(neg_lst) > 1:
            for _ in range(2):
                score *= neg_lst.popleft()
        else:
            score = neg_lst.popleft()
        answ += score

    # O(N)
    while pos_lst:
        score = 1
        if len(pos_lst) > 1:
            for _ in range(2):
                score *= pos_lst.pop()
        else:
            score = pos_lst.pop()
        answ += score

    print(answ)

    # 최종 시간 복잡도: O(NlogN)

'''
TC1
5
-1
5
-3
5
1

29

TC2
1
-1

-1

TC3
5
-1
-3
1
5
4

24

TC4
8
-5
-2
-1
1
1
4
2
9

49

TC5
8
-5
-2
-1
0
1
4
2
9

48

TC6
3
-1
2
1
'''