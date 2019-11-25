from random import choice
pedra = 'PEDRA'
papel = 'PAPEL'
tisoura = 'TESOURA'
lista = [pedra, papel, tisoura]
pc = choice(lista)
escolha = str(input('Digite: Pedra / Papel / Tesoura? ').strip())
tratando = escolha.upper()
if tratando == pc:
    print('Empate! Ambos escolheram {}'.format(escolha.capitalize()))
elif tratando == 'PEDRA' and pc == 'TESOURA':
    print('Venceu! Você escolheu Pedra e a Máquina Tesoura')
elif tratando == 'PEDRA' and pc == 'PAPEL':
    print('Perdeu! Você escolheu Pedra e a Máquina Papel')
elif tratando == 'TESOURA' and pc == 'PAPEL':
    print('Venceu! Você escolheu Tesoura e a Máquina Papel')
elif tratando == 'TESOURA' and pc == 'PEDRA':
    print('Perdeu! Você escolheu Tesoura e a Máquina Pedra')
elif tratando == 'PAPEL' and pc == 'PEDRA':
    print('Venceu! Você escolheu Papel e a Máquina Pedra')
elif tratando == 'PAPEL' and pc == 'TESOURA':
    print('Perdeu! Você escolheu Papel e a Máquina Tesoura')
