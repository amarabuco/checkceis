import urllib.request
import urllib.request
import json
import numpy as np
import pandas as pd


def getCeis(cnpj, chave):
    url = 'https://portaldatransparencia.cgu.gov.br/api-de-dados/ceis?codigoSancionado='+cnpj+'&pagina=1'
    headers = {'chave-api-dados': chave}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        result = response.read()

    print(result)
    return result


def getContratos(ente, exercicio):

    with urllib.request.urlopen('http://app.tce.ma.gov.br/tce/api/contratos?enteId='+ente+'&exercicio='+exercicio) as response:
        result = response.read()

    contratos = json.loads(result, encoding='utf-8')['content']

    cnpjs = set([contrato['fornecedor']['cpfCnpj']
                 for contrato in contratos])

    ceis = set([getCeis(cnpj, 'chave')
                for cnpj in cnpjs])

    print(ceis)

    with open('ceis.txt', 'w') as f:
        f.write(str(ceis))


getContratos('1', '2020')
