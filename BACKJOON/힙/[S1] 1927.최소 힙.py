'''
    최소 힙을 사용해서 다음 프로그램을 작성하시오.
        - 배열에 자연수 x를 넣는다.
        - 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

    프로그램은 처음에 비어있는 배열에서 시작한다.
'''

import sys
import heapq

if __name__ == '__main__':
    answ = []

    # [0] 입력
    input = sys.stdin.readline
    N = int(input().rstrip())

    COMMAND = [int(input()) for _ in range(N)]

    # [1] 힙큐 사용 최고은 권소영 김민정 김민혜 권선이 김지현
    heap = []
    heapq.heapify(heap)

    for command in COMMAND:
        if command == 0:
            if len(heap) == 0:
                answ.append(0)
            else:
                answ.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, command)

    for answer in answ:
        print(answer)


