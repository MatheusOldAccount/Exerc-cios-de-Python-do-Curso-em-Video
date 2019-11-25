from requests import get
try:
    get('http://www.pudiaskmoamsoasm.com.br')
except:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso!\033[m')
