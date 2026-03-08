'''
    https://www.acmicpc.net/problem/1987

    2 / 256

    격자:  R x C
        - 각 칸에는 대문자 알파벳이 하나씩 적혀있고
        - 좌상단(1,1)에는 말이 놓여있다.

    말은 상하좌우로 인접한 네 칸 중 한 칸으로 이동
    새로 이동한 칸에 적혀있는 알파벳은 지금까지 지나온 모든 칸에 적혀있는 알파벳과 달라야 한다.

    말이 최대 몇 칸 지날 수 있는지 구하시오.
    * 좌상단 칸도 포함

    입력:
        - R, C가 빈칸을 사이에 두고 주어짐
        - 둘째 줄부터 R개의 줄에 걸쳐 C개의 대문자 알파벳들이 빈칸없이 주어짐

    출력:
        - 말이 지날 수 있는 최대 칸수
'''

import sys
from collections import deque

def print_map(map):
    for row in map:
        print(*row)

def in_range(ci, cj):
    return 0 <= ci < R and 0 <= cj < C

def bfs(start):
    global answ

    i, j = start
    visited[i][j] = 1
    q = set()
    q.add((i, j, map[i][j]))
    #
    while q:
        ci, cj, alpha = q.pop()
        answ = max(answ, len(alpha))
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not visited[ni][nj] and map[ni][nj] not in alpha:
                q.add((ni, nj, alpha+map[ni][nj]))


# def dfs(start):
#     global answ
#
#     ci, cj = start
#     answ = max(answ, visited[alphabet[map[ci][cj]]])
#     #
#     for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         ni, nj = ci + di, cj + dj
#         if in_range(ni, nj) and not visited[alphabet[map[ni][nj]]]:
#             visited[alphabet[map[ni][nj]]] = visited[alphabet[map[ci][cj]]]+1
#             dfs((ni,nj))
#             visited[alphabet[map[ni][nj]]] = 0


if __name__ == '__main__':
    input = sys.stdin.readline
    answ = -1

    # [0] 입력
    R, C = map(int, input().strip().split()) # 최대 20 x 20
    # map = [input().split() for _ in range(R)]
    map = [[char for char in input().strip()] for _ in range(R)]

    # [1] A to Z
    alphabet = {'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
                'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18,
                'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    # [2] DFS
    # visited = [0] * 26
    # visited[alphabet[map[0][0]]] = 1
    # dfs((0,0))

    # [2-1] BFS
    visited = [[0] * C for _ in range(R)]
    bfs((0,0))

    # [3] answ
    print(answ)


'''
    시간복잡도
    최대 격자 크기 = 20 x 20 = 400
    격자별 최대 이동 가능 수 = 4 
    
'''