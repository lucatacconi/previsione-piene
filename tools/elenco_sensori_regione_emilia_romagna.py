import os
import sys
import requests

from dotenv import load_dotenv
load_dotenv()

file_destinazione_nome = "regione_emilia_romagna_sensori.csv"
separatore = ","
fine_linea = "\n"

try:

    file_destinazione = open( os.environ.get("DATA_SRC") + '/' + file_destinazione_nome , "w")

    #Intestazione file
    file_destinazione.write("IDsensore" + separatore)
    file_destinazione.write("Tipologia" + separatore)
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


except Exception as e:
    print(e)
