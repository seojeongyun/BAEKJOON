'''
    https://school.programmers.co.kr/learn/courses/30/lessons/181944
    [1] formatting 방식 - 나는 ''.format()을 사용 / 다른 사람은 f"{}"을 사용
'''

a = int(input())
if a % 2 == 0:
    print('{} is even'.format(a))
else:
    print('{} is odd'.format(a))

'''
    N = int(input())
    print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")
'''