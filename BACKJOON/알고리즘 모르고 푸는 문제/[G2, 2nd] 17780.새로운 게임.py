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

def move(obj_num):
    i, j, dir = obj[obj_num]
    if obj_num != arr_for_obj[i][j][0]:
        return 0

    ni, nj = i + di[dir], j + dj[dir]

    # 파란 블럭이거나 격자 이탈인 경우
    if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
        # 방향 바꾸고
        if dir == 0 or dir == 1:
            n_dir = (dir+1) % 2
        else:
            n_dir = (dir-1) % 2 + 2
        # n_dir로 갱신
        obj[obj_num][2] = n_dir
        # 한 칸 이동
        ni, nj = i + di[n_dir], j + dj[n_dir]
        # 이동한 칸이 다시 파란 블럭이거나 격자 이탈인 경우
        if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
            # 이동하지 않음
            return 0

    obj_lst = []
    obj_lst.extend(arr_for_obj[i][j])
    arr_for_obj[i][j] = []

    if arr[ni][nj] == 1:
        obj_lst.reverse()

    for idx in obj_lst:
        arr_for_obj[ni][nj].append(idx)
        obj[idx][:2] = [ni, nj]

    if len(arr_for_obj[ni][nj]) >= 4:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    arr_for_obj = [[[] for _ in range(N)] for _ in range(N)]
    obj = [[] for _ in range(K)]
    for idx in range(K):
        i, j, dir = map(int, input().strip().split())
        obj[idx] = [i-1, j-1, dir-1]
        arr_for_obj[i-1][j-1].append(idx)

    # [1] direction
    di, dj = [0, 0, -1, 1], [1, -1, 0, 0]

    # [2] 1000회 탐색
    turn = 1
    while turn <= 1000:
        for i in range(K):
            flag = move(i)

            if flag:
                print(turn)
                sys.exit()
        turn += 1
    print(-1)



