import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        _genere = None

    def fillDDGenre(self):
        self._view._ddGenre.options.clear()
        for g in self._model.generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(
                                                                    text=g.Name,
                                                                    data=g,
                                                                    on_click=self.memogenere
            ))


    def handleCreaGrafo(self, e):
        pass

    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass

    def memogenere(self, e):
        self._genere = e.controls.data