'''
    H-index를 나타내는 값인 h를 구하고자 한다.

    h 구하는 방법
        - 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
          나머지 논문이 h번 이하 인용되었다면, h의 최댓값이 H-index

    입력:
        논문의 인용 횟수를 담은 배열 citations
        배열 길이: 1 <= n <= 1000
        배열 요소: 0 <= h <= 10000

    출력:
        H-index를 return
'''

import sys

def solution(citations):
    # 오름차순으로 정렬
    citations.sort()

    # 뒤에서부터 오면서 조건을 만족하는 것 리턴
    for i in range(citations[-1], -1, -1):
        if i in citations:
            j = citations.index(i)
        if i <= len(citations[j:]):
            return i

if __name__ == '__main__':
    citations = [2, 4, 4, 3, 6, 8, 10, 22, 32, 13, 14, 59, 82, 19, 28, 3, 4, 4, 8, 9]
    # 2 3 8 9 10 12 24
    print(solution(citations))


'''
TC1 
[3, 0, 6, 1, 5]
0 1 3 5 6

TC2
[2, 12, 24, 3, 8, 9, 10]

TC3
[0, 0, 0, 0, 0]

TC4
[10, 10, 8, 12, 4, 7]

TC5
[2, 4, 4, 3, 6, 8, 10, 22, 32, 13, 14, 59, 82, 19, 28, 3, 4, 4, 8, 9]

TC6
[2, 4, 4, 3, 6, 8, 10, 22, 32, 13, 14, 59, 82, 19, 28, 10, 4, 4, 8, 9]

TC6
[1]
'''