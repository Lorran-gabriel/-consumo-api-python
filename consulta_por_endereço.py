import requests

# Estado, cidade e nome da rua
uf = 'MG'
cidade = 'Belo Horizonte'
rua = 'Rua dos Aimores'

url = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'

r = requests.get(url)

if r.status_code == 200:
    resultados = r.json()  # a resposta é uma lista de registros
    print(f'\nForam encontrados {len(resultados)} resultados para {rua}, {cidade} - {uf}:\n')
    
    for endereco in resultados:
        print(f"CEP: {endereco['cep']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"UF: {endereco['uf']}")
        print('-'*40)
else:
    print('Não houve sucesso na requisição.')
