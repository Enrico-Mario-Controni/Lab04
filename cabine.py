
class Cabine:

    def __init__(self, id_cab, n_letti, ponte, prezzo):
        self.__id_cab = id_cab
        self.__n_letti = n_letti
        self.__ponte = ponte
        self.__prezzo = prezzo
        self.__lista_cabine= []

    @property
    def lista_cabine(self):
        return self.__lista_cabine

    @lista_cabine.setter
    def lista_cabine(self, lista_cabine):
        self.__lista_cabine = lista_cabine

    def __str__(self):
        return (f"{self.__id_cab},  {self.__n_letti},{self.__ponte},"
                f" {self.__prezzo})")

class Cabine_animali(Cabine):
    def __init__(self, n_letti, ponte, prezzo, id_cab,n_animali):
        super().__init__(id_cab, n_letti, ponte, prezzo)
        self.__n_animali = n_animali


class Cabine_deluxe(Cabine):
    def __init__(self, id_cab, n_letti, ponte, prezzo, deluxe,):
        super().__init__(id_cab,n_letti, ponte, prezzo)
        self.__deluxe = deluxe