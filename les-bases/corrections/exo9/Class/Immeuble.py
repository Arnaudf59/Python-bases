from Class.Batiment import Batiment

class Immeuble(Batiment):
    
    def __init__(self, adresse, nb_etages, nb_balcons):
        super().__init__(adresse, nb_etages)
        self.nb_balcons = nb_balcons
        
    def get_adresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages
    
    def get_nb_balcons(self):
        return self.nb_balcons
