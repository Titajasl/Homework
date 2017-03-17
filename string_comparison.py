# Написать функцию, которая принимает на вход 2 строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def string_comparison(string_1, string_2):

    if string_1 == string_2:
        return 1

    else:
        
        if len(string_1) > len(string_2):
            return 2

        elif string_2 == 'learn':
            return 3


string_1 = input('Напишите что-нибудь: ')
string_2 = input('Напишите что-нибудь ещё раз: ')

print(string_comparison(string_1, string_2))