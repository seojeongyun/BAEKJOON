'''
    https://www.acmicpc.net/problem/15591

    2/ 512

    N개의 동영상에 대해 (1 <= N <= 5000)

    입력:
        - N, Q
        - N-1개 줄에 유사도가 한 줄에 하나씩 주어짐
            - p, q, r: p와 q가 유사도 r로 연결되어잇다.
        - Q개의 줄에는 Q개의 질문
            - ki, vi (i번 째 질문이 K = ki라면 vi를 보고 있는 소들에게 몇 개의 동영상이 추천될건지 묻는 질문)
            * 값 K를 정해서 유사도가 K이상인 동영상이 추천
    출력:
        - Q개의 줄을 출력
        - i번째 줄에는 i번째 질문에 대한 답변
'''

import sys
from collections import deque

def print_arr(arr):
    for row in arr:
        print(*row)

def BFS(start, k):
    answ = 0
    visited[start] = 1
    usado_max = sys.maxsize
    q = deque()
    q.append((start,usado_max))

    while q:
        ci, usado = q.popleft()
        for ni, w in graph[ci]:
            if not visited[ni]:
                n_usado = min(usado, w)
                visited[ni] = 1
                q.append((ni, n_usado))
                if n_usado >= k:
                    answ += 1

    return answ

if __name__ == '__main__':
    input = sys.stdin.readline
    answ_lst = []

    # [0] 입력
    # 1 <= N, Q <= 5,000
    N, Q = map(int, input().strip().split())
    pqr_lst = [list(map(int, input().strip().split())) for _ in range(N-1)]
    kv_lst = [list(map(int, input().strip().split())) for _ in range(Q)]

    # [1] pqr_list로 map 만들기
    # arr = [[0] * (N+1) for _ in range(N+1)]
    graph = [[] for _ in range(N + 1)]
    for p, q, r in pqr_lst:
        graph[p].append((q, r))
        graph[q].append((p, r))
        # arr[p][q] = r
        # arr[q][p] = r


    # [2] 질문별로  DFS/BFS 적용해서 개수 구하기
    for k, v in kv_lst:
        # 각 질문에 대해 DFS/BFS 적용할 것이니 v배열 초기화
        visited = [0] * (N+1)
        # 여기서 최소값으로 arr 업데이트하고
        answ = BFS(v, k)

        # 여기서 BFS
        answ_lst.append(answ)

    for answ in answ_lst:
        print(answ)


    # combination 적용해서 그래프 형성해야되네. X 아니었다.
    # 1----2----3----4
    #   4     3    2
    # 위처럼 1-2를 잇는 유사도는 4, 2-3을 잇는 유사도는 3, 3-4를 잇는 유사도는 2라고 할 때
    # 1----2----3----4
    #    2    2    2
    # 최솟값인 2로 맞춰놓고 풀어야한다고 생각했음.
    # 그런데 생각해보면 1부터 3까지 이동하는 경로의 최솟값은 min(4,3)=3임. 2가 아님.
    # 즉, 방문하면서 최솟값 갱신하는 방법으로 풀어야함.