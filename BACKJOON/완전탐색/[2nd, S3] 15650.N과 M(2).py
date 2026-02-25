'''
    https://www.acmicpc.net/problem/15650

    1부터 N까지 중복없이 M개 오름차순으로 고르시오.
'''

import sys

def dfs(lst):
    # 종료 조건 밎 정답 처리
    if len(lst) == M:
        answ.append(lst)
        return

    for i in range(1, N+1):
        if len(lst) == 0:
            if not v[i]:
                v[i] = 1
                dfs(lst+[i])
                v[i] = 0
        else:
            # lst 마지막 요소 값보다 큰 경우에 대해서만 진행하는 코드.
            # 왜 이렇게 코드를 작성해야 하냐면, 중복을 제거하기 위해서.
            # 예를 들어 answ에 [1,2]가 들어있는 상태고
            # 현재 lst = [2] 인 경우에 dfs(lst + [1]) => answ에 [2,1]이 들어감
            # for문은 dfs 함수가 실행될 때 마다 1부터 N+1까지 돌기 때문
            # 따라서 i의 값이 lst의 마지막 인덱스보다 큰 경우에만 dfs 함수를 실행.
            if lst[-1] < i:
                v[i] = 1
                dfs(lst + [i])
                v[i] = 0

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력
    N, M = map(int, input().rstrip().split())

    # [1] 백트래킹
    v = [0] * (N+1)
    dfs([])

    # answ.sort(key=lambda x: x[0])
    for ans in answ:
        print(*ans)


'''
    시간 복잡도: N과 M의 최대는 8
        트리 구조로 보았을 때 8^8 연산, 2^24 = 약 1600만회 << 3천만(1초 연산에 걸리는 시간)
        O(N^M)
    
    공간 복잡도: O(visited) + O(answ) + O(lst) = O(N) + O(N combination M) + O(M) = ?
    
    from gemini:
        # 공간 복잡도
        1. 공간 복잡도 분석: $O(N + M *NCM)이 정확합니다.
            상세 분석
            visited 배열: $O(N)$고정된 크기의 배열입니다.
            lst 및 재귀 스택 (System Stack): $O(M)$재귀 깊이가 최대 $M$이며, lst도 최대 $M$개의 원소를 가집니다.
            answ (정답 저장소): $O(M \times _NC_M)$ (가장 큰 비중)이 부분이 핵심입니다.
            작성하신 코드는 결과를 바로 출력하지 않고 answ라는 리스트에 모두 저장하고 있습니다.
            저장되는 원소의 개수: $_NC_M$ (조합의 수)
            각 원소의 크기: $M$ (리스트 길이)예를 들어 $N=8, M=4$라면, $_8C_4 = 70$개에 불과하지만, $N$이 커지면 메모리 폭발(Memory Limit Exceeded)의 주원인이 됩니다.
             
            20년 차 개발자의 조언 (Best Practice)코딩 테스트나 실제 대용량 데이터 처리에서는 결과를 리스트에 모았다가 한 번에 출력하는 방식을 피해야 합니다.
            현재 방식: 모든 정답을 메모리에 올림 ($O(\text{Exponential})$)
            권장 방식: 찾을 때마다 즉시 출력 (print) 하거나 파일에 쓰고 메모리 해제
            이렇게 하면 공간 복잡도를 $O(N)$ (방문 배열 + 스택)으로 획기적으로 줄일 수 있습니다.
        # 로직
        if sorted(lst) not in answ:  # 이 부분이 문제입니다.
        이 한 줄 때문에 매번 리스트를 정렬(M logM)하고, 정답 리스트 전체를 탐색(현재 찾은 정답 수 X M)하는 비용이 추가됩니다.
        최적화 방식 (Combination w/ Start Index): 애초에 싹이 날 때부터 필요한 가지(오름차순)만 키웁니다.
        1을 고르면 다음은 무조건 2부터 봅니다. (2, 1)이라는 가지 자체가 생성되지 않습니다.
'''