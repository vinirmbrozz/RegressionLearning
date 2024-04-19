import requests
import pandas as pd
import json

# URL base da API
url_base = "https://api.portaldatransparencia.gov.br/api-de-dados/ceis"

headers = {
    "chave-api-dados": "aed3cc7f2c3eca9430aa2f72c83a3d26"
}

pagina = 1

df = pd.DataFrame()

data = pd.DataFrame()

while pagina < 100:
    # URL com o número da página atual
    url = f"{url_base}?pagina={pagina}"

    # Requisição GET para a API
    response = requests.get(url, headers=headers)

    # Verificar se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converter os dados de resposta para json
        data = response.json()

        data = pd.DataFrame(data)
        
        if data.empty:
            break
        # filtrar os dados quando forem depois de 2022
        data = data[data['dataFimSancao'] > '2022-01-01']
        
        # Concatenar os dados
        df = pd.concat([df, data])
        
        # Ir para a próxima página
        pagina += 1

df.to_csv('ceis.csv', index=False)
df.to_json('ceis.json', orient='records', indent=4)

print("Dados salvos com sucesso!")