tuple = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
         'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for elements in range(0, len(tuple)):
    print(f'Na palavra {tuple[elements]} temos ', end='')
    for letter in tuple[elements]:
        if letter in 'AEIOU':
            print(f'{letter.lower()}', end=' ')
    print('')
