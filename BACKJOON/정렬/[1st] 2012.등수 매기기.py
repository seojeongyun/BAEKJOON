'''
    https://www.acmicpc.net/problem/2012

    2 / 256

    N명의 학생이 대회에 참가, N명 중 예상 등수를 적어 제출

    1등부터 N등까지 동석차 없이 등수를 매겨야 함

    불만도: 예상 등수 A, 실제 등수 B
        A와 B의 차이: abs(A-b)

    불만도의 합이 최소가 되도록 정렬

    입력: N (1 ≤ N ≤ 500,000), N개 줄에 걸쳐 예상 등수가 주어짐
    출력: 불만도 출력
'''
import sys
from itertools import permutations, combinations

def combination(lst, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(lst)):
        elem = lst[i]
        rest_lst = lst[1+i:]
        for C in combination(rest_lst, n-1):
            result.append(C+[elem])

    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())
    pred = [int(input().strip()) for _ in range(N)]
    B = N * (N + 1) // 2

    # [1] 정렬: 키 생성 비용 O(N),  정렬 비용 (NlogN)
    pred.sort(key=lambda x: -1*(B - x))
    # print(pred)

    # [2] 출력: O(N)
    for i, val in enumerate(pred):
        answ += abs((i+1)-val)
    print(answ)


'''
    TC 1
    1 5 3 1 2
    1 1 2 3 5
    
    TC 2
    5
    1 1 1 1 1
    1 1 1 1 1
    
    3
    3 1 2
    1 2 3 
    
    7
    1
    1 
    2 
    4 
    6 
    5 
    4
    1 1 2 4 4 5 6
     
'''
