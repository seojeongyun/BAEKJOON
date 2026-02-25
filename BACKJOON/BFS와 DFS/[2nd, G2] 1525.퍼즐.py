'''
    https://www.acmicpc.net/problem/1525

    1 / 32

    3x3 표 중 8칸에 숫자가 채워져 있다.
    빈 칸에 인접한 숫자를 옮길 수 있다.
    최소한의 이동으로 좌상~우하 까지 정렬된 숫자를 만들고 싶다.

    출력:
        첫째 줄에 최소의 이동 횟수
        이동 불가능하면 -1
'''

import sys
from collections import deque

def in_range(i,j):
    return 0 <= i < 3 and 0 <= j < 3

def arr2str(arr):
    result = []
    for row in arr:
        for col in row:
            result.append(str(col))
    return ''.join(result)

def bfs(seq):
    q = deque()
    q.append(seq)

    while q:
        c_seq = q.popleft()
        v.setdefault(c_seq, 0)
        # 종료 조건
        if c_seq == '123456780':
            return v[c_seq] - 1

        c_zero_idx = c_seq.index('0')
        ci, cj = c_zero_idx // 3, c_zero_idx % 3

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj):
                lst = list(c_seq)
                n_zero_idx = ni*3+nj
                lst[c_zero_idx], lst[n_zero_idx] = lst[n_zero_idx], '0'
                n_seq = ''.join(lst)
                v.setdefault(n_seq, 0)
                if not v[n_seq]:
                    v[n_seq] = v[c_seq] + 1
                    q.append(n_seq)

    return -1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    MAP = [list(map(int, input().strip().split())) for _ in range(3)]

    # [1] BFS
    v = {}
    seq = arr2str(MAP)
    v.setdefault(seq, 1)
    answ = bfs(seq)

    print(answ)