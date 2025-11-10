from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        lista_artefatti=[]
        musei=self._museo_dao.read_museo()
        artefatti=self._artefatto_dao.read_artefatti()
        id_museo=None
        for m in musei:
            if m.nome==museo:
                id_museo=m.id
                break
        for a in artefatti:
            if (id_museo is None or a.id_museo==id_museo) and (not epoca or a.epoca==epoca):
                lista_artefatti.append(a)
        return lista_artefatti

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lst_epoche=[]
        for art in self._artefatto_dao.read_artefatti():
            if art.epoca not in lst_epoche:
                lst_epoche.append(art.epoca)
        return lst_epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        return self._museo_dao.read_museo()


