class Prestito:
    def __init__(self, codice, strumento, cognome_allievo, data):
        self.codice = codice
        self.strumento = strumento
        self.cognome_allievo = cognome_allievo
        self.data = data
        self.attivo = True

    def __str__(self):
        stato = "In corso" if self.attivo else "Terminato"
        return f"Prestito {self.codice} - Allievo {self.cognome_allievo}, Strumento: {self.strumento.nome} ({self.strumento.codice}), Data: {self.data}, Stato: {stato}"