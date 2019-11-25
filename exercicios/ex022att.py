nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
nomedividido = nome.split()
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomedividido[0], len(nomedividido[0])))

