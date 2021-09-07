from Class.Batiment import Batiment

class Supermarche(Batiment):
    
    def __init__(self, adresse, nb_etages, nb_rayons):
        super().__init__(adresse, nb_etages)
        self.nb_rayons = nb_rayons
        
    def get_adresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages
    
    def get_nb_rayons(self):
        return self.nb_rayons