'''
    https://school.programmers.co.kr/learn/courses/30/lessons/12924

    자연수 N을 연속한 자연수의 합으로 표현하는 방법의 수
'''

# 투포인터 사용하면 될듯

import sys

def solution(n):
    # sum_lst = []
    # answer_lst = []
    answer_cnt = 0
    #
    # # [1] while-for 사용
    # # while: 개수 찾기 / for: 1~N 까지 순회
    # while True:
    #     for i in range(1, n):
    #         sum_lst.append(i)
    #         if sum(sum_lst) == N:
    #             answer_lst.append(sum_lst[0])
    #             answer_cnt += 1
    #             break

    # 투포인터로 하면 풀릴 거 같아서 변경
    N = int(n)

    # 투포인터
    for i in range(N+1):
        start = i
        sum = 0
        for j in range(i+1,N+1):
            end = j
            sum += end
            if sum == N:
                answer_cnt += 1
                break

    return answer_cnt

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = input().strip()

    # [1] solution
    print(solution(N))


