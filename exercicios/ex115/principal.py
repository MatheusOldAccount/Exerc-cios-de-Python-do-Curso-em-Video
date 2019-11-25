from ex115.menu import men
import ex115.arquivo

while True:
    escolha = men()
    if escolha == 3:
        break
    elif escolha == 1:
        ex115.arquivo.verPessoas()
    else:
        ex115.arquivo.adicionarPessoas()
print('-' * 30)
print(f'{"Saindo do sistema... Até logo!":^30}')
print('-' * 30)
