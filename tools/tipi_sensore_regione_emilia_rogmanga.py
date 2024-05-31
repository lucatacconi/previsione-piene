import os
import sys
import json
import requests

from dotenv import load_dotenv
load_dotenv()

file_destinazione_nome = "regione_emilia_romagna_tipi_sensore.csv"

try:

    #Lettura del file con le definizioni localBTableIT

    if not os.path.exists(os.environ.get("LOCAL_B_TABLE_SRC")):
        raise Exception("File elenco LOCAL B TABLE non trovato")

    local_B_table_file = open( os.environ.get("LOCAL_B_TABLE_SRC"), 'r')

    local_B_table = local_B_table_file.read()

    if not local_B_table:
        raise Exception("File elenco LOCAL B TABLE vuoto")

    local_B_table_file.close()

    local_B_table_json = json.loads(local_B_table)

    dizionario = {}
    for definizione in local_B_table_json:
        dizionario[definizione["Codice"]] = definizione

    if len(dizionario) == 0:
        raise Exception("Dizionario vuoto")


    #Lettura del file con i tipi di sensore della regione emilia romagna

    apiUrl = os.environ.get("ARPAE_EMILIA_ELENCO_SENSORI_IDROMETEOROLOGICA")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    data_response = response.text

    if not data_response:
        raise Exception("Errore connessione al server dati. (2)")

    cnt_stazioni = 0
    tipi_letti = []

    file_destinazione = open( os.environ.get("DATA_SRC") + '/' + file_destinazione_nome , "w")
    file_destinazione.write("Tipo Sensore\n")

    for stazione in data_response.split('\n'):

        if stazione == "":
            continue

        json_stazione = json.loads(stazione)

        if len(json_stazione['data']) == 0:
            raise Exception("Dati stazione mancanti:" + str(cnt_stazioni))

        for data in json_stazione['data']:

            if not 'timerange' in data.keys() or not 'vars' in data.keys() or len(data['vars']) == 0:
                continue

            for sensore in data['vars'].keys():
                if sensore in dizionario:

                    descrizione_sensore = dizionario[sensore]["Descrizione"].upper()

                    if descrizione_sensore not in tipi_letti:
                        tipi_letti.append(descrizione_sensore)
                        file_destinazione.write(descrizione_sensore + "\n")

        cnt_stazioni += 1


    apiUrl = os.environ.get("ARPAE_EMILIA_ELENCO_SENSORI_PORTATA")

    params = {}
    headers = {}

    response = requests.get(apiUrl, params = params, headers = headers)

    response.raise_for_status()  # Solleva un'eccezione per gli errori HTTP (4xx e 5xx)
    if response.status_code != 200:
        raise Exception("Errore connessione al server dati. (1)")

    data_response = response.text

    if not data_response:
        raise Exception("Errore connessione al server dati. (2)")


    file_destinazione = open( os.environ.get("DATA_SRC") + '/' + file_destinazione_nome , "w")
    file_destinazione.write("Tipo Sensore\n")

    for stazione in data_response.split('\n'):

        if stazione == "":
            continue

        json_stazione = json.loads(stazione)

        if len(json_stazione['data']) == 0:
            raise Exception("Dati stazione mancanti:" + str(cnt_stazioni))

        for data in json_stazione['data']:

            if not 'timerange' in data.keys() or not 'vars' in data.keys() or len(data['vars']) == 0:
                continue

            for sensore in data['vars'].keys():
                if sensore in dizionario:

                    descrizione_sensore = dizionario[sensore]["Descrizione"].upper()

                    if descrizione_sensore not in tipi_letti:
                        tipi_letti.append(descrizione_sensore)
                        file_destinazione.write(descrizione_sensore + "\n")

        cnt_stazioni += 1

    print("Trovati " + str(len(tipi_letti)) + " tipi di sensori.")

    file_destinazione.close()

except Exception as e:
    print(e)
