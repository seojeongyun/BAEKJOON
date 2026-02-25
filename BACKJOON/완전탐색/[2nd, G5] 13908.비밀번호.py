'''
    https://www.acmicpc.net/problem/13908

    비밀번호 길이와 선견지명 번호가 주어졌을 때 가능한 모든 비밀번호의 개수 출력
        선견지명: 비밀번호에 어떤 숫자가 들어가는지 일부 알 수 있음.
'''

import sys

def dfs(lst):
    global answ
    # 종료 조건 및 정답 처리
    if len(lst) == N:
        if NUM != -1:
            for num in NUM:
                if num not in lst:
                    break
            else:
                answ += 1
        else:
            answ += 1
        return

    for i in range(10):
        # dfs(lst+[i])
        lst.append(i)
        dfs(lst)
        lst.pop()



if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N, M = map(int, input().rstrip().split())
    NUM = list(map(int, input().rstrip().split())) if M != 0 else -1

    # [1] 백트래킹
    dfs([])

    print(answ)


'''
    제한: 1초/ 64MB
    입력: 1 <= N <= 7, 0 <= M <= N
    연산량: 
        BT 트리에서 최대 10^7
        선견지명 수 검증에서 7^2
        10^7 * 7^2 or 10^7 + 7^2, 후자면 ~= 1억 미만
         
    시간 복잡도: O(10^N)
    
    공간 복잡도: O(NUM) + O(lst) = O(N) + O(N) = O(N)
'''

'''
    TC 1
    3 0
    
    TC 2
    1 1
    4
    
    TC 3
    7 7
    1 2 3 4 5 6 7
'''

'''
    [포함 배제의 원리]
    https://codedrive.tistory.com/406
    N개의 수로 만들 수 있는 경우의 수 - M개의 수를 포함하지 않고 만들 수 있는 경우의 수
'''