import os
import requests

from dotenv import load_dotenv
load_dotenv()

file_dest = "arpa_lombardia_sensori.csv"

try:
    file_dest = open( os.environ.get("DATA_SRC") + '/' + file_dest , "w")



    file_dest.close()

except:
    print("An exception occurred")

# print(os.environ.get("ARPA_LOMBARDIA_ELENCO_SENSORI"))

