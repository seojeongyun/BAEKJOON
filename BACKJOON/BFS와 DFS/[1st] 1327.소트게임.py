'''
    2초, 128MB
    1부터 N까지 정수로 이루어진 N자리 순열

    K: 어떤 수를 뒤집으면 그 수 부터 오른 쪽으로 K개의 수를 뒤집어야 함
        5 4 3 2 1에서 K가 3일 때, 4를 뒤집으면 5 2 3 4 1이 된다.
        * 뒤집을 수가 K개 이상이어야만 함.

    순열을 오름차순으로 만들고 싶을 때
    수를 최소 몇 개 선택해야하는지
'''

import sys
from collections import deque

def lst_2_int(lst):
    '''
            [3,2,1] -> lst[::-1]
            [1,2,3]
                0, 1 -> 10**0 * 1
                1, 2 -> 10 ** 1 *
                2, 3

    '''

    rslt = 0
    for i, val in enumerate(lst[::-1]):
        rslt += 10 ** i * val

    return rslt

def bfs(seq):
    q = deque()
    q.append((seq, 0))
    v[lst_2_int(seq)] = 1

    while q:
        clst, cnt = q.popleft()
        cval = lst_2_int(clst)
        # 종료 조건: 오름 차순
        if all(clst[i] <= clst[i+1] for i in range(len(clst)-1)):
            return v[cval] -1

        # 각각의 수에 대해서
        for i in range(len(clst)):
            # 뒤집을 수 있으면 뒤집는다.
            if len(clst) - i >= K:
                nlst = clst[:]
                nlst[i:K+i] = nlst[i:K+i][::-1]
                nval = lst_2_int(nlst)
                # 뒤집었을 때 그 값이 미방문이면
                if nval not in v.keys():
                    v[nval] = v[cval] + 1
                    q.append((nlst, cnt))

    return -1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().strip().split())
    SEQ = list(map(int, input().strip().split()))
    # v = [0] * 87654322
    v = {}
    answ = bfs(SEQ)

    print(answ)

'''
    BFS에서 시간 복잡도: 노드 수 * 가지 수 * 1회 연산 비 
    노드: N!개 = O(N!)
    가지: N-K+1 (뒤집을 수 있는 경우) => O(N)
    1회 연산 비용: 종료조건 O(N) + 뒤집기O(N) + lst_2_int O(N) ~= O(N)
    최종: O(N! * N * N) = O(N! * N^2)
    -> N에 8 대입 == 약 250만번.
    
    공간 복잡도:
    deque: 
    v: 최대 N!개 저장 
    
'''