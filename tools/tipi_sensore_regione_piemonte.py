import os
import sys
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "regione_piemonte_tipi_sensore.csv"

try:

    fileDest = open( os.environ.get("DATA_SRC") + '/' + fileDestName , "w")

    fileDest.write("Tipo Sensore\n")

    tipiLetti = []


    apiUrl = os.environ.get("ARPA_PIEMONTE_ELENCO_SENSORI")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    for stazione in dataResponse['features']:

        for key, sensore in stazione['properties']['sensors'].items():
            if key not in tipiLetti:
                tipiLetti.append(key)
                fileDest.write(key + "\n")

    print("Trovati " + str(len(tipiLetti)) + " tipi di sensori.")

    fileDest.close()

except Exception as e:
    print(e)
