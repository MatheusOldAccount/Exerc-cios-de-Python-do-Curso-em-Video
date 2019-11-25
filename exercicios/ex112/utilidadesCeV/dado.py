def leiaDinheiro(txt):
    num = str(input(txt)).strip()
    vertexto = num
    while True:
        vertexto = vertexto.replace(',', '')
        vertexto = vertexto.replace('.', '')
        vertexto = vertexto.replace(' ', '')
        if not vertexto.isnumeric():
            print(f'\033[31mERRO: \"{num}\" é um preço inválido!\033[m')
            num = str(input(txt)).strip()
            vertexto = num
        else:
            break
    num = num.replace(',', '.')
    return float(num)

