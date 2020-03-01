def find_num(ls):
    for item in ls:
        if item in ls[item:]:
            continue
        else:
            return item

ls = [1,2,2,3,1]
print(find_num(ls))

x = {2:2, 1:2, 3:1}
x = [k for k,v in x.items() if v==1]
print(x)