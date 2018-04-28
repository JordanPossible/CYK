#!/usr/bin/python
# -*- coding:Utf-8 -*-

# On a besoin de listes et de tuples
# Module disponible en Python version >= 3.5
from typing import List, Tuple

# Pour print des belles tables
from prettytable import PrettyTable
# Type pour une variable, juste une chaine, e.g. 'X' ou 'S'
Var = str
# Type pour un alphabet
Alphabet = List[Var]
# Type pour une règle : un symbole transformé en une liste de symboles
Regle = Tuple[Var, List[Var]]

class Grammaire(object):
    """ Type pour les grammaires algébriques (en forme de Chomsky). """
    def __init__(self, sigma: Alphabet, v: Alphabet, s: Var, r: List[Regle], nom="G"):
        """ Grammaire en forme de Chomsky :
            - sigma : alphabet de production, type Alphabet,
            - v : alphabet de travail, type Alphabet,
            - s : symbol initial, type Var,
            - r : liste de règles, type List[Regle].
        """
        # On se contente de stocker les champs :
        self.sigma = sigma
        self.v = v
        self.s = s
        self.r = r
        self.nom = nom

    def __str__(self) -> str:
        """ Permet d'afficher une grammaire."""
        str_regles = ', '.join(
            "{} -> {}".format(regle[0], ''.join(regle[1]) if regle[1] else 'ε')
            for regle in self.r
        )
        return r.format(self.nom, set(self.sigma), set(self.v), self.s, str_regles)

