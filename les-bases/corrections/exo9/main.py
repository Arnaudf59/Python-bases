from Class.Immeuble import Immeuble
from Class.Supermarche import Supermarche
from Class.Banque import Banque

# 4 immeubles
immeuble1 = Immeuble("26 rue de la Gravenade", 3, 3)
immeuble2 = Immeuble("28 rue de la Grevande", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble4 = Immeuble("120 rue pleiades", 8, 4)

# 2 supermarché
supermarche1 = Supermarche("27 rue de la Gravenade", 1, 12)
supermarche2 = Supermarche("119 rue pleiades", 4, 25)

# 1 banque
banque = Banque("53 rue elios mitterand", 25, "GravenBanque", 5)

print("La rue comporte 4 immeubles", immeuble1.get_adresse(),",", immeuble2.get_adresse(), ",", immeuble3.get_adresse(), ",", immeuble4.get_adresse())
print("La rue comporte 2 supermarché", supermarche1.get_adresse(), ",", supermarche2.get_adresse())
print("La rue comporte 1 banque", banque.get_adresse())