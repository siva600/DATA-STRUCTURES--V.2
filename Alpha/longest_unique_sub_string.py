# given a string find the LONGEST SUBSTRING WITHOUT REPEATS.
# e.g.. 'abcabcbb' == 3
# https://www.youtube.com/watch?v=sZosU8JjVaA
# https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

def helper(s, start):
    seen = set()
    for i in range(start, len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            return i-start
    return len(s) - start


def max_string(s):
    max_length = 0
    for i in range(len(s)):
        max_length = max(max_length, helper(s, i))
        if max_length == len(s[i:]) or max_length > len(s[i:]):
            return max_length
    return max_length


# sliding window approach.
# initiate start, end, max_length.
def max_substring(s):
    seen = {}
    start = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] not in seen:
            seen[s[i]] = i
            if max_length <= len(s[start:i]) + 1:
                max_length = len(s[start:i]) + 1
        else:
            start = seen[s[i]] + 1
            seen[s[i]] = i

    return max_length


print(max_string("bbacbd"))
print(max_substring("pwwkew"))