# Grammaire capable de produire les phrases suivantes :
# Le bien qu’il fait, il le fait bien.
# ! Le fait est que j’ai peu de biens.
# ! J’ai bien du mal à faire ce que les autres font bien.
# ! Bien des gens ont fait un peu de bien.
# ! Bien qu’il ait fait du bien, il ne l’ a pas bien fait.
g0 = Grammaire(
    # Alphabet de production, des mots francais (avec une espace pour que la phrase soit lisible et un underscore a la place de l'apostrophe
    ['le ', 'bien ', 'qu ', 'il ', 'fait ', 'est ', 'j ', 'ai ', 'peu ', 'de ', 'biens ', 'du ', 'mal ', 'a_ ', 'faire ', 'ce ', 'que ', 'les ', 'autres ', 'font ', 'des ', 'gens ', 'ont ', 'un ', 'ait ', 'ne ', 'l ', 'a ', 'pas ', '_virgule_ ', '_point_ '],
    # Alphabet de travail, des catégories de mots :
    ['S', 'PROP ', 'PONCT_FIN ', 'GN ', 'PRO_REL ', 'PRO_SUJ ', 'PRO_OBJ ', 'NAM ', 'DET_ART ', 'NOM ', 'GV ', 'VER_PRES ', 'VER_PP ', 'ADJ ', 'VER_SUB ', 'ADV ', 'PONCT_SEG ', 'PRO_PER ', 'ADVP ', 'NOYAUX ', 'SUB ', 'PREP ', 'COMP '],
    ###################################
    'S',
    [
        ( 'S',      ['PROP ', 'PONCT_FIN '] ),

        ( 'PROP ',    ['PROP ', 'PONCT_SEG '] ),
        ( 'PROP ',    ['PROP ', 'PROP ']),
        ( 'PROP ',    ['GN ', 'VER_PRES '] ),
        ( 'PROP ',    ['GN ', 'GV '] ),
        ( 'PROP ',    ['PRO_SUJ ', 'GV '] ),
        ( 'PROP ',    ['PRO_SUJ ', 'GV '] ),
        ( 'COMP ',    ['PREP ', 'NOM '] ),
        
        ( 'NOYAUX ',    ['ADV ', 'PREP '] ),
        
        ( 'GV ',    ['VER_PRES ', 'GN '] ),
        ( 'GV ',    ['GV ', 'GV '] ),
        ( 'GV ',    ['VER_PRES ', 'VER_PP '] ),
        ( 'GV ',    ['GV ', 'GN '] ),
        ( 'GV ',    ['VER_SUB ', 'VER_PP '] ),
        ( 'GV ',    ['GV ', 'COMP '] ),
        ( 'GV ',    ['VER_PRES ', 'ADV '] ),
        ( 'GV ',    ['VER_PRES ', 'SUB '] ),
        ( 'GV ',    ['PRO_PER ', 'GV '] ),
        ( 'GV ',    ['ADV ', 'GV '] ),
        ( 'GV ',    ['GV ', 'VER_PP '] ),
        ( 'GV ',    ['VER_PRES ', 'ADV '] ),
        
        ( 'PRO_REL ',    ['PRO_REL ', 'PRO_REL '] ),

        ( 'GN ',    ['GN ', 'PREP '] ),
        ( 'GN ',    ['PRO_SUJ ', 'PRO_OBJ '] ),
        ( 'GN ',    ['NOYAUX ', 'NOM '] ),
        ( 'GN ',    ['GN ', 'GN '] ),
        ( 'GN ',    ['DET_ART ', 'NOM '] ),
        ( 'GN ',    ['PRO_REL ', 'PRO_SUJ '] ),
        ( 'GN ',    ['PRO_REL ', 'GN '] ), 
        ( 'GN ',    ['ADV ', 'GN '] ),
        ( 'GN ',    ['DET_ART ', 'GN '] ),
        ( 'GN ',    ['NOYAUX ', 'NOM '] ),
        ( 'GN ',    ['DET_ART ', 'NOM '] ),
        ( 'GN ',    ['ADV ', 'GN '] ),
        ( 'GN ',    ['SUB ', 'PRO_PER '] ),

        ( 'ADV ',    ['ADV ', 'ADV '] ),
          
        ( 'DET_ART ', ['le '] ),
        ( 'DET_ART ', ['l '] ),
        ( 'DET_ART ', ['les '] ),
        ( 'DET_ART ', ['un '] ),

        ( 'ADV ', ['bien '] ),
	    ( 'ADV ', ['peu '] ), 
        ( 'ADV ', ['ne '] ),
        ( 'ADV ', ['pas '] ),

        ( 'ADJ ', ['bien '] ),

        ( 'NOM ', ['biens '] ),
        ( 'NOM ', ['bien '] ),
	    ( 'NOM ', ['fait '] ),
        ( 'NOM ', ['mal '] ),
        ( 'NOM ', ['autres '] ),
        ( 'NOM ', ['gens '] ),
        ( 'NOM ', ['pas '] ),

        ( 'VER_PRES ', ['fait '] ),
        ( 'VER_PRES ', ['est '] ),
	    ( 'VER_PRES ', ['ai '] ),
        ( 'VER_PRES ', ['font '] ),
        ( 'VER_PRES ', ['faire '] ),
        ( 'VER_PRES ', ['ont '] ),
        ( 'VER_PRES ', ['a '] ),

        ( 'VER_PP ', ['fait '] ),

        ( 'VER_SUB ', ['ait '] ),

        ( 'PONCT_SEG ', ['_virgule_ '] ),

        ( 'PRO_REL ', ['qu '] ),
        ( 'PRO_REL ', ['ce '] ),
        ( 'PRO_REL ', ['que '] ),

        ( 'PRO_PER ', ['l '] ),

        ( 'PRO_SUJ ', ['il '] ),
        ( 'PRO_SUJ ', ['j '] ), 

        ( 'PRO_OBJ ', ['le '] ),

	    ( 'SUB ', ['que '] ),
        ( 'SUB ', ['qu '] ),

	    ( 'PREP ', ['de '] ),
        ( 'PREP ', ['du '] ),
        ( 'PREP ', ['a_ '] ),
        ( 'PREP ', ['des '] ),

        ( 'PONCT_FIN ', ['_point_ '] ),
    ],
    nom="PH1"
)


#Algo estBienForme
def estBienFormee(self: Grammaire) -> bool:
    """ Vérifie que G est bien formée. """
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    tests = [
        s in v,  # s est bien une variable de travail
        sigma.isdisjoint(v),  # Lettres et variables de travail sont disjointes
        all(
            regle[0] in v  # Les membres gauches de règles sont des variables
            and  # Les membres droits de règles sont des variables ou des lettres
            all(r in sigma | v for r in regle[1])
            for regle in regles
        )
    ]
    return all(tests)
# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.estBienFormee = estBienFormee

#Algo estChomsky
def estChomsky(self: Grammaire) -> bool:
    """ Vérifie que G est sous forme normale de Chomksy. """
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    estBienChomsky = all(
        (   # S -> epsilon
            regle[0] == s and not regle[1]
        ) or (  # A -> a
            len(regle[1]) == 1
            and regle[1][0] in sigma  # a in Sigma
        ) or (  # A -> B C
            len(regle[1]) == 2
            and regle[1][0] in v  # B in V, not Sigma
            and regle[1][1] in v  # C in V, not Sigma
        )
        for regle in regles
    )
    return estBienChomsky and estBienFormee(self)
# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.estChomsky = estChomsky

#Algo CKY
def cocke_kasami_younger(self, w):
    """ Vérifie si le mot w est dans L(G). """
    assert estChomsky(self), "Erreur : {} n'est pas en forme de Chomsky, l'algorithme de Cocke-Kasami-Younger ne fonctionnera pas.".format(self.nom)
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    n = len(w)
    E = dict()  # De taille n^2
    # Cas special pour tester si le mot vide est dans L(G)
    if n == 0:
        return (s, []) in regles, E
    # Boucle en O(n^2)
    for i in range(n):
        for j in range(n):
            E[(i, j)] = set()
    # Boucle en O(n x |G|)
    for i in range(n):
        for regle in regles:
            # Si regle est de la forme : A -> a
            if len(regle[1]) == 1:
                A = regle[0]
                a = regle[1][0]
                if w[i] == a:  # Notez que c'est le seul moment ou utilise le mot w !
                    E[(i, i)] = E[(i, i)] | {A}
    # Boucle en O(n^3 x |G|)
    for d in range(1, n):          # Longueur du morceau
        for i in range(n - d):     # Début du morceau
            j = i + d              # Fin du morceau, on regarde w[i]..w[j]
            for k in range(i, j):  # Parcourt du morceau, ..w[k].., sans la fin
                for regle in regles:
                    # Si regle est de la forme A -> B Cde donner les notes
                    if len(regle[1]) == 2:
                        A = regle[0]
                        B, C = regle[1]
                        if B in E[(i, k)] and C in E[(k + 1, j)]:
                            E[(i, j)] = E[(i, j)] | {A}
    # On a finit, il suffit maintenant d'utiliser la table créée par programmation dynamique
    return s in E[(0, n - 1)], E
# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.genere = cocke_kasami_younger

def transformW(w):
    result = []
    for word in w:
        if(word in result):
            while(word in result):
                word = " " + word
            result.append(word)
        else:
            result.append(word)
    return result

# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.genere = transformW

def prettyPrintUnderMatShape(E, w):
    filePath = "./results/"
    for k in E.copy():
        if k in E and not E[k]:  # On retire les clés qui ont un E[(i, j)] vide
            del(E[k])

    results = PrettyTable(transformW(w))
    matRange = len(w)
    row = []
    for t in range(0, matRange):
        for i in range(0, matRange):
            # print(E1.get((i, i+t)), end='   ')
            if(E1.get((i, i+t))):
                row.append(E1.get((i, i+t)))
            else:
                row.append("")
        results.add_row(row)
        row.clear()
    # print(results)
    outfile = filePath +  "res.txt"
    file=open(outfile, "w+") 
    file.write(''.join(str(results)))
    file.close()
# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.genere = prettyPrintUnderMatShape


def testeMot(g, w):
    """ Joli affichage pour un test """
    print("# Test si w in L(G) :")
    print("  Pour", g.nom, "et w =", w)
    estDansLG, E = cocke_kasami_younger(g, w)
    if estDansLG:
        print("  ==> Ce mot est bien engendré par G !")
    else:
        print("  ==> Ce mot n'est pas engendré par G !")
    return estDansLG, E

