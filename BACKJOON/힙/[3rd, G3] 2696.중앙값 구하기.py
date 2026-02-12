'''
    https://www.acmicpc.net/problem/2696

    1 / 128

    수열의 홀수번 째 수를 읽을 때 마다 지금까지 입력받은 값의 중앙값을 출력

    예시:
        수열이 1 5 4 3 2
        첫 번째 수 읽을 때 중앙값 1
        세 번째 수 읽을 때 중앙값 4
        다섯 번째 수 읽을 때 중앙값 3

    입력:
        테스트 케이스 T ( 1<= T <= 1000)
        TC 첫째 줄에는 수열 크기 M(1 <= M <= 9,999, M은 홀수)
        수열의 원소가 10개 씩 주어짐

    출력:
        각 TC에 대해 첫째 줄에는 중앙값 개수
        둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 출력
        한 번에 10개씩 출력
'''

import sys
from heapq import heappush, heappop

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] TC 횟수 입력
    TC = int(input().strip())

    for _ in range(TC):
        tc_answ = []
        # [1] 수열 길이, 수열 입력
        M = int(input().strip())

        num = []
        for _ in range(M//10 + 1):
            num += list(map(int, input().strip().split()))

        # [2]
        left = []
        right = []
        center = [num[0]]
        tc_answ.append(num[0])
        for i in range(1, M):
            # logN
            if center[0] > num[i]:
                heappush(left, -num[i])
            else:
                heappush(right, num[i])

            # 홀수 번 마다 중앙값 갱신 확인
            # left와 right의 길이를 확인해서 길이가 긴쪽에서 최대값 혹은 최소값을 center로 만든다.
            # left가 긴 경우: 최대값 리턴(최대 힙) -> center 대체 -> 기존 center는 right에 heappush
            # right가 긴 경우: 최소값 리턴(최소 힙) -> center 대체 -> 기존 center는 left에 heappush
            if i % 2 == 0:
                if len(left) > len(right):
                    mid_val = center.pop()
                    new_mid = -heappop(left)
                    heappush(right, mid_val)    # logN
                    center.append(new_mid)
                    tc_answ.append(new_mid)

                elif len(left) < len(right):
                    mid_val = center.pop()
                    new_mid = heappop(right)
                    heappush(left, -mid_val)    # logN
                    center.append(new_mid)
                    tc_answ.append(new_mid)

                else:
                    tc_answ.append(center[0])

        # [3] 정답 처리
        answ.append([len(tc_answ)])
        answ.append(tc_answ)

    for val in answ:
        if len(val) > 10:
            for i in range(len(val) // 10 + 1):
                print(*val[i*10:i*10+10])
        else:
            print(*val)


'''
     left        mid         right
*                23
                 23          41
*    13          23          41
     13 22       23          41 
*    -3 13       22          23 41
'''
