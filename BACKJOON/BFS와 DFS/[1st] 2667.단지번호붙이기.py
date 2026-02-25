'''
정사각형의 지도
    - 1은 집이 있는 곳
    - 0은 집이 없는 곳

집의 모임을 정의하고, 모임에 번호를 붙임
    모임 정의 : 상하좌우로 연결된 것들

입력
    - N 지도
    - 0과1이 연속적으로 N개, N번 입력 받음
출력
    - 첫째 줄에 총 단지 수
    - 단지 내 집의 수를 오름차순으로 정렬해 한 줄에 하나 씩
'''
def is_in_range(coord:tuple):
    x, y = coord
    return 0<=x<N and 0<=y<N

def DFS(start:tuple, cnt:int):
    x, y = start
    visited[y][x] = 1
    for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
        nx, ny = x + dx, y + dy
        if is_in_range((nx,ny)):
            if visited[ny][nx] == 0 and MAP[ny][nx] == 1:
                MAP[ny][nx] = 2
                cnt = DFS((nx,ny), cnt+1)
    return cnt

def BFS(start:tuple, cnt:int):
    Q = []
    Q.append(start)
    visited[start[1]][start[0]] = 1
    while Q:
        x, y = Q.pop(0)
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if is_in_range((nx,ny)):
                if visited[ny][nx] == 0 and MAP[ny][nx] == 1:
                    Q.append((nx,ny))
                    visited[ny][nx] = 1
                    cnt += 1
    return cnt

def print_status(visited):
    for row in visited:
        for col in row:
            print(col, end='')
        print()

if __name__ == '__main__':
    global MAP, visited
    # 입력
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    #
    visited = [[0] * N for _ in range(N)]

    # 단지별 -> 연결된 노드 개수 파악 -> DFS
    # 단지와 단지 사이는 연결이 끊겨있음 -> 어떻게 파악?
    # => 방문하지 않은 1을 만났으면 탐색
    start = (0,0)
    x,y = start
    dfs_num_cluster = []
    bfs_num_cluster = []
    for row in range(N):
        for col in range(N):
            nx,ny = x + col, y + row
            if visited[ny][nx] == 0 and MAP[ny][nx] == 1:
                start = (nx, ny)
                dfs_cnt = DFS(start, cnt=1)
                # bfs_cnt = BFS(start, cnt=1)
                dfs_num_cluster.append(dfs_cnt)
                # bfs_num_cluster.append(bfs_cnt)

    dfs_num_cluster.sort()
    print(len(dfs_num_cluster))
    for i in range(len(dfs_num_cluster)):
        print(dfs_num_cluster[i])

    # print_status(visited)

    # bfs_num_cluster.sort()
    # print(len(bfs_num_cluster))
    # for i in range(len(bfs_num_cluster)):
    #     print(bfs_num_cluster[i])

    # print_status(visited)
