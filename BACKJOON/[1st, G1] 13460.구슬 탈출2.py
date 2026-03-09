'''
    https://www.acmicpc.net/problem/13460

    2 / 512

    보드: N x M
        - 보드에는 구멍이 존재.
        - 빨간 구슬과 파란 구슬이 하나 씩 들어가있다.

    목표:
        - 빨간 구슬을 구멍을 통해 빼내는 것
        - 파란 구슬이 구멍에 들어가면 안된다.
        - 동시에 들어가도 안된다.

    동작:
        - 상하좌우로 기울이기

    각 동작에서 공은 동시에 움직인다.
    두 구슬은 동시에 같은 칸에 있을 수 없다.
    더 이상 구슬이 움직이지 않을 때 까지 기울인다.

    최소 몇 번 만에 빨간 구슬을 빼낼 수 있는지 구하시오

    입력:
        - 첫 번째 줄에는 N, M (3 ≤ N, M ≤ 10)
        - N개의 줄에 길이 M의 문자열이 주어진다.
            -  '.', '#', 'O', 'R', 'B'
                - '.'은 빈 칸
                - '#'은 공이 이동할 수 없는 장애물 또는 벽
                - 'O'는 구멍의 위치
                - 'R'은 빨간 구슬의 위치
                - 'B'는 파란 구슬의 위치
    출력:
        - 최소 몇 번 만에 빼낼 수 있는지 출력
        - 만약 10번 이하로 움직여서 빼낼 수 없으면 -1
'''

'''
    이동 조건:
        - 상하좌우
        - .으로만 이동
        - R 위치 != B 위치
    visited:
        - B,R 따로 3차원 관리
'''
import sys
from collections import deque

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs(r_start, b_start, goal):
    ri, rj = r_start
    bi, bj = b_start
    gi, gj = goal
    visited[ri][rj] = 1
    #
    q = deque()
    q.append((ri,rj,bi,bj))

    while q:
        rci, rcj, bci, bcj = q.popleft()
        # 10회가 넘은 경우 (10회 이하로 구슬을 꺼낼 수 없는 경우 -1 리턴)
        if visited[rci][rcj] == 11:
            return -1

        # 빨간 구슬이 구벙을 통과한 경우
        if rci == gi and rcj == gj:
            return visited[rci][rcj]-1

        # 이동할 수 없을 때 까지 이동
        # 카운팅

        # 구슬 이동
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            # B와 R은 같은 방향으로 이동해야 함.
            rni, rnj, bni, bnj = rci+di, rcj+dj, bci+di, bcj+dj
            if in_range(rni, rnj) and map[rni][rnj] != '#' and not visited[rni][rnj]: # 범위내, 미방문, 벽이 아니면
                # 기울이기(벽이나 빨간/파란공을 마주치기 전까지)
                while True:
                    rni, rnj, bni, bnj = rni+di, rnj+dj, bni+di, bnj+dj
                    # 둘 중 하나가 벽을 마주친 경우
                    if map[rni][rnj] == '#' or map[bni][bnj] == '#':
                        if map[rni][rnj] == '#'
                visited[rni][rnj] = visited[rci][rcj] + 1
                q.append((rni, rnj, bni, bnj))

            # 파란 구슬 경우의 수
            # 골인(-1), 벽이나 빨간 구슬에 의해 막힌 경우, 이동하는 경우
    return -2

def print_map(map):
    for row in map:
        print(*row)

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, M = map(int, input().strip().split())
    map = [[char for char in input().strip()] for _ in range(N)]

    # [1] visited 배열
    visited = [[0] * M for _ in range(N)]

    # [2] BFS
    # R, B, O의 좌표를 알아내야 함.
    for row in range(N):
        for col in range(M):
            if map[row][col] == 'R':
                ri, rj = row, col
            if map[row][col] == 'B':
                bi, bj = row, col
            if map[row][col] == 'O':
                gi, gj = row, col

    answ = bfs((ri, rj), (bi, bj), (gi,gj))
    print(answ)