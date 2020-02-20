# given 1 to 26 alphabets and map 1->a , 2->b, 3->c ...
# find no.of ways to decode a given message.. e.g., given 12  
# result is 'ab' or 'l' -2 ways. 
# "" - > "" = 1 way.
# https://www.youtube.com/watch?v=qli-JCrSwuk&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

def decode(s):
    if len(s) == 0:
        return 1
    if s[0] == 0:
        return 0
    else:
        return decode(s[1:]) + decode(s[2:])
print(decode('12'))