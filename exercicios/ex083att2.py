expressao = str(input('Digite a expressão: ')).strip()
pilha = []
for símb in expressao:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão está válida!')
else:
    print('Expressão está errada!')
