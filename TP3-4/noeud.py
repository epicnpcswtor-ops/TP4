import numpy
import matplotlib
import matplotlib.pyplot as plt

# Modifié par Isaac 

class Noeud :

    def __init__ (self, val, list_enfants) :
        self.val = val
        self.list_enfants = list_enfants

    def ajouter_noeud (self,noeud): 
        if isinstance(noeud, Noeud) :
            self.list_enfants.append(noeud)

    def afficher (self): 
        print(self.val)
        for k in self.list_enfants :
            k.afficher()

    def evaluer(self, dico) :
        if isinstance(self.val, (int, float)) :
            return (self.val)

        elif isinstance(self.val, str) and self.val not in ["+", "-", "*"]:
            if self.val in dico:
                return float(dico[self.val])
            else:
                raise ValueError("Pas dans le dictionnaire")

        else : 

            terme_1 = self.list_enfants[0].evaluer(dico)
            terme_2 = self.list_enfants[1].evaluer(dico)

            if self.val == "+" :
                return terme_1 + terme_2

            if self.val == "-" :
                return terme_1 - terme_2

            if self.val == "*" :
                return terme_1 * terme_2


    def tracer(self, var, liste_val):
        resultats = []

        for val in liste_val :
            dico = {var : val}
            res = self.evaluer(dico)

            resultats.append(res)

        plt.figure("Tracé de var")       
        plt.plot(liste_val, resultats)
        plt.xlabel(var)
        plt.ylabel("resultats")
        plt.show()
                        

        
