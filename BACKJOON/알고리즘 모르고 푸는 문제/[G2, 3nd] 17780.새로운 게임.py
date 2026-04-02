'''
    https://www.acmicpc.net/problem/17780

    0.5 / 512

    새로운 게임
        격자: N x N
        말의 개수 K개
            - 1번부터 K번 까지 번호가 매겨져 있고, 이동 방향도 미리 정해져있음
                - 이동 방향은 상하좌우 중 하나

        턴
            - 1번 말부터 K번 말까지 순서대로 이동
            - 한 말이 이동할 때 위에 올려져있는 말도 함께 이동
            - 가장 아래에 있는 말만 이동할 수 있음

        턴 종료
            - 말이 4개 이상 쌓이는 순간 종료

        EX
            - A번 말이 이동하려는 칸이 흰색인 경우 그 칸으로 이동
                - 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올림
                - A,B,C로 쌓여있고, 이동하려는 칸에 D,E가 있는 경우 D,E,A,B,C가 됨
            - 이동하려는 칸이 빨간색인 경우, 이동 후 A번 말과 그 위에 있는 모든 말의 순서를 반대로 바꿈
                - A,B,C가 이동하고, 이동하려는 칸에 말이 없으면 C,B,A
                - A,D,F,G가 이동하고, 이동하려는 칸에 말이 E,C,B로 있는 경우에는 E,C,B,G,F,D,A
            - 이동하려는 칸이 파란색인 경우, A번의 말의 이동 방향을 반대로 하고 한 칸 이동
                -방향을 반대로 한 후 이동하려는 칸이 파란색인 경우에는 이동하지 않고 방향만 바꿈
            - 체스판을 벗어나는 경우, 방향을 반대로한 후 한 칸 이동

    입력:
        - 체스판 크기 N, 말의 개수 K
        - N개의 줄에 체스판의 정보
            - 0은 흰색, 1은 빨간색, 2는 파란색
        - K개의 줄에 말의 정보
            - 3개의 정수, 행 열, 이동 방향
                - 행 열은 1부터 시작하고, 이동 방향은 4 이하
                - 이동 방향은 1부터 우좌상하

    출력:
        게임이 종료되는 턴의 번호를 입력, 1000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1 출력
'''

import sys

def move(obj_idx):
    i, j, dir = obj_lst[obj_idx]
    if obj_idx != arr_obj[i][j][0]:
        return 0

    # 이동 후 좌표 계산
    ni, nj = i + di[dir], j + dj[dir]

    # 이동 후 마주치는 벽이 파란 색이거나 맵 바깥일 경우
    if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
        # 방향 전환: 동 <-> 서 / 남 <-> 북
        if dir == 0 or dir == 1:
            n_dir = (dir + 1) % 2
        else:
            n_dir = (dir - 1) % 2 + 2

        # 한 칸 이동 (파란 벽 마주치면 방향 전환 후 한 칸 이동이 규칙)
        ni, nj = i + di[n_dir], j + dj[n_dir]
        obj_lst[obj_idx][2] = n_dir
        # 그런데 그 다음 칸도 파란 벽이거나 바깥인 경우
        if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
            return 0

    obj_set = []
    obj_set.extend(arr_obj[i][j])
    arr_obj[i][j] = []

    # 이동 칸이 붉은 벽인 경우
    if arr[ni][nj] == 1:
        obj_set.reverse()

    # 말들의 좌표 갱신
    for idx in obj_set:
        obj_lst[idx][:2] = [ni, nj]
        arr_obj[ni][nj].append(idx)

    if len(arr_obj[ni][nj]) >= 4:
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    arr_obj = [[[] for _ in range(N)] for _ in range(N)]
    obj = [list(map(int, input().strip().split())) for _ in range(K)]
    obj_lst = [[0] for _ in range(K)]

    # [1] obj_list 관리
    for idx, (i, j, dir) in enumerate(obj):
        obj_lst[idx] = [i-1, j-1, dir-1]
        arr_obj[i-1][j-1].append(idx)

    # [2] direction: 우좌상하
    di, dj = [0, 0, -1, 1], [1, -1, 0, 0]

    # [3] 1000회 이동
    cnt = 1
    while cnt <= 1000:
        for idx in range(K):
            flag = move(idx)

            if flag:
                print(cnt)
                sys.exit()
        cnt += 1

    print(-1)





