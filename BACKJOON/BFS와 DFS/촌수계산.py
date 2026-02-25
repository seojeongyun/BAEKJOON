'''
입력
    - 1. 사람의 수 N
    - 2. 서로 다른 두 사람의 번호
    - 3. 부모 자식들 간의 관계의 개수 M
    - 4. 부모 자식간의 관계를 나타내는 두 번호 x,y
        - x는 정수 y의 부모 번호

출력
    - 촌수를 나타내는 정수 출력
    - 친척 관계가 전혀 없는 경우 -1 출력

* 최단경로 찾기 -> BFS가 유리
'''

# def DFS(start:int, end:int, cnt:int):
#     visited[start] = True
#     for next in range(len(GRAPH)):
#         if visited[next] == False and GRAPH[start][next] == 1:
#             visited[next] = True
#             cnt = DFS(next, cnt + 1)
#             if next == end:
#                 return cnt
#     return cnt

def BFS(start:int, end:int):
    Q = []
    Q.append(start)
    visited[start] = 1

    while Q:
        start = Q.pop(0)
        if start == end:
            return visited[end] -1
        #
        for next in range(len(GRAPH)):
            if visited[next] == 0 and GRAPH[start][next] == 1:
                Q.append(next)
                visited[next] = visited[start] + 1

    return -1
    # 위처럼 해도 되고. 어차피 촌수 없으면 visited[end] = 0 일테니, cnt -1 로 print해도 됨.
# def BFS(start:int, end:int, cnt:int):
#     Q = []
#     Q.append(start)
#     visited[start] = 1
#
#     while Q:
#         start = Q.pop(0)
#         if start == end:
#             return cnt
#         #
#         for next in range(len(GRAPH)):
#             if visited[next] == 0 and GRAPH[start][next] == 1:
#                 Q.append(next)
#                 visited[next] = visited[start] + 1
#         cnt += 1
#     return -1
# BFS 어떻게 동작하는지 정확히 이해 못한 멍청이

if __name__ == '__main__':
    global visited, GRAPH
    N = int(input())
    X, Y = list(map(int, input().split()))
    M = int(input())
    F = [list(map(int, input().split())) for _ in range(M)]

    GRAPH = [[None] * (N+1) for _ in range(N+1)]
    for x, y in F:
        GRAPH[x][y] = 1
        GRAPH[y][x] = 1

    visited = [0] * (N+1)
    #
    start = X
    end = Y
    cnt = 0
    #
    cnt = BFS(start, end)
    # cnt = BFS(start, end, cnt)
    # BFS 동작 이해 못한 멍청이
    print(cnt)
