import flet as ft
#from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view, model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        lista_musei=self._model.get_musei()
        self._view._dd_museo.options.clear()
        for museo in lista_musei:
            self._view._dd_museo.options.append(ft.dropdown.Option(museo.nome))
        self._view.update()
    def on_change_museo(self,e):
        self.museo_selezionato = e.control.value

    def popola_epoche(self):
        lista_epoche=self._model.get_epoche()
        self._view._dd_epoca.options.clear()
        for epoca in lista_epoche:
            self._view._dd_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.update()

    def on_change_epoche(self,e):
        self.epoca_selezionata = e.control.value


    def mostra_artefatti(self,e):
      lista_art=self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)
      self._view.lista_art.controls.clear()
      if not lista_art:
            self._view.lista_art.controls.append(ft.Text('Nessun artefatto trovato'))
      else:
          for a in lista_art:
              self._view.lista_art.controls.append(ft.Text(a))
      self._view.update()

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
