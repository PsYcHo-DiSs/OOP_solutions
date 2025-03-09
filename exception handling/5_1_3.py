def convert(value):
    for T in (int, float, str):
        try:
            return T(value)
        except:
            pass


lst_in = input().split()
lst_out = [convert(x) for x in lst_in]
