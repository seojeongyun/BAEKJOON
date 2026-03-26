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

# 탐색하면서 작은 값으로 업데이트하는 건 순차적으로 동작하게 됨
# 4 -> 3 -> 2 이면, 4,3 비교할 땐 3이 작은데 최솟값은 2라서 오답이 됨
# 연결된 그래프의 가중치가 최소가 되도록 전처리한 후 BFS.
# 전처리하는 작업만 하면 될 거 같음
def BFS(start, k):
    answ = 0
    visited[start] = 1000000000
    q = deque()
    q.append(start)

    while q:
        ci = q.popleft()
        for ni in range(N+1):
            if not visited[ni] and arr[ni][ci]:
                visited[ni] = min(visited[ci], arr[ni][ci])
                q.append(ni)
                if arr[ni][ci] >= k:
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
    arr = [[0] * (N+1) for _ in range(N+1)]
    for p, q, r in pqr_lst:
        arr[p][q] = r
        arr[q][p] = r
        # 여기서 최소값 처리만 해주면 될듯

    # [2] 질문별로  DFS/BFS 적용해서 개수 구하기
    for k, v in kv_lst:
        # 각 질문에 대해 DFS/BFS 적용할 것이니 v배열 초기화
        visited = [0] * (N+1)
        answ = BFS(v, k)
        answ_lst.append(answ)

    for answ in answ_lst:
        print(answ)





