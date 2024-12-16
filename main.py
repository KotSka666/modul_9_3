first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))

