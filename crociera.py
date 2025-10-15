class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome

class cabine(Crociera):
    def __init__(self, nome, id_cab, n_letti, prezzo, n_animali, deluxe):
        super().__init__(nome)
        self.__id_cab = id_cab
        self.__n_letti = n_letti
        self.__prezzo = prezzo
        self.__n_animali = n_animali
        self.__deluxe = deluxe


class passeggeri (Crociera):
    def __init__(self, nome, id_cliente,  nome_cliente, cognome_cliente):
        super().__init__(nome)
        self.__id_cliente = id_cliente
        self.__nome_cliente = nome_cliente
        self.__cognome_cliente = cognome_cliente

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        import csv
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:

        except FileNotFoundError:
            print("File not found")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

