from Class.Player import Player

class Guerrier(Player):
    
    def __init__(self, pseudo, pv, attaque):
        super().__init__(pseudo, pv, attaque)
        self.armure = 3
        print("Bienvenue au guerrier", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
    
    # Une methode get pour récupérer les point d'armure
    def get_armure(self):
        return self.armure
    
    # On modifie la methode dommage pour inséré les point d'armure
    def dommage(self, dommage):
        if self.armure > 0:
          self.armure -= 1
          dommage = 0
          
        super().dommage(dommage)
        
    # On rajoute une methode pour recharger les points d'armure
    def recharge_armure(self):
        self.armure = 3