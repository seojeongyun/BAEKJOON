# asnw += bfs(cur_r, cur_c)
from collections import deque
def bfs(cur_r, cur_c):
    Q = deque()
    Q.append((cur_r, cur_c))
    visited = [[0] * (C+2) for _ in range(R+4)]
    visited[cur_r][cur_c] = 1
    mx_r = 0

    while Q:
        cur_r, cur_c = Q.popleft()
        mx_r = max(mx_r, cur_r)
        for dr, dc in ((-1, 0),(0, 1),(1, 0),(0, -1)):
            nxt_r, nxt_c = cur_r + dr, cur_c + dc
            # if MAP[cur_r][cur_c] == MAP[nxt_r][nxt_c] or ([cur_r, cur_c] in exit_set and MAP[nxt_r][nxt_c] > 1):
            if visited[nxt_r][nxt_c] == 0 and (MAP[cur_r][cur_c] == MAP[nxt_r][nxt_c] or ((cur_r, cur_c) in exit_set and MAP[nxt_r][nxt_c] > 1)):
                Q.append((nxt_r, nxt_c))
                visited[nxt_r][nxt_c] = 1

    return mx_r-2

if __name__ == '__main__':
    R, C, K = list(map(int, input().split()))
    units = [list(map(int, input().split())) for _ in range(K)]
    MAP = [[1] + [0] * C + [1] for _ in range (R+3)] + [[1] * (C+2)]
    g_num = 1
    answ = 0
    exit_set = set()

    # 0, 1, 2, 3 = 북 동 남 서
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for cur_c, dir in units:
        g_num += 1
        cur_r = 1
        while True:
            # 아래로 한 칸 이동
            if MAP[cur_r + 1][cur_c-1] + MAP[cur_r+2][cur_c] + MAP[cur_r+1][cur_c+1] == 0:
                cur_r += 1
            # 왼으로 구른다
            elif MAP[cur_r-1][cur_c-1] + MAP[cur_r][cur_c-2] + MAP[cur_r+1][cur_c-1] + MAP[cur_r+1][cur_c-2] + MAP[cur_r+2][cur_c-1] == 0:
                dir = (dir -1) % 4
                cur_r, cur_c = cur_r+1, cur_c-1
            # 우로 구른다
            elif MAP[cur_r-1][cur_c+1] + MAP[cur_r][cur_c+2] + MAP[cur_r+1][cur_c+1] + MAP[cur_r+1][cur_c+2] + MAP[cur_r+2][cur_c+1] == 0:
                dir = (dir + 1) % 4
                cur_r, cur_c = cur_r+1, cur_c+1
            else:
                break

        if cur_r < 4: # 삐져나왔으면 초기화
            MAP = [[1] + [0] * C + [1] for _ in range (R+3)] + [[1] * (C+2)]
            exit_set = set()
            g_num = 1

        else:   # MAP에 나를 등록, BFS
            MAP[cur_r+1][cur_c] = MAP[cur_r-1][cur_c] = g_num
            MAP[cur_r][cur_c-1:cur_c+2] = [g_num] * 3
            exit_set.add((cur_r + dr[dir], cur_c + dc[dir]))

            answ += bfs(cur_r, cur_c)
    print(answ)


