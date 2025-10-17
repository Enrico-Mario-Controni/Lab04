from cabine import *
from passeggeri import Passeggeri
from prenotazioni import Prenotazioni


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.lista_cabine = []
        self.lista_clienti = []
        self.lista_prenotazioni = []

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
                    if len(row[0])>3 :
                        if len(row)> 4:
                            if row[4].isalpha():
                                id_cab = row[0]
                                n_letti = row[1]
                                ponte = row[2]
                                prezzo = int(row[3])
                                deluxe=row[4]
                                cabina=Cabine_deluxe(id_cab, n_letti, ponte, prezzo, deluxe)
                                self.lista_cabine.append(cabina)
                            else :
                                cabina=Cabine_animali(
                                id_cab=row[0],
                                n_letti=row[1],
                                ponte=row[2],
                                prezzo=int(row[3]),
                                n_animali=int(row[4]))
                                self.lista_cabine.append(cabina)

                        else:
                            cabina= Cabine(
                                id_cab=row[0],
                                n_letti=row[1],
                                ponte=row[2],
                                prezzo=row[3])
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

        for cab in self.lista_cabine:
            cabine=Prenotazioni("null", cab.id_cab, True)
            self.lista_prenotazioni.append(cabine)


        valore_trovato=False
        for cabine in self.lista_cabine:
            for cliente in self.lista_clienti:
                for prenotazioni in self.lista_prenotazioni:
                    if (codice_cabina == cabine.id_cab and codice_passeggero == cliente.id_cliente
                        and prenotazioni.disponibilita==True and prenotazioni.id_cliente!=codice_passeggero):
                        valore_trovato=True
                        break

                if valore_trovato==True:
                    break

            if valore_trovato==True:
                break

        if valore_trovato==False:
            raise Exception ("Cabine o Clienti non trovati!!!")

        for c in self.lista_prenotazioni:
            print(c)




    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO



    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO



