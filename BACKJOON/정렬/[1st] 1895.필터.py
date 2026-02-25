'''
    https://www.acmicpc.net/problem/1895

    2 / 128

    중앙값
        : 숫자 9개가 오름 or 내림으로 정렬되어 있을 때 중앙갑은 다섯 번째 숫자

    이미지 I = R x C (3 <= R,C <= 40)
        각 픽셀은 V값을 가짐 (0 <= V <= 255)

    filter size = 3x3 , stride = 1에 대해서 중앙값 pooling

    필터링된 이미지 J를 구하고, 값이 T 이상인 픽셀의 수 구하기.
'''

import sys

def find_center(lst):
    lst.sort()
    return lst[4]

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []
    cnt = 0

    # [0] 입력
    R, C = map(int, input().strip().split())
    I = [list(map(int, input().strip().split())) for _ in range(R)]
    T = int(input().strip())

    # [1] Stride:
    for i in range(R-3+1):
        for j in range(C-3+1):
            si, sj = i, j
            lst = []
            for di in range(3):
                for dj in range(3):
                    ci, cj = si+di, sj+dj
                    lst.append(I[ci][cj])

            # dbg
            # print(lst)
            # [2] 중앙값 찾기
            answ.append(find_center(lst))

    # [3] T 이상인 값 개수 찾기
    for val in answ:
        if val >= T:
            cnt += 1

    print(cnt)

'''
    시간 복잡도:
        1. stride
            R,C 2중 포문은 O(N^2) -> N은 3<= R,C <= 40 을 의미
            di,dj는 9회로 O(1) -> 무시
            
        2. 중앙값 찾기
            len(lst) = 9인 lst를 정렬
            lst 길이 고정이므로 O(1)
            
        3. 출력
            len(answ)는 최악의 경우 37^2정도.
            따라서 O(N^2)에 가까움
        
        최종 O(N^2)이고, O(40*40) 은 2초 이내 통과 보장
'''