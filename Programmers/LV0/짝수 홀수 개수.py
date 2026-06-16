'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120824

    주어진 숫자 리스트에서 짝수와 홀수 개수 구하기
'''

def solution(num_list):
    even = 0
    odd = 0
    for num in num_list:
        if num % 2 == 1:
            odd +=1
        else:
            even +=1
    answer = [even, odd]
    return answer

print(solution([1, 3, 5, 7]))

'''
    [다른 사람 풀이]
    def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
'''