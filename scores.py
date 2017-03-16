    # список всех оценок школы по классам
scores_list = [
    {'school_class': '1', 'scores': [3,5,4,1,2,4,4,5,5,2,2]},
    {'school_class': '2', 'scores': [5,4,4,5,5,4,3,4,3,4,5,5,5,4]},
    {'school_class': '3', 'scores': [3,2,2,1,2,3,4,3,2,2,2,2,3,]},
    {'school_class': '4', 'scores': [3,4,4,3,5,3,3,3,4,2,3,4]},
    {'school_class': '5', 'scores': [4,4,2,3,2,4,5,5,1,3,4,3]},
    {'school_class': '6', 'scores': [3,2,3,5,4,3,2,1,2,5,5,4,4]},
    {'school_class': '7', 'scores': [5,5,5,5,5,5,5,5,5,5]},
    {'school_class': '8', 'scores': [4,5,2,3,1,4,5,3,4,5,5,2]},
    {'school_class': '9', 'scores': [2,3,2,3,2,3,3,2,2,3,2,1,2,1]}
    ]

    # Вычислим средний балл по школе
average_list = []                    # cписок средних баллов по классам
for note in scores_list:
    scores = note.get('scores')
    summ = 0

    for score in scores:
        summ = summ + score

    class_average = summ / len(scores)     # средний балл в классе 
    average_list.append(class_average)     # добавим средний балл в список

summ = 0                                   # вычисляем средний балл по школе
for average in average_list:         
    summ += average

school_average = summ / len(average_list)    # средний балл по школе

print('Средний балл по школе: ', round(school_average))
print('\n')
    
    
    # Вычислим средние баллы по классам
for note in scores_list:
    school_class = note.get('school_class')
    scores = note.get('scores')
    summ = 0
    
    for score in scores:
        summ = summ + score

    class_average = summ / len(scores)    # средний балл по классу

    print('Средний балл по классу {}:'.format(school_class), round(class_average))