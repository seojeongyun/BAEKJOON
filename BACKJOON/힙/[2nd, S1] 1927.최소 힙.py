'''
    https://www.acmicpc.net/problem/1927

    1 / 128

    최소힙을 이용해 프로그램 작성
        - 배열에 자연수 x를 넣는다
        - 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

    입력:
        첫째 줄에 연산의 개수 N(1<= N <= 100,000)
        N개의 줄에 걸쳐 정수 x 제공
            x가 자연수면 배열에 추가
            x가 0이면 작은값 출력 후 제거

    출력:
        입력에서 0이 주어진 횟수만큼 답 출력
        배열이 비어있는 경우 0이 들어오면 0 출력
'''

import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력
    N = int(input().strip())
    heap = []

    # [1] 문제 풀이: O(NlogN) 
    for _ in range(N):
        x = int(input().strip())
        if x == 0:
            if len(heap) == 0:
                answ.append(0)
            else:
                answ.append(heapq.heappop(heap)) # heappop에서 O(logk)
        else:
            heapq.heappush(heap, x) # heappush에서 O(logk)

    for val in answ:
        print(val)
