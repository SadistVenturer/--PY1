my_dict = {}
def get_count_char(str_):
    str_ = str_.lower()
    for sym in str_:
        sym_count = str_.count(sym)
        if sym.isalpha() and not my_dict.get(sym):
            my_dict[sym] = sym_count
    return my_dict
main_str = """
Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
def get_procent_char(my_dict_):
    counter = sum(my_dict_.values())
    for sym in my_dict_:
        my_dict_[sym] = round(my_dict_[sym] * 100 / counter, 2)
    return my_dict_
print(get_procent_char(my_dict))
