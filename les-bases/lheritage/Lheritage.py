from Class.Player import Player
from Class.Guerrier import Guerrier

player = Player("Arnaud", 20, 5)
warrior = Guerrier("DarkWarrior", 30, 2)
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())

if issubclass(Guerrier, Player):
    print("La class guerrier est bien une spécialisation de la class Player")