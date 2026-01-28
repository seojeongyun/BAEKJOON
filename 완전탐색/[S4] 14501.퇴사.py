'''
    N + 1일째 되는 날 퇴사.
    남은 N일 동안 상담 진행

    최대 수익을 구하시오
'''

# 시간 복잡도
# 1 <= N <= 15 이므로, 상담을 한다 vs 안 한다로 완탐 시 2^15번 연산
# 2^15 ~= 2^10이 대략 1000이므로, 1000^4 수준의 연산. 완탐 적용 가능

# 알고리즘: 재귀
# 재귀: 함수 하나만 완성하면 됨
# 1. 종료조건 : 상담이 N+1 이내 완료 가능해야함
    # if n >= N+1: 수익 갱신
        # cash = max(cash(아마 Pi), sum(누적되어온 값))
# 2. 하부 함수 처리
    # 상담하는 경우
        # if n + T[n] <= N+1
            # dfs (n+T[n], sum+P[n])
    # 상담하지 않는 경우
        # dfs(n+1, sum)

import sys

# def search(start, sum):
#     global answ
#     # [1] 종료조건: 가능한 start를 종료에 관련된 것으로 정의
#     if start >= N:
#         answ = max(answ, sum)
#         return
#
#     # [2] 하부 함수 호출: 화살표 개수만큼(현재는 이진트리)
#     if start+T[start] <= N: # 퇴사일 전에 상담 완료 가능한 경우
#         search(start+T[start], sum+P[start])
#     # 여기서 else 쓰면 실패, 가능한 모든 경우를 처리해야 함.
#     search(start+1, sum) #  상담하지 않는 경우

def search(now, cash):
    global answ

    # [1] 종료 조건
    if now >= N:
        # 정답에 대한 조건 처리
        # 최대 수익을 뽑아야 하므로 answ와 cash를 비교해서 큰 값으로 answ 갱신
        answ = max(answ, cash)
        return

    # [2] 상담 가능한지
    if now+T[now] <= N:    # 퇴사일 이전이면, 즉 상담이 가능하면
        search(now+T[now], cash+P[now])
    # [3] 상담을 안하는 경우
    search(now+1, cash)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    T = [0] * N
    P = [0] * N
    for i in range(N):
        T[i], P[i] = map(int, input().rstrip().split())

    answ = 0
    search(0,0)
    print(answ)