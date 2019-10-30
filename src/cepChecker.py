#!python3
import json
import requests
import time


def requestcodeValidation(requestCEP):
    jeison = str(json.loads(requestCEP.text).values())
    if jeison == 'dict_values([True])':
        return 'CEP não localizado'
    else:
        return 'CEP localizado'     

def checkCEP(CEP):
    if len(CEP) == 8:
        url = "https://viacep.com.br/ws/"+CEP+"/json/"
        requestCEP = requests.get(url)
        resposta = requestcodeValidation(requestCEP)
        print (resposta)
        return resposta
    else:
        print ("Número de caractéres inválido")
        return "Número de caractéres inválido"
