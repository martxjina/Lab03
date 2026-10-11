class Strumento:
    def __init__(self, codice, nome, marca, anno, costo ):
            self.codice = codice
            self.nome = nome
            self.marca = marca
            self.anno = int(anno)
            self.costo = float(costo)

    def __str__(self):
        return f"{self.codice}: {self.nome}, Marca: {self.marca}, Anno: {self.anno}, Valore: {self.costo}"


