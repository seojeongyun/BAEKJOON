'''
    수열의 홀수번 째 마다 지금까지 입력받은 값의 중앙값을 출력하는 프로그램

    출력
        - 첫째 줄: 출력하는 중앙값의 개수
        - 둘 째 줄: 홀수 번째 읽을 때 마다 구한 중앙값

    알고리즘
        - 첫째 줄: N / 2 + 1
        - 중앙값 구하기
            - 최대힙과 최소힙을 만들고 각각 pop 시키면서 pop된 값이 같아지면 중앙값
'''

import sys
import heapq

# 알고리즘 [1]
# 최소힙 최대힙 생성 후 pop 시킴.
# 동일한 값을 pop시킨 경우 중앙값

# 알고리즘 [2]
# 최소힙 생성하고 for문으로 필요한 만큼만 슬라이싱해서 사용(메모리 관리)

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    T = int(input())
    answ = []

    # 테스트 케이스에 대해서
    for TC in range(T):
        # 수열 크기 입력
        N = int(input())

        # 출력하는 중앙값 개수
        n_rslt = N // 2 + 1
        center = []
        data = []

        # 데이터 입력
        input_data = [list(map(int, input().rstrip().split())) for _ in range(N//10+1)]
        for row in input_data:
            for col in row:
                data.append(col)

        # 홀수 번 째 마다 홀수 개 만큼의 heapq 생성
        for i in range(1, N+1, 2):
            sliced_min = data[:i]
            heapq.heapify(sliced_min)

            center_pos = i // 2 + 1
            for j in range(center_pos):
                if j == center_pos-1:
                    center.append(heapq.heappop(sliced_min))
                else:
                    heapq.heappop(sliced_min)
        answ.append([n_rslt, center])

    for answer in answ:
        print(answer[0])
        if len(answer[1]) > 10:
            line = len(answer[1]) // 10 + 1
            for i in range(line):
                print(*answer[1][i*10:i*10+10])

        else:
            print(*answer[1])






