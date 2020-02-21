# given 'AABCDEBBBEE' - return BBB - 3
# given 'AACD' - return AA-2
def longest_subsequence(s):
    max_count = 0
    prev_char = None
    max_char = None

    for current_char in s:
        if current_char == prev_char:
            count += 1
        else:
            count = 1
        if max_count < count:
            max_count = count
            max_char = current_char
        prev_char = current_char
    return {max_char: max_count}

print(longest_subsequence('AACC'))

