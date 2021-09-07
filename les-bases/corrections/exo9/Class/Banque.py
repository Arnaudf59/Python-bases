from Class.Batiment import Batiment

class Banque(Batiment):
    
    def __init__(self, adresse, nb_etages, nom, nb_coffre):
        super().__init__(adresse, nb_etages)
        self.nom = nom
        self.nb_coffre = nb_coffre
        
    def get_adresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages
    
    def get_nom(self):
        return self.nom
    
    def get_nb_coffre(self):
        return self.nb_coffre