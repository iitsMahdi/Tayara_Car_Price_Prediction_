class Car:
    def __init__(self):
        self.marque = None
        self.modele = None
        self.kilo = None
        self.color = None
        self.boite = None
        self.annee = None
        self.cylindre = None
        self.puissance = None
        self.carburant = None
        self.prix = None

    def update_attributes(self, marque, modele, kilo, color, boite, annee, cylindre, puissance, carburant, prix):
        self.marque = marque
        self.modele = modele
        self.kilo = kilo
        self.color = color
        self.boite = boite
        self.annee = annee
        self.cylindre = cylindre
        self.puissance = puissance
        self.carburant = carburant
        self.prix = prix

    def __repr__(self):
        return f"Car({self.marque}, {self.modele}, {self.kilo}, {self.color}, {self.boite}, {self.annee}, {self.cylindre}, {self.puissance}, {self.carburant}, {self.prix})"