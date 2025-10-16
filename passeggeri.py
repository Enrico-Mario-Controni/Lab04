
class Passeggeri:
    def __init__(self, id_cliente, nome_cliente, cognome_cliente):
        self.__id_cliente = id_cliente
        self.__nome_cliente = nome_cliente
        self.__cognome_cliente = cognome_cliente
        self.__lista_clienti = []

    @property
    def lista_clienti(self):
        return self.__lista_clienti

    @lista_clienti.setter
    def lista_clienti(self, lista_clienti):
        self.__lista_clienti = lista_clienti

    def __str__(self):
        return (f"{self.__id_cliente},  {self.__nome_cliente}, {self.__cognome_cliente}")

