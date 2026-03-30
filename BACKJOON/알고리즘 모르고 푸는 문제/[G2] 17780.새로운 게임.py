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

def move(chess_num):
    i, j, dir = horse[chess_num]
    if chess_num != chess[i][j][0]:
        return 0

    ni, nj = i+dy[dir], j+dx[dir]

    if not 0 <= nj < N or not 0 <= ni < N or arr[ni][nj] == 2:
        if 0 <= dir <= 1: # x축 이동
            n_dir = (dir+1) % 2
        else:
            n_dir = (dir-1) % 2 + 2

        horse[chess_num][2] = n_dir
        ni, nj = i + dy[n_dir], j + dx[n_dir]
        # 반대쪽도 파란색 칸이면 이동하지 않음
        if not 0 <= nj < N or not 0 <= ni < N or arr[ni][nj] == 2:
            return 0

    chess_set = []
    chess_set.extend(chess[i][j])
    chess[i][j] = []

    if arr[ni][nj] == 1:
        chess_set.reverse()

    for i in chess_set:
        chess[ni][nj].append(i)
        horse[i][:2] = [ni, nj]

    if len(chess[ni][nj]) >= 4:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    chess = [[[] for _ in range(N)] for _ in range(N)]
    horse = [0 for _ in range(K)]

    obj = [list(map(int, input().strip().split())) for _ in range(K)]
    for idx, (i, j, dir) in enumerate(obj):
        chess[i-1][j-1].append(idx)
        horse[idx] = [i-1, j-1, dir-1]

    dx = [1, -1, 0, 0] # 1부터 우좌상하
    dy = [0, 0, -1, 1]

    # [1]
    # 가지고 있어야 하는 정보
    # 말의 좌표, 이동 방향, 쌓이는 순서, 동일 턴 내에서 이동했는지 여부

    turn = 1
    while turn <= 1000:
        for i in range(K):
            flag = move(i)
            if flag:
                print(turn)
                sys.exit()
        turn += 1
    print(-1)


'''
    시간 복잡도
    1000 * K 정도.
'''








