'''
BOJ 1759. 암호 만들기
https://www.acmicpc.net/problem/1759
'''

from itertools import combinations

pwd_length, alpha_count = map(int, input().split())
alphabets = list(map(str, input().split()))

combinations = list(map(sorted, list(combinations(alphabets, pwd_length))))

for combination in combinations:
    _v = 0
    _c = 0

    for word in combination:
        if word in 'aeiou':
            _v += 1
        else:
            _c += 1

    if _v >= 1 and _c >= 2:
        print(''.join(combination))