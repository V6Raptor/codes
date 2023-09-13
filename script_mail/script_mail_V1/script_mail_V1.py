#####################################################################
######################## script_mail_V1 by V6R #########################
#####################################################################
#######################################
############## IMPORTANT ##############
#######################################
#1 Vous devez absolument créer un mot de passe d'application sur votre compte gmail pour que le script soit fonctionnel
#2 Tuto pour créer un mot de passe d'application : https://www.youtube.com/watch?v=nuD6qNAurVM&t=1s&ab_channel=WebTech
#3 Une fois fait, entrez vos information dans le fichier config.json ==> "email" : "Votre @ email","pwd" : "Votre mot de passe d'application"
#4 Executez le script avec  py .\script_mail_V1.py


####################################################
############## import de bibliothèque ##############
####################################################
import smtplib
import json
from email.message import EmailMessage
from cryptography.fernet import Fernet


#########################################################
############## config gmail (fichier json) ##############
#########################################################
#json_file = open("config.json")
#gmail_cfg = json.load(json_file)

#print ("votre configuration: ", gmail_cfg) # affiche dans la console le fichier config


#####################################################################
############## chiffrement du fichier de configuration ##############
#####################################################################
vachette = Fernet.generate_key() # permet de générer une clé de chiffrement
 
with open('HowtoOpenADoor.key', 'wb') as HowtoOpenADoor: # écriture de la clé de chiffrement sur un fichier nommé "HowtoOpenADoor" (ouverture en mode écriture "wb")
   HowtoOpenADoor.write(vachette)
print("La solution: ", vachette, "\n") # affiche dans la console le contenu du fichier de la clé de chiffrement

  
#1 ouverture de la clé
with open('HowtoOpenADoor.key', 'rb') as HowtoOpenADoor: # lecture du fichier contenant la clé de chiffrement (ouverture en mode lecture "rb")
    solution = HowtoOpenADoor.read()
   
#2 utilisation de la clé
fernet = Fernet(solution) 
    
# ouverture du fichier à chiffrer
with open('config.json', 'rb') as TuVasDisparaitre: # lecture de la variable contenant le fichier config (ouverture en mode lecture "rb")
    non_chiffred = TuVasDisparaitre.read()
print ("Fichier non chiffré: ", non_chiffred, "\n") # affiche dans la console le contenu du fichier non chiffré
    
# chiffrement du fichier
chiffred = fernet.encrypt(non_chiffred) # chiffrement du fichier config

# Ecriture des données chiffrées
with open('config.json', 'wb') as fichier_chiffred: # écriture des données chiffrées sur un fichier nommé "fichier_chiffred" (ouverture en mode écriture "wb")
    fichier_chiffred.write(chiffred)
print("Fichier chiffré: ", chiffred, "\n") # affiche dans la console le contenu du fichier chiffré


#######################################################################
############## déchiffrement du fichier de configuration ##############
#######################################################################
# utilisation de la clé
fernet = Fernet(solution)

with open('config.json', 'rb') as fichier_chiffred2:
    chiffred2 = fichier_chiffred2.read()

# déchiffrement du fichier
dechiffred = fernet.decrypt(chiffred2)

# Ecriture des données déchiffrées
with open('config.json', 'wb') as fichier_dechiffred: # écriture des données déchiffrées sur un fichier nommé "fichier_dechiffred" (ouverture en mode écriture "wb")
    fichier_dechiffred.write(dechiffred)    
print ("Fichier déchiffré: ", dechiffred, "\n") # affiche dans la console le contenu du fichier déchiffré


#########################################################
############## config gmail (fichier json) ##############
#########################################################
json_file = open("config.json")
gmail_cfg = json.load(json_file)

print ("votre configuration: ", gmail_cfg, "\n") # affiche dans la console le fichier config


###############################################
############## message à envoyer ##############
###############################################
#1 message préenregistré
message = EmailMessage() # création d'une variable "message" contenant la fonction "EmailMessage()"
# message ["to"] = gmail_cfg ["email"] # Ligne de test d'envoi
message ["to"]= input("Entrez l'adresse du destinataire: ")
message ["from"] = gmail_cfg ["email"] 
message ["subject"] = "Un potentiel alternant"
message.set_content ("Bonjour,\n\n\n J\'intègre un double cursus en alternance à l\'ESIEE IT, me permettant d\'obtenir un Bachelor en cybersécurité et Licence d\'Informatique générale.\n Dans ce cadre, je vous propose de rejoindre votre équipe pour un contrat d\'un an ou plus en tant qu\'administrateur système et réseau en alternance ou autre en lien avec celui-ci.\n\n Dans le cas où ceci serait possible je reste à votre disposition en vue d'éventuelle demande d'information supplémentaire.\n\n Je vous prie d\'agréer, Madame, Monsieur, l\'expression de mon profond respect.\n\n\n Cordialement,\n\n Limane MANÉ-COLY")


###########################################################################################
############## Création du client smtp + connexion à gmail et envoie du mail ##############
###########################################################################################
with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp :
    smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
    smtp.send_message(message)
    
    print ("Mail envoyé !")