def get_answer(question):
    question = str(question).lower()
    answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}
    print(answers[question])

def ask_user():
    question = None
    while question != 'Хорошо':
        question = input('Как дела? ')
        
        try:
            get_answer(question)
        except KeyError:
            print('')
        
        if question == 'пока':
            break

try:
    ask_user()
except KeyboardInterrupt:
    print('\nВсего хорошего!')