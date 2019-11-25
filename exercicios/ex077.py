tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
for c in range(0, len(tupla)):
    print(f'Na palavra {(tupla[c]).upper()} temos', end=' ')
    for d in range(0, len(tupla[c])):
        if tupla[c][d] in 'aeiou':
            print(tupla[c][d], end=' ')
    print('')
