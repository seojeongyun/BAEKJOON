'''
    격자: M x N

    토마토
        잘 익은 토마토: 1
            하루 뒤 인접한 곳의 익지 않은 토마토들이 익음
        안 익은: 0
        빈 격자: -1

    출력 :
        다 익게 되는 최소 일수
        처음 부터 익어있으면 0, 모두 익지 못하는 상황이면 -1
'''

import sys
from collections import deque

def vis(map):
    for row in map:
        print(*row)

def in_range(i, j):
    return 0 <= i < M and 0 <= j < N

def bfs(start):
    q = deque(start)

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not v[ni][nj] and not MAP[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                MAP[ni][nj] = 1

    # 0이 하나라도 있으면 1 출력
    if not all(col for row in MAP for col in row):
        return -1

    # 0이 하나도 없으면
    return v[ci][cj] - 1

def solution():
    global answ
    lst = []
    if all(col == 1 for row in MAP for col in row):
        return 0

    for i in range(M):
        for j in range(N):
            if MAP[i][j] == 1:
                # BFS 출발 지점 저장
                v[i][j] = 1
                lst.append((i,j))

    # if not v[i][j] and MAP[i][j] == 1:
    #     v[i][j] = 1
    #     answ += bfs((i, j))
    answ = bfs(lst)
    return answ



if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N, M = map(int, input().rstrip().split())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(M)]

    # [1] 탐색
    v = [[0] * (N) for _ in range(M)]
    solution()

    print(answ)

'''
    시간 복잡도: O(E + V)
    E: 1,000,000 * 4 = 4,000,000
    V: 최대 1000^2 = 1,000,000
    
    최종 시간복잡도 합치기

    [from gpt]
    시간 복잡도
        초기 all 검사: O(MN)
        익은 토마토 찾기: O(MN)
        BFS: O(MN)
        마지막 all 검사: O(MN)
        합쳐도 빅오로는 O(MN)+O(MN)+O(MN)+O(MN)=O(MN)
    
    공간 복잡도
        | 구성 요소   | 공간    |
        | ------- | ----- |
        | MAP     | O(MN) |
        | v       | O(MN) |
        | BFS 큐   | O(MN) |
        | 시작점 리스트 | O(MN) |
        | 기타      | O(1)  |

'''

