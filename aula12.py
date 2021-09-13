import requests



# def retorna_cep(cep):    
#     response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
#     print(response.status_code)
#     print(response.json())
#     print(type(response.json))
#     dados_cep = response.json()
#     return dados_cep

# def retorna_dados_pokemon(pokemon):
#     response = requests.get(f'https://pokeapi.co/api/v2/pokemon/pikachu/{pokemon')
#     dados_poke = response.json()
#     return dados_poke

def retorna_respose(url):
    respose = requests.get(url)
    return respose.text


if __name__ == '__main__':
    #retorna_cep('75900091')
    #dados_poke = retorna_dados_pokemon('pikachu')
    #print(dados_poke)
    # retorna_cep('75906865')
    respose = retorna_respose('https://www.spacedesk.net')
    print(respose)

