'''
   https://school.programmers.co.kr/learn/courses/30/lessons/42748

   배열의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때 k번째 수
'''

def solution(array, commands):
    answer = []

    for cmd in commands:
        i, j, k = cmd
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])

    return answer

if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, cmd))