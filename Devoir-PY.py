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


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
test_attribut = 'a'
test_balise = 'p'


test_html = etape6(html_doc, test_balise, test_attribut)


####################################################
#####################  Etape 7 #####################
####################################################


def etape7(html, balise, attribut):
    recup_txt = BeautifulSoup(html, 'lxml')
    balise_print = recup_txt.find_all(balise)
    convert = recup_txt.get_text()
    # attribut_print = balise_print.find_all(attribut)


    print(balise_print)
    print(convert)
    # print(attribut_print)


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<img src="pic_trulli.jpg" alt="Italian Trulli">
<img src="img_girl.jpg" alt="Girl in a jacket">
<img src="img_chania.jpg" alt="Flowers in Chania">
<a href="https://www.w3schools.com">Visit W3Schools</a>
<a href="https://esiee-it.blackboard.com/ultra/courses/_101859_1/outline/edit/document/_1173113_1?courseId=_101859_1&view=content">ESIEE</a>
<a href="https://google.com">Navigateur</a>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

test_balise = 'img'
test_attribut = 'alt'

test_html = etape7(html_doc, test_balise, test_attribut)


####################################################
#####################  Etape 8 #####################
####################################################


def etape8(url):
    nom_domaine = urlparse(url).netloc
    print(nom_domaine)


url_test = 'https://google.com'

test_html = etape8(url_test)


####################################################
#####################  Etape 9 #####################
####################################################


def etape9(nom_domaine, urls):
    urls_du_domaine = []
    urls_hors_domaine = []

    for url in urls:
        if nom_domaine in url:
            urls_du_domaine.append(url)
        else:
            urls_hors_domaine.append(url)

    return urls_du_domaine, urls_hors_domaine



nom_domaine = "example.com"
liste_urls = [
    "http://www.example.com/page1",
    "http://subdomain.example.com/page2",
    "https://anotherdomain.com",
    "http://www.example.org",
    "https://example.com/page3"
]

urls_du_domaine, urls_hors_domaine = trier_urls_par_domaine(nom_domaine, liste_urls)

print("URLs du domaine : ", urls_du_domaine)
print("URLs hors du domaine : ", urls_hors_domaine)


####################################################
#####################  Etape 10 ####################
####################################################

def etape10(url):
    page = requests.get(url)
    html = page.content
    texte_recup = BeautifulSoup(html, 'lxml')
    print(texte_recup)



lien = 'https://mc-projet-bts.alwaysdata.net/vitrine'

test_html2 = etape10(lien)


####################################################
#####################  Etape 11 ####################
####################################################


def etape11(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            keywords_content = keywords.get('content')
            mots_cles = keywords_content.split(',')[:3]
            occurrences = {mot: keywords_content.count(mot) for mot in mots_cles}
        else:
            mots_cles = []
            occurrences = {}

        liens_entrants = len(soup.find_all('a', href=True))

        liens_sortants = len([link for link in soup.find_all('a') if link.get('href').startswith('http')])

        balises_alt = soup.find_all('img', alt=True)
        presence_balises_alt = len(balises_alt) > 0

        print("Mots-clés et leurs 3 premières occurrences :", occurrences)
        print("Nombre de liens entrants :", liens_entrants)
        print("Nombre de liens sortants :", liens_sortants)
        print("Présence de balises alt pour les images :", presence_balises_alt)
    else:
        print("La requête a échoué avec le code :", response.status_code)

url_page = input("Entrez l'URL de la page à analyser : ")

audit_page(url_page)


