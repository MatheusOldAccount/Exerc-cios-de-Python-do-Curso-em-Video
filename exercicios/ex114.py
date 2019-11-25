import requests
try:
    requests.get("http://www.pudim.com.br")
except:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso!\033[m')
