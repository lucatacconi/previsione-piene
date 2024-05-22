import os
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "arpa_lombardia_sensori.csv"

try:
    fileDest = open( os.environ.get("DATA_SRC") + '/' + fileDestName , "w")

    f.write("Tipo Sensore\n")

    limit = 1000
    offset = 0
    dataCheck = True

    while dataCheck:

        apiUrl = os.environ.get("ARPA_LOMBARDIA_ELENCO_SENSORI")
        apiUrl += "?$limit=" + str(limit) + "&$offset=" + str(offset)

        params = {}
        headers = {}

        response = requests.get(apiUrl, params = params, headers = headers)

        response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
        if response.status_code != 200:
            raise Exception("Errore connessione al server dati.")

        dataResponse = response.json()

        # Verifica che data sia una lista
        if isinstance(dataResponse, list):
            # Conta il numero di elementi nell'array
            numContents = len(dataResponse)
            if numContents == 0:
                dataCheck = False
            else:
                print(f"L'array contiene {numContents} elementi. {offset}")
                offset += 1000

        else:
            dataCheck = False

    print("Fine")

    fileDest.close()

except Exception as e:
    print(f"Errore: {e}")
