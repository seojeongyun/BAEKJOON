'''
    https://www.acmicpc.net/problem/1697

    수빈: N (0 <= N <= 100,000)
        - 걷기: 현재 위치 X에서 1초 후 X-1 또는 X+1로 이동
        - 순간이동: 현재 위치 X에서 1초 후 2X의 위치로 이동

    동생: K (0 <= N <= 100,000)

    출력: 수빈이가 동생을 찾는 가장 빠른 시간이 몇 초 후인지 계산
'''

# 백트래킹 실패

import sys
# sys.setrecursionlimit(10**7)
# def in_range(x):
#     return 0 <= x <= 100000
#
# def dfs(n, time):
#     global answ
#
#     # 종료 조건 및 정답 처리
#     if n == K:
#         answ = min(answ, time)
#         return answ
#
#     if in_range(n+1):
#         v[n + 1] = 1
#         dfs(n + 1, time + 1)
#         v[n + 1] = 0
#
#     if in_range(n - 1):
#         v[n - 1] = 1
#         dfs(n - 1, time + 1)
#         v[n - 1] = 0
#
#     if in_range(2 * n):
#         v[2 * n] = 1
#         dfs(2 * n, time + 1)
#         v[2 * n] = 0
#
# if __name__ == '__main__':
#     input = sys.stdin.readline
#     answ = 0
#
#     # [0] 입력
#     N, K = map(int, input().rstrip().split())
#
#     v = [0] * 100001
#     dfs(0, 0)
#     print(answ)

from collections import deque

def in_range(x):
    return 0 <= x <= 100000

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        ci = q.popleft()
        if ci == K:
            # start는 카운트 안 해야되는데 v 배열 특성상 start부터 1이므로 1을 빼준다
            return v[ci]-1

        for di in ((ci+1),(ci-1),(2*ci)):
            ni = di
            if in_range(ni) and not v[ni]:
                q.append(ni)
                v[ni] = v[ci] + 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().rstrip().split())
    v = [0] * 100001
    print(bfs(N))
    # print(v)


'''
    시간복잡도: O(E+V)
        V = 정점 수 = 10만 = N
        E = 간선 수 = 정점 별로 3개씩 = 3*N
        Thus, O(N + 3N) = O(4N) = O(N)
    
    공간복잡도: O(visited) = O(N)
    
    * from gemini
        O(visited) + O(deque) = O(N) + O(N)
'''