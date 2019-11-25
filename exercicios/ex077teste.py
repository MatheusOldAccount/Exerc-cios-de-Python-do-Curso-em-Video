palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in range(0, len(palavras)):
    print(f'Na palavra {palavras[palavra].upper()} temos: ', end='')
    for letter in palavras[palavra]:
        if letter.lower() in 'aeiou':
            print(f'{letter.lower()} ', end='')
    print()
