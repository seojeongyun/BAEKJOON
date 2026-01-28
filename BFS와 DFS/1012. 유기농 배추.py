'''
    어떤 배추에 흰배추지렁이가 한 마리라도 살고 있으면 인접한 배추로 이동할 수 있어 해충으로부터 보호받을 수 있음
        - 인접 : 상하좌우

    배추들이 모여있는 곳에 흰배추지렁이가 한 마리만 살고 있으면 되므로
    서로 인접해있는 배추들이 몇 군데 퍼져있는지 조사
        - 배추 군집 개수 세아리기

    입력:
        - 가로길이 M(1 ≤ M ≤ 50)
        - 세로길이 N(1 ≤ N ≤ 50)
        - 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
        - K 줄에 걸쳐
            - X(0 ≤ X ≤ M-1)
            - Y(0 ≤ Y ≤ N-1)

    출력:
        - 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수
'''

from collections import deque

def print_status(arr):
    for row in arr:
        for col in row:
            print(col, end=' ')
        print()

def in_range(i,j):
    return 0<=i<N and 0<=j<M

def DFS(visited, ci, cj):
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        if in_range(ni, nj):
            if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                DFS(visited, ni, nj)

def BFS(visited, i, j):
    Q = deque()
    Q.append((i,j))
    visited[i][j] = 1

    while Q:
        ci, cj = Q.popleft()
        for di, dj in ((-1, 0),(1, 0),(0, 1),(0, -1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni,nj):
                if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                    visited[ni][nj] = 1
                    Q.append((ni, nj))

    return 1

def group():
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 1:
                # cnt += BFS(visited, i, j)
                DFS(visited, i, j)
                cnt += 1


    return cnt

if __name__ == '__main__':
    T = int(input())
    answ = []
    for tc in range(T):
        M, N, K = list(map(int, input().split()))
        xy = [list(map(int, input().split())) for _ in range(K)]
        arr = [[0] * M for _ in range(N)]
        # print_status(arr)
        for j, i in xy:
            arr[i][j] = 1

        N_group = group()
        answ.append(N_group)

    for i in range(len(answ)):
        print(answ[i])