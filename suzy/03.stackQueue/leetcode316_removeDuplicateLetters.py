# Leetcode 316. Remove Duplicate Letters

# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# queue
# input : bcabc
# b
# bc
# bca
# (b)cab
# (b,c)abc
import collections

def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char,''))
    return ''

def removeDuplicateLetters_stack(s):
    counter, seen, stack = collections.Counter(s), set(s), []
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)

# deque --- wrong answer
def removeDuplicateLetters_deque(s):
    deq = collections.deque([])

    for char in s:
        if char in deq:
            deq.remove(char)
            deq.append(char)
        else:
            deq.append(char)

    return "".join(deq)

# set -- cbacdcbc : wrong answer
def removeDuplicateLetters_set(s):
    return "".join(sorted(list(set(s))))

if __name__ == "__main__":
    # Input: s = "bcabc"
    # Output: "abc"
    s = "bcabc"
    print("input >>> ", s)
    print(removeDuplicateLetters(s))

    # "cbacdcbc"
    # adbc
    # Input: s = "cbacdcbc"
    # Output: "acdb"
    s = "cbacdcbc"
    print("input >>> ", s)
    print(removeDuplicateLetters(s))
