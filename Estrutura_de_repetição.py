import requests

url = 'https://viacep.com.br/ws/'
cep_base = 30140071
formato = '/json/'

for i in range(5):
    cep = str(cep_base + i)
    r = requests.get(url + cep + formato)
    
    if r.status_code == 200:
        print()
        print(f'CEP {cep} - JSON:')
        print(r.json())
        print()
    else:
        print(f'CEP {cep} - Nao houve sucesso na requisicao.')
