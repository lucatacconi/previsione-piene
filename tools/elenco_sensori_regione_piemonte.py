import os
import sys
import requests
import hashlib
import json

from dotenv import load_dotenv
load_dotenv()

file_destinazione_nome = "regione_piemonte_sensori.csv"
separatore = ","
fine_linea = "\n"

try:

    file_destinazione = open( os.environ.get("DATA_SRC") + '/' + file_destinazione_nome , "w")

    #Intestazione file
    file_destinazione.write("CodiceUnivocoSensore" + separatore)
    file_destinazione.write("IDsensore" + separatore)
    file_destinazione.write("Tipologia" + separatore)
    file_destinazione.write("Tipologia_aggregata" + separatore)
    file_destinazione.write("UnitaMisura" + separatore)
    file_destinazione.write("IDStazione" + separatore)
    file_destinazione.write("Nome" + separatore)
    file_destinazione.write("Quota" + separatore)
    file_destinazione.write("Provincia" + separatore)
    file_destinazione.write("DataInstallazione" + separatore)
    file_destinazione.write("Storico" + separatore)
    file_destinazione.write("Latitudine" + separatore)
    file_destinazione.write("Longitudine")
    file_destinazione.write(fine_linea)

    elementi_letti = 0


    apiUrl = os.environ.get("ARPA_PIEMONTE_ELENCO_SENSORI")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    dataResponse = response.json()

    if 'features' not in dataResponse:
        raise Exception("Errore connessione al server dati. (2)")

    for stazione in dataResponse['features']:

        if 'properties' not in stazione:
            continue

        if 'geometry' not in stazione:
            continue

        if 'coordinates' not in stazione['geometry']:
            continue

        latitudine = stazione['geometry']['coordinates'][1]
        longitudine = stazione['geometry']['coordinates'][0]
        id_stazione = stazione['properties']['sensor']
        nome = stazione['properties']['name']
        quota = stazione['properties']['quote']
        provincia = stazione['properties']['province_sign']
        data_installazione = stazione['properties']['date_validity']
        storico = stazione['properties']['date_start_publication']


        for codice_tipo_sensore, sensore in stazione['properties']['sensors'].items():

            chiave_sensore = id_stazione +'-'+ codice_tipo_sensore

            codice_univoco_sensore = hashlib.md5((id_stazione + codice_tipo_sensore).encode()).hexdigest()
            file_destinazione.write(codice_univoco_sensore + separatore)

            tipologia_aggregata = ''
            descrizione_sensore = codice_tipo_sensore
            unita_misura = ''

            file_destinazione.write(chiave_sensore + separatore)
            file_destinazione.write(descrizione_sensore + separatore)
            file_destinazione.write(tipologia_aggregata + separatore)
            file_destinazione.write(unita_misura + separatore)
            file_destinazione.write(id_stazione + separatore)
            file_destinazione.write(nome + separatore)
            file_destinazione.write(str(quota) + separatore)
            file_destinazione.write(provincia + separatore)
            file_destinazione.write(data_installazione + separatore)
            file_destinazione.write(storico + separatore)
            file_destinazione.write(str(latitudine) + separatore)
            file_destinazione.write(str(longitudine))
            file_destinazione.write(fine_linea)

            elementi_letti += 1

    print("Letti " + str(elementi_letti) + " dettagli sensore.")

    file_destinazione.close()

except Exception as e:
    print(e)
