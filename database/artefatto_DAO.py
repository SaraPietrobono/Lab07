import database.DB_connect
from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto
import mysql.connector


"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass
    @staticmethod
    def read_artefatti():
        results=[]
        cnx=database.DB_connect.ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection failed')
            return []
        else:
            cursor = cnx.cursor(dictionary=True)
            query="""SELECT * FROM artefatto""" #mi seleziono tutti gli artefatti nella tabella torino
            cursor.execute(query)
            for row in cursor:
                artefatti=Artefatto(row['id'],
                                    row['nome'],
                                    row['tipologia'],
                                    row['epoca'],
                                    row['id_museo'])
                results.append(artefatti)
            cursor.close()
            cnx.close()
            return results
