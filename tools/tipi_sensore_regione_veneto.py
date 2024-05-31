import os
import sys
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "regione_veneto_tipi_sensore.csv"

try:
    fileDest = open( os.environ.get("DATA_SRC") + '/' + fileDestName , "w")

    fileDest.write("Tipo Sensore\n")

    tipiLetti = []

    # Livello idrometrico
    apiUrl = os.environ.get("ARPA_VENETO_ELENCO_SENSORI_LIVELLO_IDROMETRICO")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    if dataResponse['success'] != True:
        raise Exception("Errore connessione al server dati. (2)")

    for sensore in dataResponse['data']:
        if sensore['nome_sensore'] not in tipiLetti:
            tipiLetti.append(sensore['nome_sensore'])
            fileDest.write(sensore['nome_sensore'] + "\n")


    # Sensore vento
    apiUrl = os.environ.get("ARPA_VENETO_ELENCO_SENSORI_VENTO")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    if dataResponse['success'] != True:
        raise Exception("Errore connessione al server dati. (2)")

    for sensore in dataResponse['data']:
        if sensore['nome_sensore'] not in tipiLetti:
            tipiLetti.append(sensore['nome_sensore'])
            fileDest.write(sensore['nome_sensore'] + "\n")


    # Portata
    apiUrl = os.environ.get("ARPA_VENETO_ELENCO_SENSORI_PORTATA")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    if dataResponse['success'] != True:
        raise Exception("Errore connessione al server dati. (2)")

    for sensore in dataResponse['data']:
        if sensore['nome_sensore'] not in tipiLetti:
            tipiLetti.append(sensore['nome_sensore'])
            fileDest.write(sensore['nome_sensore'] + "\n")


    # Precipitazioni
    apiUrl = os.environ.get("ARPA_VENETO_ELENCO_SENSORI_PRECIPITAZIONE")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    if dataResponse['success'] != True:
        raise Exception("Errore connessione al server dati. (2)")

    for sensore in dataResponse['data']:
        if sensore['nome_sensore'] not in tipiLetti:
            tipiLetti.append(sensore['nome_sensore'])
            fileDest.write(sensore['nome_sensore'] + "\n")



    print("Trovati " + str(len(tipiLetti)) + " tipi di sensori.")

    fileDest.close()

except Exception as e:
    # print(e.__doc__)
    print(e.message)
