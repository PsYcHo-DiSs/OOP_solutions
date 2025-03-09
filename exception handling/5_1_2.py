def is_int(s):
    return s.lstrip('-').isdigit()

lst_in = input().split()

res = sum(map(int, filter(is_int, lst_in)))
print(res)