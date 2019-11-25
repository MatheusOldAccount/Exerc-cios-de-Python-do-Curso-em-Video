def escreva(*txt):
    tam = len(txt[0]) + 4
    print('~' * tam)
    print(f'  {txt[0]}  ')
    print('~' * tam)


escreva('Olá, Mundo!')
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
