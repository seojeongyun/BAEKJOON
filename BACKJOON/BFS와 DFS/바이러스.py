'''
연결되어있는 노드 개수 파악하는 문제
    - DFS : 연결 요소 찾기
        예시에서, 1 -> 2 -> 3 -> 5 -> 6
        연결되어있는 요소를 끝까지 파고 가서 찾아야하니 DFS 사용해야할듯.
'''

def DFS(start, cnt):
    #
    visited[start] = 1
    for next in range(N+1):
        if G[start][next] == 1 and visited[next] == 0:
            cnt = DFS(next, cnt+1)

    return cnt

if __name__ == '__main__':
    global V, visited, G
    N = int(input())
    V = int(input())
    M = list(input().split() for _ in range(V))

    G = [[None] * (N+1) for _ in range(N+1)]

    for x,y in M:
        G[int(x)][int(y)] = 1
        G[int(y)][int(x)] = 1

    visited = [0] * (N+1)

    start = 1
    cnt = 0
    cnt = DFS(start, cnt)

    print(cnt)
