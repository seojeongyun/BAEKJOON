'''
    https://school.programmers.co.kr/learn/courses/30/lessons/42746

    양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수
'''

# def permutation(lst, n):
#     result = []
#
#     if n == 0:
#         return [[]]
#
#     for i, elem in enumerate(lst):
#         for P in permutation(lst[:i] + lst[i+1:], n-1):
#             result += [[elem]+P]
#
#     return result

def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(num_str)))

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))

'''
TC1
[6, 10, 2]
6 2 10

TC2
[3, 30, 34, 5, 9]
9 5 34 3 30
'''