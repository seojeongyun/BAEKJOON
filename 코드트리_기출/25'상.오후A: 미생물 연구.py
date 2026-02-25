'''
    격자: N x N

    실험: Q회 진행
        1. 미생물 투입
            - 좌상단(r1,c1)이고 우하단(r2,c2)인 직사각형 영역에 미생물 한 무리 투입
            - 영역 내에 다른 미생물이 존재하면 덮어씀
            - 덮어씌워지면서 기존 미생물 무리가 두 영역 이상으로 나뉘면 기존 미생물 모두 사라짐

        2. 배양 용기 이동
            - 기존 배양 용기에서 가장 영역이 넓은 무리 선택 (둘 이상이면 먼저 투입된 미생물이 우선순위)
            - 기존 용기에서의 형태 유지, 다른 미생물과 겹치지 않도록
                - 이 조건 내에서 x좌표가 작은 위치로 옮김(그런 위치가 둘 이상이면 y가 자은 위치로 오도록)
            - 어떤 곳에도 둘 수 없는 미생물 무리가 있다면 해당 미생물 무리는 사라짐

        3. 실험 결과 기록
            - 미생물 무리 중 상하좌우로 맞닿은 면이 있는 무리 " 인접한 무리 "
            - 모든 인접한 무리 쌍 확인
                - 확인하는 두 무리가 A, B라면 (A의 영역의 넓이 * B의 영역의 넓이) 만큼 성과 획득
            - 확인한 모든 쌍의 성과를 더한 값이 실험의 결과

    입력:
        - 첫 줄에 N, Q (2 <= N <= 15, 1 <= Q <= 50)
            - N은 격자 사이즈, Q는 실험 횟수
        - Q줄에 걸쳐 추가되는 미생물의 위치 정보 제공
            - r1,c1,r2,c2
'''

'''
TC 1
8 4
2 2 5 6
2 3 5 8
2 0 5 3
1 1 6 6

8 2
0 0 3 4
0 1 7 2
'''
from collections import deque

def print_map(map):
    for row in map:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def search_cluster():
    v = [[0] * 8 for _ in range(N)]
    cluster_coord_dict = {}
    for row in range(N):
        for col in range(N):
            if MAP[row][col] > 0 and not v[row][col]:
                cluster_coord_dict.setdefault(MAP[row][col], [])
                cluster_coord_lst = bfs((row, col), MAP[row][col], v)
                cluster_coord_dict[MAP[row][col]].append(cluster_coord_lst)
    return cluster_coord_dict

def bfs(start, target_val, v):
    q = deque()
    q.append(start)
    cluster_coord = []

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and MAP[ni][nj] == target_val and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = target_val
                cluster_coord.append((ni, nj))

    cluster_coord.sort(key=lambda x: (x[0], x[1]))
    return cluster_coord

def put_microorganism(lst, i):
    c1,r1,c2,r2 = lst

    for row in range(r1, r2):
        for col in range(c1, c2):
            MAP[row][col] = i

    cluster_coord_dict = search_cluster()

    for k in cluster_coord_dict.keys():
        if len(cluster_coord_dict[k]) > 1:
            del(cluster_coord_dict[k])

    return cluster_coord_dict

def move_microorganism(microorganism_dict):
    NEW_MAP = [[0] * 8 for _ in range(N)]
    # 면적순 -> 일찍 들어온 순으로 정렬
    microorganism_dict = dict(sorted(microorganism_dict.items(), key=lambda x: (len(x[1][0]), x[0])))

    for k, v in microorganism_dict:
        candidate_coord = []
        lb_i, lb_j = v[0][0]

        # new_MAP에서 val이 0이 아닌 모든 좌표 추출
        for row in range(N):
            for col in range(N):
                if NEW_MAP[row][col] == 0:
                    candidate_coord.append((row, col))

        # x작고 y 작은 순으로 정렬
        candidate_coord.sort(key=lambda x: (x[1], x[0]))

        # 추출된 좌표에서 가장 작은 x에 대입 가능한지 확인
        for cand_i, cand_j in candidate_coord:

            for ci, cj in v[0]:
                pass


        # 해당 x값으로부터 나열 가능하면 나열, 이런 x가 두 개면 y가 작도록

        # 불가능하면 new_MAP에 배치 가능한 가장 작은 y 계산
        # 이것도 안되면 제거


if __name__ == '__main__':
    answ = []

    # [0] 입력
    N, Q = map(int, input().split())
    microorganism_coord = [list(map(int, input().split())) for _ in range(Q)]

    # [1] map, v 생성
    MAP = [[0] * 8 for _ in range(N)]
    # v = [[0] * 8 for _ in range(N)]

    # [2] 실험 시작
    for i, coord in enumerate(microorganism_coord):
        # [3] 미생물 투입
        microorganism_dict = put_microorganism(coord, i+1)

        # [4] 배양 용기 이동
        move_microorganism(microorganism_dict)
        print_map(MAP)

        # [5] 실험 결과 기록
        # answ.append(score)

    for val in answ:
        print(val)

