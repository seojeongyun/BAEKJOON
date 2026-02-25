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

def in_range(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def map2str(map):
    result = ''
    for row in map:
        for col in row:
            result += str(col)
    return result

def find_zero(c_map):
    for i in range(3):
        for j in range(3):
            if c_map[i][j] == 0:
                return i, j

def bfs(MAP):
    seq = map2str(MAP)
    v.setdefault(seq, 1)
    #
    q = deque()
    q.append(MAP)

    while q:
        c_map = q.popleft()
        c_seq = map2str(c_map)
        # 종료 조건
        if c_seq == '123456780':
            return v[c_seq]-1

        # 0 위치 찾기
        ci, cj = find_zero(c_map)

        # 0 위치 바꿔가면서 탐색
        for di, dj in((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            # 범위 내면 0 상하좌우 바꿈
            if in_range(ni, nj):
                n_map = [row[:] for row in c_map]
                n_map[ci][cj] = n_map[ni][nj]
                n_map[ni][nj] = 0
                n_seq = map2str(n_map)
                v.setdefault(n_seq, 0)
                if not v[n_seq]:
                    q.append(n_map)
                    v[n_seq] = v[c_seq] + 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    MAP = [list(map(int, input().strip().split())) for _ in range(3)]
    #
    v = {}

    # [1] BFS
    v.setdefault(map2str(MAP), 1)
    answ = bfs(MAP)

    print(answ)


'''
    시간 복잡도: 노드 수 + 간선 수
    노드 수는 3*3 = 9
    간선 수는 각 노드 당 상하좌우이므로 4*9
    O(E+V) = O(5V) = O(V)
    
    깊은 복사 비용: 모름
    
    find_zero 함수 9회 순환 고정이므로 O(1)
    map2str 함수 9회 순환 + 문자열 변환 비용
    
    최종 시간 복잡도: O(V) * 깊은 복사 비용 * map2str 함수에서 문자열 변환 비용
    
    공간 복잡도: q에 3x3배열 저장하는데 최악의 경우 러프하게 잡았을 때 노드당 상하좌우에 대한 3x3매트릭스 -> 36개 정수 저장인듯?
    
'''
