fabiogay = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
fabiogayrecebe = ''
for fg in range(len(fabiogay) -1, -1, -1):
    fabiogayrecebe += fabiogay[fg]
print('O inverso da frase {} é {}'.format(fabiogay, fabiogayrecebe))
if fabiogayrecebe == fabiogay:
    print('É palíndromo')
else:
    print('Não é palíndromo')
