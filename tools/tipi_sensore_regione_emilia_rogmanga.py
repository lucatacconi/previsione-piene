import os
import sys
import json
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "regione_emilia_romagna_tipi_sensore.csv"

try:

    #Lettura del file con le definizioni localBTableIT

    if not os.path.exists(os.environ.get("LOCAL_B_TABLE_SRC")):
        raise Exception("File elenco LOCAL B TABLE non trovato")

    local_B_table_file = open( os.environ.get("LOCAL_B_TABLE_SRC"), 'r')

    local_B_table = local_B_table_file.read()

    if not local_B_table:
        raise Exception("File elenco LOCAL B TABLE vuoto")

    local_B_table_file.close()


    json_object = json.loads(local_B_table)


    print(local_B_table)


except Exception as e:
    print(e)
