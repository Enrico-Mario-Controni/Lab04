class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.lista_cabine = []
        self.lista_clienti = []


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

        from cabine import Cabine
        from passeggeri import Passeggeri

        import csv
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row[0])>3 :
                        cabina= Cabine(
                        id_cab = row[0],
                        n_letti = row[1],
                        ponte = row[2],
                        prezzo = row[3],
                        deluxe= row[4] if len(row) > 4 and row[4].isdigit() else "null",
                        n_animali=row[4] if len(row) > 4 and not row[4].isdigit() else "null")

                        self.lista_cabine.append(cabina)

                    else:
                        cliente= Passeggeri(
                        id_cliente=row[0],
                        nome_cliente=row[1],
                        cognome_cliente=row[2])
                        self.lista_clienti.append(cliente)



        except FileNotFoundError:
            print("File not found")


        for c in self.lista_cabine:
            print(c)
        for p in self.lista_clienti:
            print(p)


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

