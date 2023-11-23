####################################################
##################  Bibliothèques ##################
####################################################

from collections import Counter
import csv


####################################################
#####################  Etape 1 #####################
####################################################

def etape1 (texte) :
    liste = texte.split(" ")
    occurence = Counter(liste)
    
    liste_final = dict(sorted(occurence.items(), key=lambda item: item[1], reverse=True))
    
    
    return (liste_final)
    
texte_test = ("bonjour ceci est mon texte de test ce texte est un test de texte")

nbr_mots = etape1 (texte_test)

print ("Liste de mots avec occurence", nbr_mots)


####################################################
#####################  Etape 2 #####################
####################################################

def etape2(donnees, mots_parasites):
    structure_filtree = {mot: occurrence for mot, occurrence in donnees.items() if mot not in mots_parasites}
    return structure_filtree

mots_parasites = ["le", "la", "les","un", "une","ce", "de", "des"]

donnees_etape1 = nbr_mots

donnees_filtre = etape2(donnees_etape1, mots_parasites)
print("Sans les parasites", donnees_filtre)


####################################################
#####################  Etape 3 #####################
####################################################

def recuperer_mots_parasites(nom_fichier):
    try:
        with open(nom_fichier, newline='', encoding='utf-8') as fichier_csv:
            f = open("fichier_csv", "a")
            f.write(mots_parasites)
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                mot = ligne.get('Mot')  # Modifier ici selon le nom de la colonne dans votre fichier CSV
            f.close()
    
    except FileNotFoundError:
        print("Fichier introuvable.")
    
    return mots_parasites

#f = open("parasite.csv", "x")

fichier_csv = 'parasite.csv'  # Remplacez ceci par le chemin vers votre fichier CSV
liste_mots_parasites = recuperer_mots_parasites(fichier_csv)

print(liste_mots_parasites)