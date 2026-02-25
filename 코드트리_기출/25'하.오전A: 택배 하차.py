'''
    박스 쌓기
        - 나
            모든 박스의 좌표 획득해서 아래로 쌓음
        - 혜주 / 종윤
            r = h 부 터 시작해서 아래로 최대한 얼만큼 내릴 수 있는 지 계산하고 그 지점부터 h만큼 쌓아올림

    박스 빼기
        - 혜주
            왼/오로 상자 뺄 때 모든 상자에 대해서 접근하는 게 아니고
            왼쪽으로 뺄 수 있는 애 / 오른쪽으로 뺄 수 있는 애만 찾아서 접근하려고 시도
        - 종윤
            나처럼 우선순위 높은 애부터 왼/오로 이동, 막히면 다음 박스

    박스 뺀 후 쌓기
        - 혜주 / 종윤
            arr을 0으로 다시 초기화하고 빠진 빡스를 제외한 나머지 박스 다시 쌓음
'''
def print_status(arr):
    for row in arr:
        for col in row:
            print(col, end='      ')
        print()

def in_range(i,j):
    # (i: 0 ~ 2N-1, j: 0 ~ N+1)
    return 0 <= i <= 2*N-1 and 0 <= j <= N+1

def find_area():
    glst = []
    for i, h, w, c in units:
        tlst = []
        tlst.append(i)
        ci = N-1
        for di in range(h):
            ni = ci - di
            cj = c
            for dj in range(w):
                nj = cj + dj
                tlst.append([ni, nj])
        glst.append(tlst)
    return glst

def load(glst, clr):
    glst.sort(key=lambda x: -x[1][0])
    for i, group in enumerate(glst):                            # 그룹 하나 선정
        if clr:
            for ti, tj in glst[i][1:]:
                arr[ti][tj] = 0

        dist = 1
        go_nxt_group = False                                    # 선택된 그룹이 범위내, 조건을 만족하는지 확인하는 변수
        while True:                                             # 계속 1씩 내려갈 것임.
            tlst = []                                           #
            for ci, cj in group[1:]:                            # 선택된 그룹의 첫 번째 좌표 추출
                ni,nj = ci+dist, cj                             # dist만큼 아래로 이동
                tlst.append([ni,nj])                            # tlst에 저장

            for ci, cj in tlst:                                 # 선택된 그룹의 모든 좌표가 1만큼 아래로 내려간 것에 대한 리스트에서 좌표 추출
                if not in_range(ci,cj) or arr[ci][cj] != 0:     # 만약 그룹을 구성하는 좌표중 하나라도 조건을 만족하지 못하면 / 범위 밖 or arr이 차있으면
                    tlst_ = []
                    tlst_.append(group[0])
                    for j, (ci, cj) in enumerate(tlst):         # 그룹 전체에 대해서
                        ni, nj = ci-1, cj                       # 위로 한 칸 올리고
                        arr[ni][nj] = group[0]                  # arr에 택배 번호 삽입 후
                        tlst_.append([ni, nj])                  # tlst_에 저장

                    glst[i] = tlst_                             # tlst_를 glst에 반영. 즉 glst[i]에는 가능한 가장 아래의 그룹 좌표가 들어감
                    go_nxt_group = True                         # 다음 그룹으로 넘어감
                    break

            if go_nxt_group:
                break

            dist += 1
    glst.sort(key=lambda x: -x[0])
    return glst

def unit_rm(glst):
    answ = []
    # [2-1] 택배 상자 번호 순으로 sort
    glst.sort(key=lambda x : -x[0])
    # [2-2] 왼쪽부터 시작
    dir = 3
    #
    # [2-3] 택배 다 사라질 때 까지 반복
    while True:
        go_nxt_direction = False
        for idx in range(len(glst)-1, -1, -1):          # 뒤에서 부터 접근
            go_nxt_group = False
            if go_nxt_direction:
                break
            for ci, cj in glst[idx][1:]:                      # 그룹 구성원 좌하단 좌표에 접근
                if go_nxt_group:
                    break
                if go_nxt_direction:
                    break
                #
                ni, nj = ci, cj
                for _ in range(N):                      # 좌하단 좌표 N회 이동
                    if nj == 0 or nj == N+1:                         # 0 혹은 N+1에 도달하면, 즉, 완전히 빼낸 경우
                        # 방향 전환
                        dir = (dir + 2) % 4
                        # arr에 반영하고
                        for i, j in glst[idx][1:]:
                            arr[i][j] = 0
                        # 삭제 -> glst 갱신
                        answ.append(glst[idx][0])
                        glst.pop(idx)
                        # load
                        glst = load(glst,1)
                        go_nxt_direction = True
                        break

                    else:
                        ni, nj = ni + dy[dir], nj + dx[dir]
                        if arr[ni][nj] == 0 or arr[ni][nj] == glst[idx][0]:
                            continue
                        else:
                            go_nxt_group = True
                            break

        if len(glst) == 0:
            break

    return answ





if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    units = [list(map(int, input().split())) for _ in range(M)] # k, h, w, c

    arr = [[0] * (N+2) for _ in range(2*N)]

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # [1] 적재
    # [1-1] h, w, c 바탕으로 unit 영역 구하기
    glst = find_area()

    # [1-2] unit 아래로 쌓기
    glst = load(glst, 0)

    # [2] 빼기
    answ = unit_rm(glst)

    # [3] 출력
    for i in range(len(answ)):
        print(answ[i])

