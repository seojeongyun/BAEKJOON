'''
    모든 음식의 스코빌 지수를 K 이상으로 만들기
        - 스코빌 지수가 가장 낮은 두 개의 음식을 섞어 만듦
            - 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

    K 이상이 될 때 까지 반복

    입력:
        배열의 길이 2 이상 100만 이하
        K <= 10억
        음식의 스코빌 지수는 0 이상 100만 이하

    출력:
        섞어야되는 최소 횟수

'''
import heapq
from heapq import heappush, heappop, heapify

# 모든 음식의 스코빌 지수를 K 이상으로 만드는 최소 횟수
# 만들 수 없다면 -1을 리턴

def calc_scoville(x1, x2):
    return x1 +(2*x2)

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    # 최솟값이 K보다 작고 len이 2개 이상이면
    # 음식을 섞는다
    while scoville[0] < K and len(scoville)>1:
        min1, min2 = heappop(scoville), heappop(scoville)
        new_scoville = calc_scoville(min1, min2)
        heappush(scoville, new_scoville)
        answer += 1

    if scoville[0] >= K:
        return answer
    else:
        return -1

if __name__ == '__main__':
    answ = solution([1, 2, 3, 9, 10, 12], 7)
    print(answ)

'''
TC1 
[1, 2, 3, 9, 10, 12] 7 2

TC2
[
'''

