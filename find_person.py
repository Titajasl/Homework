def find_person(name):
    index = 0
    while name_list[index] != name:
        index += 1
    return name_list[index]

name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
name = 'Валера'
print(find_person(name), 'нашёлся')