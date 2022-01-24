'''
BOJ 1759. 암호 만들기
https://www.acmicpc.net/problem/1759
'''

# DFS
def dfs(words, path, limit, vows, cons):
    if len(path) > limit:
        return

    if len(path) == limit and vows >= 1 and cons >= 2:
        result.append(path)

    for i in range(len(words)):
        if words[i] in "aeiou":
            dfs(words[i + 1:], path + words[i], limit, vows + 1, cons)
        else:
            dfs(words[i + 1:], path + words[i], limit, vows, cons + 1)


pwd_length, alpha_count = map(int, input().split())
alphabets = sorted(input().split())

result = []
dfs(alphabets, "", pwd_length, 0, 0)

print(result)