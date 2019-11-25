from datetime import date


def voto(birthday):
    age = date.today().year - birthday
    if age < 16:
        return f'Com {age} anos: NÃO VOTA.'
    elif age >= 65 or 16 <= age < 18:
        return f'Com {age} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
