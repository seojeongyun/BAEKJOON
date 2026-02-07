'''
    격자: N x N
    퀸 N개를 서로 공격할 수 없게 놓는 수를 구하시오.

    * 퀸: 8방향 무제한 이동 가능

'''

def print_status(map):
    for row in map:
        for col in row:
            print(col, end=' ')
        print()

def dfs(row):
    global answ
    # [1] 종료 조건: row == N
    if row == N:
        # [2] 정답 처리
        answ += 1
        return

    for j in range(N):
        if visited1[j] == 0 and visited2[row - j] == 0 and visited3[row+j] == 0:
            visited1[j] = visited2[row-j] = visited3[row+j] = 1
            dfs(row+1)
            visited1[j] = visited2[row - j] = visited3[row + j] = 0

if __name__ == '__main__':
    N = int(input())

    visited1 = [0] * N
    visited2 = [0] * (2*N - 1)
    visited3 = [0] * (2*N - 1)

    answ = 0

    dfs(0)

    print(answ)