'''
    https://www.acmicpc.net/problem/8979

    1 / 128

    1. 금메달 수가 더 많은 나라
    2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
    3. 금메달 == 은메달이면, 동메달 수가 더 많은 나라

    각 국가는 1부터 N사이의 정수로 표현된다
    한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의
    두 나라의 금==은==동 이면 등수는 같다

    입력: 각 국가의 금,은,동 정보
    출력: 어느 국가가 몇 등을 했는지
'''

import sys

# if __name__ == '__main__':
#     input = sys.stdin.readline
#
#     # [0] 입력
#     N, K = map(int,input().strip().split())
#     lst = [list(map(int, input().strip().split())) for _ in range(N)]
#     country = []
#     medals = []
#     for i in range(len(lst)):
#         country.append(lst[i][0])
#         medals.append(lst[i][1:])
#
#     country_K_medals = medals[country[K-1]-1]
#     # [1] 정렬
#     medals.sort(key=lambda x: (-x[0], -x[1], -x[2]))
#
#     same_cnt = 0
#     buff = medals[0]
#     # [2] 출력: 국가 K의 등수 (동점 고려)
#     for i in range(len(medals)):
#         if i > 0 and buff == medals[i]:
#             same_cnt += 1
#         if country_K_medals == medals[i]:
#             print(i+1-same_cnt)
#             break
#         buff = medals[i]
N, K = map(int, input().split())
medals = []
for _ in range(N):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

target_index = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[target_index][1:] == medals[i][1:]:
        print(i + 1)
        break


'''
TC1
2 1
1 1 0 0
2 1 0 0

TC2
3 2
1 2 0 0
2 1 0 0
3 0 0 0

TC3: 반례
6 1
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

6 2
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

6 3
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

6 4
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

6 5
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

6 6
1 11 0 0
2 11 0 0
3 5 0 0
4 2 0 0
5 5 0 0
6 0 0 0

3 1
1 0 0 0
2 0 0 0
3 0 0 0
'''