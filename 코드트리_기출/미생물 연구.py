'''
    격자 : N x N

    1. 미생물 투입
        좌표 : 좌하단(c1, r1), 우상단(c2, r2)
        미생물 덮어쓰기
        무리 나뉘면 사라짐

    2. 배양 용기 이동
        - 동일 격자, 기존 용기에서 한 마리도 존재 하지 않을 때 까지
        - 우선순위 (면적 -> 먼저 투입된)
        - 영역 겹침 X, 우선순위 (x 작은 -> y 작은)
        - 어디에도 둘 수 없는 경우 사라짐

    3. 인접 무리 쌍 확인
        - 인접하는 무리끼리의 영역 곱
'''
class group:
    def __init__(self, idx):
        self.idx = idx
        self.coords = []

def in_range(coord:tuple):
    x, y = coord
    return 0<=x<N and 0<=y<N

def overwrite():
    bl_x, bl_y, ur_x, ur_y = list(map(int, input().split()))

    for y in range(bl_y, ur_y):
        for x in range(bl_x, ur_x):
            MAP[y][x] = m_idx

    return MAP

def group_check():
    tlst = []
    visited = [[0] * N for _ in range(N)]

    for y in range (N):
        for x in range(N):
            if MAP[y][x] > 0 and visited[y][x] == 0:
                glst = BFS([x,y], visited)
                tlst.append(glst)

    return tlst

def BFS(coord:tuple, visited):
    idx = MAP[coord[1]][coord[0]]
    visited[coord[1]][coord[0]] = idx

    glst = []
    #
    glst.append(idx)
    glst.append(coord)
    #
    Q = []
    Q.append(coord)
    #
    while Q:
        x, y = Q.pop(0)
        # 4방향, 범위내, v, MAP
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if in_range((nx,ny)):
                if visited[ny][nx]==0 and MAP[ny][nx]==idx:
                    visited[ny][nx] = 1
                    Q.append((nx,ny))
                    glst.append([nx,ny])

    return glst


def del_group(rlst):
    del_set = set()
    for i in range(len(rlst)-1):
        for j in range(i+1, len(rlst)):
            if rlst[i][0] == rlst[j][0]:
                del_set.add(i)
                del_set.add(j)

    for i in range(len(rlst)-1, -1, -1):
        if i in del_set:
            rlst.pop(i)

    return rlst

def replace(rlst):
    # [1] 우선순위 결정
    rlst.sort(key=lambda x: (-len(x), x[0]))

    # [2] 상대좌표로 저장
    for lst in rlst:
        x, y = N, N
        for dx, dy in lst[1:]:
            x = min(x, dx)
            y = min(y, dy)

        for idx in range(1, len(lst)):
            lst[idx][0] -= x
            lst[idx][1] -= y

    # [3] move
    # [3-1] 들어갈 수 있는지 판단
    NEW_MAP = [[0] * N for _ in range(N)]
    for lst in rlst:
        idx = lst[0]
        x, y = check(NEW_MAP, lst[1:]) # 가능한 시작 좌표 리턴, 불가능하면 -1,-1 리
        if (x, y) != (-1, -1):
            for cx, cy in lst[1:]:
                NEW_MAP[y+cy][x+cx]=idx

    return NEW_MAP


def check(NEW_MAP, lst):
    # 최소열/최소행 기준으로 배치 가능한지 판단 후 기준 좌표 리턴, 불가능시 -1,-1
    for y in range(N):
        for x in range(N):
            # x랑 y가 기준좌표
            for cx, cy in lst:
                if x+cx>=N or y+cy>=N or NEW_MAP[y+cy][x+cx] != 0:
                    break
            else:
                return x, y
    return -1,-1

if __name__ == '__main__':
    N, Q = list(map(int, input().split()))
    MAP = [[0] * N for _ in range(N)]
    lst= []
    glst = []

    for m_idx in range(1, Q+1):

        # [1] 미생물 덮어쓰기
        overwrite()

        # [2] 무리 확인
        rlst = group_check()

        # [3] 분리되었으면 삭제
        rlst = del_group(rlst)

        # [4] 재배치
        '''- 우선순위 (면적 -> 먼저 투입된)
        - 영역 겹침 X, 우선순위 (x 작은 -> y 작은)
        - 어디에도 둘 수 없는 경우 사라짐'''
        NEW_MAP = replace(rlst)
        print()
