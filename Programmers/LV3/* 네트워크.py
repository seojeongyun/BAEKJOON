'''
    https://school.programmers.co.kr/learn/courses/30/lessons/43162#
'''

# 연결 그래프가 주어진 경우, v를 1차원으로 선언
# v의 인덱스는 연결 그래프의 row를 의미

from collections import deque


def dfs(i, v, n, computers):
    for j in range(n):
        if not v[j] and computers[i][j]:
            v[j] = 1
            dfs(j, v, n, computers)
    return


def solution(n, computers):
    answer = 0

    # BFS
    #     v = [0] * n
    #     for i in range(n):
    #         # 미방문
    #         if not v[i]:
    #             answer += 1
    #             #
    #             q = deque([i])
    #             v[i] = 1
    #             while q:
    #                 # pop
    #                 cj = q.popleft()

    #                 # 순회: 0~N, 미방문, 범위내, 조건 만족
    #                 for nj in range(n):
    #                     if not v[nj] and computers[cj][nj]:
    #                         v[nj] = 1
    #                         q.append(nj)

    # DFS
    v = [0] * n

    for i in range(n):
        if not v[i]:
            answer += 1
            v[i] = 1
            dfs(i, v, n, computers)
    return answer