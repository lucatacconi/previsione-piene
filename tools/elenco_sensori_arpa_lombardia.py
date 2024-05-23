import os
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "arpa_lombardia_sensori.csv"
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

    limit = 1000
    offset = 0
    dataCheck = True
    elementiLetti = 0

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

        # Conta il numero di elementi nell'array
        numContents = len(dataResponse)
        if numContents == 0:
            dataCheck = False
        else:

            for sensore in dataResponse:

                fileDest.write(sensore['idsensore'] + separatore)
                fileDest.write(sensore['tipologia'] + separatore)
                fileDest.write(sensore['unit_dimisura'] + separatore)
                fileDest.write(sensore['idstazione'] + separatore)
                fileDest.write(sensore['nomestazione'] + separatore)
                fileDest.write(sensore['quota'] + separatore)
                fileDest.write(sensore['provincia'] + separatore)
                fileDest.write(sensore['datastart'] + separatore)
                fileDest.write(sensore['storico'] + separatore)
                fileDest.write(sensore['lat'] + separatore)
                fileDest.write(sensore['lng'])
                fileDest.write(fineLinea)

                elementiLetti += 1

            offset += 1000

    print("Letti " + str(elementiLetti) + " dettagli sensore.")

    fileDest.close()

except Exception as e:
    # print(e.__doc__)
    print(e.message)
