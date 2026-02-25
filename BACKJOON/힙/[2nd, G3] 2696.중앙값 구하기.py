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
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    total_answ = []
    # [0] 입력
    TC = int(input().strip())

    for _ in range(TC):
        answ = []

        M = int(input().strip())
        # 수열 개수 10개 이상이면 반복문으로 입력 받기
        # 시간 복잡도 O(M)
        if M > 10:
            lst = []
            data = [list(map(int, input().strip().split())) for _ in range(M//10+1)]
            for row in data:
                for col in row:
                    lst.append(col)
        else:
            lst = list(map(int, input().strip().split()))

        # [1] 중앙값 구하기 O(M)
        cnt = 0
        tlst = []
        while lst:
            cnt += 1
            tlst.append(lst.pop(0)) # pop(0)은 O(N), N번 반복 -> O(N^2)
            if cnt % 2 != 0:
                # tlst에서 중앙값 찾기
                tlst.sort() # sigma k=1부터 k=N까지의 (klogk) 누적합, 원소 개수가 증가하기 때
                            # 대충 N/2번 sort 진행 * 정렬 비용 (NlogN)
                answ.append(tlst[cnt//2])

        # [2] 출력
        if len(answ) > 9:
            total_answ.append([len(answ)])
            for i in range(len(answ)//10+1):
                total_answ.append(answ[10*i:10*i+10])
        else:
            total_answ.append([len(answ)])
            total_answ.append(answ)

    for val in total_answ:
        print(*val)
        # if len(val) > 10:
        #     for i in range(len(answ)//10+1):
        #         print(val[10*i:10*i+10])
        # else:
        #     print(*val)


'''
1
23
23 41 13 22 -3 24 -31 -11 -8 -7
3 5 103 211 -311 -45 -67 -73 -81 -99
-33 24 56
'''