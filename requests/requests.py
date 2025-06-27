"""
Pegar Informações - GET
Criar Informações - POST
Editar Informações - PATCH
Deletar Informações - DELETE
"""

import requests
requisicao = requests.get("")
print(requisicao) #resposta 200
print(requisicao.json()) #pegar a informação armazenada dentro da requisição

"""
INFORMAÇÃO NO FORMATO JSON
{
  "nome": "João",
  "idade": 30,
  "cidade": "São Paulo"
}

"""

