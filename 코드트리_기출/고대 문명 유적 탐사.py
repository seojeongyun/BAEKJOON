from collections import deque

def in_range(r,c):
    return 0<=r<5 and 0<=c<5

def rotate(arr, r, c):
    rotated_MAP = [row[:] for row in arr]
    # 3 x 3 행렬 회전
    for i in range(3):
        for j in range(3):
            rotated_MAP[r+i][c+j] = arr[r+3-j-1][c+i]
    return rotated_MAP

def group(s_MAP):
    treasure_num, cnt = 0, 0
    visited = [[0] * 5 for _ in range(5)]
    coords_list = []
    for r in range(5):
        for c in range(5):
            if visited[r][c] == 0:
                cnt, coords = bfs(r, c, visited, s_MAP)
                treasure_num += cnt
                coords_list += coords
    coords = list(set(coords_list))
    return treasure_num, coords

def bfs(r, c, visited, s_MAP):
    Q = deque()
    Q.append((r, c))
    cnt = 0
    coords = []
    visited[r][c] = 1
    cnt += 1
    coords.append((r,c))
    while Q:
        r, c = Q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if in_range(nr,nc):
                if s_MAP[r][c] == s_MAP[nr][nc] and visited[nr][nc] == 0:
                    Q.append((nr,nc))
                    visited[nr][nc] = 1
                    cnt += 1
                    coords.append((nr,nc))
    if cnt < 3:
        coords = []
        cnt = 0
    return cnt, coords


if __name__ == '__main__':
    K, V = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(5)]
    treasure_list = list(map(int, input().split()))

    mx_t_coords = []
    answ_lst = []
    # 북 동 남 서
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 회전 중심 좌표 순회
    for _ in range(K):
        stop = False
        answ = 0
        mx_t_num = 0
        treasure_list_idx = 0
        for rot in range(1, 4):
            for c in range(0, 3):
                for r in range(0, 3):
                    rotated_MAP = [row[:] for row in MAP]
                    for _ in range(rot):
                        rotated_MAP = rotate(MAP, r, c)
                    treasure_num, coords = group(rotated_MAP)
                    if mx_t_num < treasure_num:
                        mx_t_num = treasure_num
                        mx_t_coords = coords
                        max_MAP = [row[:] for row in rotated_MAP]
        if mx_t_num == 0:
            stop = True
            break
        #
        answ += mx_t_num
        mx_t_coords.sort(key=lambda x: (x[1], -x[0]))
        while True:
            for r,c in mx_t_coords:
                max_MAP[r][c] = treasure_list[treasure_list_idx]
                treasure_list_idx += 1
            treasure_num, mx_t_coords = group(max_MAP)
            if treasure_num >= 3:
                answ += treasure_num
                mx_t_coords.sort(key=lambda x: (x[1], -x[0]))

            else:
                break
        answ_lst.append(answ)
        MAP = max_MAP

    if stop:
        pass

    print(*answ_lst)





