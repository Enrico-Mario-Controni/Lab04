
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

    @property
    def id_cab(self):
        return self.__id_cab

    @property
    def n_letti(self):
        return self.__n_letti

    @property
    def ponte(self):
        return self.__ponte

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    def __lt__(self, other):
        return self.prezzo < other.prezzo


    def __str__(self):
        return (f"{self.__id_cab},  {self.__n_letti},{self.__ponte},"
                f" {self.__prezzo}")

class Cabine_animali(Cabine):
    def __init__(self, n_letti, ponte, prezzo, id_cab,n_animali):
        super().__init__(id_cab, n_letti, ponte, prezzo)
        self.__n_animali = n_animali
        self.prezzo = self.sovraprezzo()

    def sovraprezzo(self):
        n_animali= self.__n_animali
        prezzo = self.prezzo*(1+0.1*n_animali)
        return prezzo


    def __str__(self):
        return (f"{self.id_cab},  {self.n_letti},  {self.ponte}, {self.prezzo}, {self.__n_animali}")


class Cabine_deluxe(Cabine):
    def __init__(self, id_cab, n_letti, ponte, prezzo, deluxe,):
        super().__init__(id_cab,n_letti, ponte, prezzo)
        self.__deluxe = deluxe
        self.prezzo = self.sovraprezzo()

    def sovraprezzo(self):
        return self.prezzo*1.20

    def __str__(self):
        return (f"{self.id_cab}, {self.n_letti},  {self.ponte}, {self.prezzo}, {self.__deluxe}")
