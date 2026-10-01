from noeud import Noeud

n1 = Noeud("y", [])
n2 = Noeud(3, [])


n3 = Noeud("+", [])
n3.ajouter_noeud(n2)
n3.ajouter_noeud(n1)

n4 = Noeud("Exp", [])
n4.ajouter_noeud(n3)

n4.afficher()


mon_dictionnaire = {
    "y": 5.0,
    "x": 2.5,
    "z": 9.0
}

print(n3.evaluer(mon_dictionnaire))