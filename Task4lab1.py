my_dict = {}
def get_count_char(str_):
    sym_count = 0
    str_ = ' '.join(str_.lower().split())
    for sym in str_:
        if sym.isalpha() and my_dict.get(sym, True):
            my_dict[sym] = str_.count(sym)
        if  sym_count > 1:
            return my_dict
main_str = "''"
""'"'
print(get_count_char(main_str))
