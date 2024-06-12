import os
import sys
import requests

from dotenv import load_dotenv
load_dotenv()

fileDestName = "regione_piemonte_tipi_sensore.csv"

try:

    fileDest = open( os.environ.get("DATA_SRC") + '/' + fileDestName , "w")

    fileDest.write("Tipo Sensore\n")

except Exception as e:
    print(e)
