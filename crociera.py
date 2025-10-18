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
                                prezzo=int(row[3]))
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

        if self.lista_prenotazioni == []:
            for c in self.lista_cabine:
                quadro_camere= Prenotazioni("null", c.id_cab, True)
                self.lista_prenotazioni.append(quadro_camere)

        cab_trovata=False
        for c in self.lista_cabine:
            if c.id_cab == codice_cabina:
                cab_trovata=True
                break
            else:
                cab_trovata=False

        cliente_trovato=False
        for cliente in self.lista_clienti:
            if cliente.id_cliente == codice_passeggero:
                cliente_trovato=True
                break

            else:
                cliente_trovato=False

        for pren in self.lista_prenotazioni:
            if pren.id_cliente == codice_passeggero:
                raise Exception(f"Il passeggero {codice_passeggero} è già assegnato alla cabina {pren.id_cabine}")


        trovato=False
        if cab_trovata and cliente_trovato:
            for book in self.lista_prenotazioni:
                if book.id_cabine == codice_cabina:
                    trovato = True
                    if book.disponibilita:
                        book.id_cliente = codice_passeggero
                        book.disponibilita = False

                    else:
                        raise Exception ("la cabina è già occupata")
                    break

        if trovato == False:
            raise Exception( "non è stata trovata la cabina o il passeggero")

        for el in self.lista_prenotazioni:
            print(el)



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        self.lista_cabine.sort(key=lambda x: x.prezzo)
        return self.lista_cabine

    def __str__(self):
        return (f"{self.lista_cabine}")



    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for clienti in self.lista_clienti:
            cabina_trovata=False
            for prenotazioni in self.lista_prenotazioni:
                if prenotazioni.id_cliente == clienti.id_cliente:
                    print(f"passeggero: {prenotazioni.id_cliente}, cabina assegnata {prenotazioni.id_cabine}")
                    cabina_trovata=True
                    break

            if cabina_trovata == False:
                print(f"Passeggero: {clienti.id_cliente} non ha una cabina assegnata")






