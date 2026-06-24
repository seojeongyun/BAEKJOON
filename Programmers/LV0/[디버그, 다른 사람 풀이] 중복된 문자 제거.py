'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120888
    [1] dict.fromkeys(my_string): string에 적용하면 {'p': None, 'e': None, 'o': None, 'l': None} return
        - 알파벳 순서 보존, 중복 제거
'''

def solution(my_string):
    removed = 0
    lst = []
    my_string_lst = list(my_string)
    for i, char in enumerate(my_string):
        if char in lst:
            del my_string_lst[i-removed]
            removed += 1
        else:
            lst.append(char)
    answer = ''.join(my_string_lst)
    return answer

print(solution("people"))


'''
    def solution(my_string):
        answer = ''
        for i in my_string:
            if i not in answer:
                answer += i
        return answer
'''