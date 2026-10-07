from Strumento import Strumento

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.__responsabile = responsabile

        @property
        def responsabile(self):
            return self.__responsabile

        @responsabile.setter
        def responsabile(self, responsabile):
            self.__responsabile = responsabile
            print("Il nome del responsabile è stato aggiornato correttamente!")

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        strumenti = []
        with open(file_path, "r", encoding='utf-8') as f:
            for riga in f:
                riga = riga.strip()
                if riga:
                    continue
                campi = riga.split(',')
                if len(campi) >= 6:
                    s = Strumento(campi[0], campi[1], campi[2], campi[3], campi[4], campi[5])
                    strumenti.append(s)
                else:
                    print('Alla riga mancano dei campi')
        return strumenti

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
