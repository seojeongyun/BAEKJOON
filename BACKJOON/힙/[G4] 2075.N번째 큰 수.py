'''
    격자: NxN
        - 모든 수는 자신의 한 칸 위에 있는 수보다 크다

    N 번째 큰 수를 찾는 프로그램
'''

# 메모리 관리
    # heap에 다 넣어두고 최댓값 뽑으면 메모리 많이 먹음
    # N번째 큰 수 구하는 것이니 pushpop 이용해서 길이 N으로 고정

import sys
import heapq

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N = int(input())  # N번째로 큰 수의 N

    heap = []
    heapq.heapify(heap)
    for _ in range(N):
        data = [int(x) for x in input().rstrip().split()]
        for e in data:
            if len(heap) < N:
                heapq.heappush(heap, e)
            else:
                heapq.heappushpop(heap, e)

    print(min(heapq.nlargest(N, heap)))


