
class Prenotazioni:
    def __init__(self, id_cliente, id_cabine, disponibilita ):
        self.__id_cabine = id_cabine
        self.__id_cliente = id_cliente
        self.disponibilita = disponibilita

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    @property
    def id_cabine(self):
        return self.__id_cabine

    @id_cabine.setter
    def id_cabine(self, id_cabine):
        self.__id_cabine = id_cabine

    def __str__(self):
        return(f" ID_cabine: {self.__id_cabine}, cliente: {self.__id_cliente}, disponibilità: {self.disponibilita}")



