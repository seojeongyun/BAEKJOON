'''
    격자: N x N
        격자 내 모든 수는 자신의 한 칸 위의 수보다 크다.

    출력: N번째 큰 수를 찾으시오.
'''

# 메모리 제한 12MB => 사용할 자료 구조 특정 => heap 사용

import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = 0

    # [0] 입력
    N = int(input().rstrip())

    # [1] 힙 생성
    HEAP = []
    heapq.heapify(HEAP)

    # [2] 메모리 제한으로 인해 for 문으로 한 줄 씩 받으면서 처리
    # MAP = [list(map(int, input().rstrip().split()) for _ in range(N)]으로 한 번에 받고 시작하면 메모리 과점유

    for _ in range(N):
        # [3] 한 줄 입력받기
        DATA = map(int, input().rstrip().split())

        # [4] 요소 하나에 대해서
        for data in DATA:
            # [5] HEAP의 요소 개수가 N개 이하면 추가
            if len(HEAP) <= N:
                heapq.heappush(HEAP, data)
            # [6] N개 초과면 요소 추가후 최소값 추출
            else:
                heapq.heappushpop(HEAP, data)

    # [7] 상위 N개의 최대값 추출
    ANSW = heapq.nlargest(N, HEAP)

    print(min(ANSW))
