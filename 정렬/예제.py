lst = [4,2,1,3,1]

sorted_lst = sorted(lst)
print(' '.join(map(str, sorted_lst)))
print(' '.join(map(str, lst)))

lst.sort()
print(' '.join(map(str, lst)))


eat = [
    ('Chicken', 17900, 'Puradak'),
    ('Pizza', 21000, 'Domino'),
    ('Spagetti', 12000, 'Mola')
]

eat = sorted(eat, key=lambda x: x[1])
print(eat)

eat = sorted(eat, key=lambda x: x[1], reverse=True)
print(eat)

eat.sort(key=lambda x: x[0])
print(eat)

lst1 = [21, 51, 4, 31, 2]
lst2 = [12, 24, 3, 53, 29]

dct = dict(zip(lst1, lst2))
print(dct)
print(sorted(dct))

sorted_dict = sorted(dct.items())
print(sorted_dict)

for k, v in sorted_dict:
    print('dictionary[{}] = {}'.format(k, v))


from collections import deque
if __name__ == '__main__':
    DQ = deque([1,2,3,4])
    DQ.popleft()
    print(DQ[0])

