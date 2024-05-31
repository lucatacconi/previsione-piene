import os
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "arpa_veneto_sensori.csv"
separatore = ","
fineLinea = "\n"

try:

    fileDest = open( os.environ.get("DATA_SRC") + '/' + fileDestName , "w")

    #Intestazione file
    fileDest.write("IDsensore" + separatore)
    fileDest.write("Tipologia" + separatore)
    fileDest.write("UnitaMisura" + separatore)
    fileDest.write("IDStazione" + separatore)
    fileDest.write("Nome" + separatore)
    fileDest.write("Quota" + separatore)
    fileDest.write("Provincia" + separatore)
    fileDest.write("DataInstallazione" + separatore)
    fileDest.write("Storico" + separatore)
    fileDest.write("Latitudine" + separatore)
    fileDest.write("Longitudine")
    fileDest.write(fineLinea)

    elementiLetti = 0


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

        fileDest.write(str(sensore['codseqst']) + separatore)
        fileDest.write(sensore['nome_sensore'] + separatore)
        fileDest.write(sensore['misura'] + separatore)
        fileDest.write(str(sensore['codice_stazione']) + separatore)
        fileDest.write(sensore['nome_stazione'] + separatore)
        fileDest.write(str(sensore['quota']) + separatore)
        fileDest.write(sensore['provincia'] + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latitudine']) + separatore)
        fileDest.write(str(sensore['longitudine']))
        fileDest.write(fineLinea)

        elementiLetti += 1


    # Sensori vento
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

        fileDest.write(str(sensore['codseqst']) + separatore)
        fileDest.write(sensore['nome_sensore'] + separatore)
        fileDest.write(sensore['misura'] + separatore)
        fileDest.write(str(sensore['codice_stazione']) + separatore)
        fileDest.write(sensore['nome_stazione'] + separatore)
        fileDest.write(str(sensore['quota']) + separatore)
        fileDest.write(sensore['provincia'] + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latitudine']) + separatore)
        fileDest.write(str(sensore['longitudine']))
        fileDest.write(fineLinea)

        elementiLetti += 1


    # Sensori portata
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

        fileDest.write(str(sensore['codseqst']) + separatore)
        fileDest.write(sensore['nome_sensore'] + separatore)
        fileDest.write(sensore['misura'] + separatore)
        fileDest.write(str(sensore['codice_stazione']) + separatore)
        fileDest.write(sensore['nome_stazione'] + separatore)
        fileDest.write(str(sensore['quota']) + separatore)
        fileDest.write(sensore['provincia'] + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latitudine']) + separatore)
        fileDest.write(str(sensore['longitudine']))
        fileDest.write(fineLinea)

        elementiLetti += 1


    # Sensori precipitazioni
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

        fileDest.write(str(sensore['codseqst']) + separatore)
        fileDest.write(sensore['nome_sensore'] + separatore)
        fileDest.write(sensore['misura'] + separatore)
        fileDest.write(str(sensore['codice_stazione']) + separatore)
        fileDest.write(sensore['nome_stazione'] + separatore)
        fileDest.write(str(sensore['quota']) + separatore)
        fileDest.write(sensore['provincia'] + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latitudine']) + separatore)
        fileDest.write(str(sensore['longitudine']))
        fileDest.write(fineLinea)

        elementiLetti += 1

    # Sensori laguna di Venezia ========================================================================================================

    posizione_sensori = {}

    # Sensori livello marea

    apiUrl = os.environ.get("VENEZIA_ELENCO_SENSORI_LIVELLO_MAREA")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    for sensore in dataResponse:

        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write('Livello marea' + separatore)
        fileDest.write('m' + separatore)
        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write(sensore['stazione'] + separatore)
        fileDest.write('0' + separatore)
        fileDest.write('VE' + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latDDN']) + separatore)
        fileDest.write(str(sensore['lonDDE']))
        fileDest.write(fineLinea)

        posizione_sensori[str(sensore['ID_stazione'])] = (str(sensore['latDDN']), str(sensore['lonDDE']))

        elementiLetti += 1


    # Sensori onda di laguna

    apiUrl = os.environ.get("VENEZIA_ELENCO_SENSORI_ONDA_LAGUNA")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    for sensore in dataResponse:

        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write('Onda di laguna' + separatore)
        fileDest.write('m' + separatore)
        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write(sensore['stazione'] + separatore)
        fileDest.write('0' + separatore)
        fileDest.write('VE' + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latDDN']) + separatore)
        fileDest.write(str(sensore['lonDDE']))
        fileDest.write(fineLinea)

        posizione_sensori[str(sensore['ID_stazione'])] = (str(sensore['latDDN']), str(sensore['lonDDE']))

        elementiLetti += 1


    # Sensori onda fuori laguna

    apiUrl = os.environ.get("VENEZIA_ELENCO_SENSORI_ONDA_MARE")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    for sensore in dataResponse:

        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write('Onda fuori laguna' + separatore)
        fileDest.write('m' + separatore)
        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write(sensore['stazione'] + separatore)
        fileDest.write('0' + separatore)
        fileDest.write('VE' + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(sensore['latDDN']) + separatore)
        fileDest.write(str(sensore['lonDDE']))
        fileDest.write(fineLinea)

        posizione_sensori[str(sensore['ID_stazione'])] = (str(sensore['latDDN']), str(sensore['lonDDE']))

        elementiLetti += 1


    # Sensori vento

    apiUrl = os.environ.get("VENEZIA_ELENCO_SENSORI_VENTO")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    for sensore in dataResponse:

        latDDN = ''
        lonDDE = ''

        if str(sensore['ID_stazione']) in posizione_sensori:
            latDDN, lonDDE = posizione_sensori[str(sensore['ID_stazione'])]
        else:
            continue

        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write('Direzione vento' + separatore)
        fileDest.write('m' + separatore)
        fileDest.write(str(sensore['ID_stazione']) + separatore)
        fileDest.write(sensore['stazione'] + separatore)
        fileDest.write('0' + separatore)
        fileDest.write('VE' + separatore)
        fileDest.write('' + separatore)
        fileDest.write('' + separatore)
        fileDest.write(str(latDDN) + separatore)
        fileDest.write(str(lonDDE))
        fileDest.write(fineLinea)

        elementiLetti += 1

    print("Letti " + str(elementiLetti) + " dettagli sensore.")

    fileDest.close()

except Exception as e:
    # print(e.__doc__)
    print(e.message)
