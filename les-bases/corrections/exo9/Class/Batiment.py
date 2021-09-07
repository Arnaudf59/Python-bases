class Batiment:
    
    def __init__(self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages
        
    def get_adresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages