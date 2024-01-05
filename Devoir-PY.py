####################################################
##################  BibliothÃ¨ques ##################
####################################################

from collections import Counter
import pandas
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

####################################################
#####################  Etape 1 #####################
####################################################

def etape1(texte):
    liste = texte.split(" ")
    occurence = Counter(liste)

    liste_final = dict(sorted(occurence.items(), key=lambda item: item[1], reverse=True))

    return (liste_final)


texte_test = ("bonjour ceci est mon texte de test ce texte est un test de texte")

nbr_mots = etape1(texte_test)

print("Liste de mots avec occurence", nbr_mots)


####################################################
#####################  Etape 2 #####################
####################################################

def etape2(donnees, mots_parasites):
    structure_filtree = {mot: occurrence for mot, occurrence in donnees.items() if mot not in mots_parasites}
    return structure_filtree


mots_parasites = ["le", "la", "les", "un", "une", "ce", "de", "des"]

donnees_etape1 = nbr_mots

donnees_filtre = etape2(donnees_etape1, mots_parasites)
print("Sans les parasites", donnees_filtre)


####################################################
#####################  Etape 3 #####################
####################################################

def etape3(nom_fichier):
    try:
        parasites = pandas.read_csv("parasite.csv")
    except:
        print("Fichier introuvable.")

    return parasites



fichier_csv = 'parasite.csv'  # Remplacez ceci par le chemin vers votre fichier CSV
liste_mots_parasites = etape3(fichier_csv)

print(liste_mots_parasites)


####################################################
#####################  Etape 5 #####################
####################################################


def etape5(html):
    recup = BeautifulSoup(html, 'lxml')
    sans_balise =recup.get_text()

    print(sans_balise)



avec_balise = '<p>Ceci est un paragraphe </p>'

test_html1 = etape5(avec_balise)


####################################################
#####################  Etape 6 #####################
####################################################


def etape6(html, balise, attribut):
    recup_txt = BeautifulSoup(html, 'lxml')
    recup_balise = balise
    recup_attribut = attribut
    balise_print = recup_txt.find_all(recup_balise)
    attribut_print = recup_txt.find_all(attribut)


    print(balise_print)
    print(attribut_print)
... (95 lignes restantes)
