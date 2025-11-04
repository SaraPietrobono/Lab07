from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo
import database.DB_connect

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass
    @staticmethod
    def read_museo():
        results=[]
        cnx = database.DB_connect.ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection failed')
            return None
        else:
            cursor = cnx.cursor()
            query = """SELECT * FROM museo"""  # mi seleziono tutti gli artefatti nella tabella torino
            cursor.execute(query)
            for row in cursor:
                musei = Museo(row['id'],
                               row['nome'],
                                      row['tipologia'])
                results.append(musei)
            cursor.close()
            cnx.close()
            return results


