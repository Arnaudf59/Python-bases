# La class Player correspond au cours Objet
from Class.Players import Player  
    
player1 = Player("Arnaud", 20, 3)
player2 = Player("Maud", 20, 1)

print(player1.get_pseudo(), "attaque", player2.get_pseudo())
player1.attaque_player(player2)
print("Bienvenue au joueur", player1.get_pseudo(), "/ Point de vie :", player1.get_pv(), "/ Attaque : ", player1.get_attaque())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Point de vie :", player2.get_pv(), "/ Attaque : ", player2.get_attaque())