from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti = []

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
                if not riga:
                    continue
                campi = riga.split(',')
                if len(campi) >= 5:
                    s = Strumento(campi[0], campi[1], campi[2], campi[3], campi[4])
                    strumenti.append(s)
                else:
                    print('Alla riga mancano dei campi')
        self.__strumenti = strumenti
        for s in strumenti:
            print(s)

        return strumenti

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if self.__strumenti:
            ultimo_codice = self.__strumenti[-1].codice
            num = int(ultimo_codice[1:]) + 1
        else:
            num = 1

        codice = f"S{num}"
        nuovo_strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.__strumenti.append(nuovo_strumento)
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.__strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumento_selezionato = None
        for s in self.__strumenti:
            if s.codice == id_strumento:
                strumento_selezionato = s
                break

        if not strumento_selezionato:
            raise ValueError("Strumento non trovato con questo ID.")

        if self.__prestiti:
            ultimo_codice = self.__prestiti[-1].codice
            num = int(ultimo_codice[1:]) + 1
        else:
            num = 1
        codice_prestito = f"P{num}"

        nuovo_p = Prestito(codice_prestito, strumento_selezionato, cognome_allievo, data)
        self.__prestiti.append(nuovo_p)
        return nuovo_p


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        prestito_trovato = None
        for p in self.__prestiti:
            if p.codice == id_prestito:
                prestito_trovato = p
                break

        if not prestito_trovato:
            raise ValueError("Prestito non trovato con questo ID.")

        if not prestito_trovato.attivo:
            raise ValueError("Questo prestito è già stato terminato.")

        prestito_trovato.attivo = False
        return prestito_trovato