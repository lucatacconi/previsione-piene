import os
import sys
import requests
import hashlib
import json

from dotenv import load_dotenv
load_dotenv()

file_destinazione_nome = "regione_emilia_romagna_sensori.csv"
separatore = ","
fine_linea = "\n"

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

    for stazione in data_response.split('\n'):

        if stazione == "":
            continue

        json_stazione = json.loads(stazione)

        if len(json_stazione['data']) == 0:
            raise Exception("Dati stazione mancanti:" + str(cnt_stazioni))

        giri = 0

        codice_univoco_sensore = ''
        id_sensore = ''
        id_stazione = ''
        nome = ''
        quota = ''
        provincia = ''
        data_installazione = ''
        storico = ''
        latitudine = ''
        longitudine = ''

        for data in json_stazione['data']:

            if giri == 0:

                codice_univoco_sensore = ''
                id_stazione = data['vars']['B01194']['v'] #ID stazione, vedi file di conversione B TABLE
                nome = data['vars']['B01019']['v'] #Nome stazione, vedi file di conversione B TABLE
                quota = str(data['vars']['B07030']['v']) #Altezza sul mare (m), vedi file di conversione B TABLE
                provincia = ''
                data_installazione = ''
                storico = ''
                unita_misura = ''
                latitudine = str(data['vars']['B05001']['v']) #Latitudine, vedi file di conversione B TABLE
                longitudine = str(data['vars']['B06001']['v']) #Longitudine, vedi file di conversione B TABLE

                # Devo normalizzare i dati della longitudine e latitudine perchè alcuni non hanno la virgola
                latitudine.replace(",", ".")
                longitudine.replace(",", ".")

                giri += 1

            else:

                if not 'timerange' in data.keys() or not 'vars' in data.keys() or len(data['vars']) == 0:
                    continue

                for sensore in data['vars'].keys():
                    if sensore in dizionario:

                        descrizione_sensore = dizionario[sensore]["Descrizione"].upper()

                        # if sensore['tipologia'] not in tipiSensoriConsentiti:
                        #     continue

                        chiave_sensore = id_stazione +'-'+ sensore +'-'+ latitudine +'-'+ longitudine

                        if chiave_sensore not in tipi_letti:
                            tipi_letti.append(chiave_sensore)

                            codice_univoco_sensore = hashlib.md5((id_stazione + sensore).encode()).hexdigest()
                            file_destinazione.write(codice_univoco_sensore + separatore)

                            tipologia_aggregata = ''

                            file_destinazione.write(chiave_sensore + separatore)
                            file_destinazione.write(descrizione_sensore + separatore)
                            file_destinazione.write(tipologia_aggregata + separatore)
                            file_destinazione.write(unita_misura + separatore)
                            file_destinazione.write(id_stazione + separatore)
                            file_destinazione.write(nome + separatore)
                            file_destinazione.write(quota + separatore)
                            file_destinazione.write(provincia + separatore)
                            file_destinazione.write(data_installazione + separatore)
                            file_destinazione.write(storico + separatore)
                            file_destinazione.write(latitudine + separatore)
                            file_destinazione.write(longitudine)
                            file_destinazione.write(fine_linea)

                            elementi_letti += 1

                giri += 1
        cnt_stazioni += 1

    #Lettura del file con i tipi di sensore della regione emilia romagna - Portata

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

    cnt_stazioni = 0

    tipi_letti = []

    for stazione in data_response.split('\n'):

        if stazione == "":
            continue

        json_stazione = json.loads(stazione)

        if len(json_stazione['data']) == 0:
            raise Exception("Dati stazione mancanti:" + str(cnt_stazioni))

        giri = 0

        codice_univoco_sensore = ''
        id_sensore = ''
        id_stazione = ''
        nome = ''
        quota = ''
        provincia = ''
        data_installazione = ''
        storico = ''
        latitudine = ''
        longitudine = ''

        for data in json_stazione['data']:

            if giri == 0:

                codice_univoco_sensore = ''
                id_stazione = data['vars']['B01194']['v'] #ID stazione, vedi file di conversione B TABLE
                nome = data['vars']['B01019']['v'] #Nome stazione, vedi file di conversione B TABLE
                quota = str(data['vars']['B07030']['v']) #Altezza sul mare (m), vedi file di conversione B TABLE
                provincia = ''
                data_installazione = ''
                storico = ''
                unita_misura = ''
                latitudine = str(data['vars']['B05001']['v']) #Latitudine, vedi file di conversione B TABLE
                longitudine = str(data['vars']['B06001']['v']) #Longitudine, vedi file di conversione B TABLE

                # Devo normalizzare i dati della longitudine e latitudine perchè alcuni non hanno la virgola
                latitudine.replace(",", ".")
                longitudine.replace(",", ".")

                giri += 1

            else:

                if not 'timerange' in data.keys() or not 'vars' in data.keys() or len(data['vars']) == 0:
                    continue

                for sensore in data['vars'].keys():
                    if sensore in dizionario:

                        descrizione_sensore = dizionario[sensore]["Descrizione"].upper()

                        # if sensore['tipologia'] not in tipiSensoriConsentiti:
                        #     continue

                        chiave_sensore = id_stazione +'-'+ sensore +'-'+ latitudine +'-'+ longitudine

                        if chiave_sensore not in tipi_letti:
                            tipi_letti.append(chiave_sensore)

                            codice_univoco_sensore = hashlib.md5((id_stazione + sensore).encode()).hexdigest()
                            file_destinazione.write(codice_univoco_sensore + separatore)

                            tipologia_aggregata = ''

                            file_destinazione.write(chiave_sensore + separatore)
                            file_destinazione.write(descrizione_sensore + separatore)
                            file_destinazione.write(tipologia_aggregata + separatore)
                            file_destinazione.write(unita_misura + separatore)
                            file_destinazione.write(id_stazione + separatore)
                            file_destinazione.write(nome + separatore)
                            file_destinazione.write(quota + separatore)
                            file_destinazione.write(provincia + separatore)
                            file_destinazione.write(data_installazione + separatore)
                            file_destinazione.write(storico + separatore)
                            file_destinazione.write(latitudine + separatore)
                            file_destinazione.write(longitudine)
                            file_destinazione.write(fine_linea)

                            elementi_letti += 1

                giri += 1
        cnt_stazioni += 1

    print("Letti " + str(elementi_letti) + " dettagli sensore.")

    file_destinazione.close()

except Exception as e:
    print(e)
