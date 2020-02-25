# Given example 2 strings - bisect, secret
# find the longest common substring.
# here 'sec' is the common one and longest one.
# refer image longest_common_sub_string_image.png

def LCW(u,v):
    for r in range(len(u)+1):
        print(LCW[r][len(v)+1])

str1 = 'bisect'
str2 = 'secret'
print(LCW(str1, str2))
