# Class qui est en relation avec le cours Objet
class Player:
    
    def __init__(self, pseudo, pv, attaque):
        self.pseudo = pseudo
        self.pv = pv
        self.attaque = attaque
        print("Bienvenue au joueur", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_pv(self):
        return self.pv
    
    def get_attaque(self):
        return self.attaque
    
    def dommage(self, dommage):
        self.pv -= dommage
        print("Aie... vous venez de subir", dommage, "dégats !")
        
    def attaque_player(self, target_player):
        target_player.dommage(self.attaque)