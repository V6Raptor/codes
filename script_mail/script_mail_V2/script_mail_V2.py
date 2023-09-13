#####################################################################
######################## script_mail_V1 by V6R ######################
#####################################################################
#######################################
############## IMPORTANT ##############
#######################################
#1 Vous devez absolument créer un mot de passe d'application sur votre compte gmail pour que le script soit fonctionnel
#2 Tuto pour créer un mot de passe d'application : https://www.youtube.com/watch?v=nuD6qNAurVM&t=1s&ab_channel=WebTech
#3 Une fois fait, entrez vos information dans le fichier config.json ==> "email" : "Votre @ email","pwd" : "Votre mot de passe d'application"
#4 Executez le script avec  py .\script_mail_V2.py


####################################################
############## import de bibliothèque ##############
####################################################
import smtplib
import json
from email.message import EmailMessage
from cryptography.fernet import Fernet


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


message = EmailMessage() # création d'une variable "message" contenant la fonction "EmailMessage()"


# message ["to"] = gmail_cfg ["email"] # Ligne de test d'envoi
message ["to"]= input("Entrez l'adresse du destinataire: ")
print ("Le destinataire est : ", message ["to"], "?") 

réponse = input("Répondre oui ou non: ")

if réponse == "oui": # Objet
    print ("Destinataire validé(e) !")
    message ["from"] = gmail_cfg ["email"]
    message ["subject"] = input("Entrez l'objet: ")
    print ("L'objet est: ", message ["subject"], "?")
    réponse = input("Répondre oui ou non: ")
        
    if réponse == "oui": # message personnalisé
        print ("Objet validé !")
        msg = input ("Entrez votre message: ")
        print ("Votre message est: ", msg, "?")
        réponse = input("Répondre oui ou non: ")
        
        if réponse == "oui": # envoi message
            print("Message validé !")
        
        elif réponse == "non":
            msg = input ("Veuillez retapez votre message: ")
            print ("Votre message est: ", msg, "?")
            réponse = input("Répondre oui ou non: ")
            
            while réponse != "oui":
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # envoi message
                print("Message validé !")
        
        else:
            msg = input ("Veuillez retapez votre message: ")
            print ("Votre message est: ", msg, "?")
            réponse = input("Répondre oui ou non: ")
            
            while réponse != "oui":
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # envoi message
                print("Message validé !")


    elif réponse == "non":
        message ["subject"] = input("Veuillez retapez l'objet: ")
        print ("L'objet est: ", message ["subject"], "?")
        réponse = input("Répondre oui ou non: ")
            
        while réponse != "oui":
            message ["subject"] = input("Veuillez retapez l'objet: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
            
        if réponse == "oui": # message personnalisé
            print ("Objet validé !")
            msg = input ("Entrez votre message: ")
            print ("Votre message est: ", msg, "?")
            réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # envoi message
                print("Message validé !")
            
            elif réponse == "non":
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
            
            else:
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
        
        
        else:
            message ["subject"] = input("Veuillez retapez l'objet: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
           
            while réponse != "oui":
                message ["subject"] = input("Veuillez retapez l'objet: ")
                print ("L'objet est: ", message ["subject"], "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # message personnalisé
                msg = input ("Entrez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
                
                elif réponse == "non":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
                else:
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")


elif réponse == "non":
    message = input("Veuillez retapez l'adresse du destinataire: ")
    print ("Le destinataire est : ", message, "?")
    réponse = input("Répondre oui ou non: ")
    
    while réponse != "oui":
        message ["to"] = input("Veuillez retapez l'adresse du destinataire: ")
        print ("Le destinataire est : ", message, "?")
        réponse = input("Répondre oui ou non: ")
    
    if réponse == "oui": # Objet
        print ("Destinataire validé(e) !")
        message ["from"] = gmail_cfg ["email"]
        message ["subject"] = input("Entrez l'objet: ")
        print ("L'objet est: ", message ["subject"], "?")
        réponse = input("Répondre oui ou non: ")
        
        if réponse == "oui": # message personnalisé
            print ("Objet validé !")
            msg = input ("Entrez votre message: ")
            print ("Votre message est: ", msg, "?")
            réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # envoi message
                print("Message validé !")
            
            elif réponse == "non":
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
            
            else:
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
        
        elif réponse == "non": # Objet
            message ["subject"] = input("Veuillez retapez l'objet: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
            
            while réponse != "oui": # Objet
                message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
                print ("L'objet est: ", message ["subject"], "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # message personnalisé
                print ("Objet validé !")
                msg = input ("Entrez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
                
                elif réponse == "non":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
                else:
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
        else: # Objet
            message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
           
            while réponse != "oui": # Objet
                message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
                print ("L'objet est: ", message ["subject"], "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # message personnalisé
                print ("Objet validé !")
                msg = input ("Entrez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
                
                elif réponse == "non":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
                else:
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")


else:
    message = input("Veuillez retapez l'adresse du destinataire: ")
    print ("Le destinataire est : ", message, "?")
    réponse = input("Répondre oui ou non: ")
    
    while réponse != "oui":
        message ["to"] = input("Veuillez retapez l'adresse du destinataire: ")
        print ("Le destinataire est : ", message, "?")
        réponse = input("Répondre oui ou non: ")
    
    if réponse == "oui": # Objet
        print ("Destinataire validé(e) !")
        message ["from"] = gmail_cfg ["email"]
        message ["subject"] = input("Entrez l'objet: ")
        print ("L'objet est: ", message ["subject"], "?")
        réponse = input("Répondre oui ou non: ")
        
        if réponse == "oui": # message personnalisé
            print ("Objet validé !")
            msg = input ("Entrez votre message: ")
            print ("Votre message est: ", msg, "?")
            réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # envoi message
                print("Message validé !")
            
            elif réponse == "non":
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
            
            else:
                msg = input ("Veuillez retapez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                while réponse != "oui":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
        
        elif réponse == "non":
            message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
            
            while réponse != "oui":
                message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
                print ("L'objet est: ", message ["subject"], "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # message personnalisé
                print ("Objet validé !")
                msg = input ("Entrez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
                
                elif réponse == "non":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
                else:
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
        
        else:
            message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
            print ("L'objet est: ", message ["subject"], "?")
            réponse = input("Répondre oui ou non: ")
           
            while réponse != "oui":
                message ["subject"] = input("Veuillez retapez l'adresse du destinataire: ")
                print ("L'objet est: ", message ["subject"], "?")
                réponse = input("Répondre oui ou non: ")
            
            if réponse == "oui": # message personnalisé
                print ("Objet validé !")
                msg = input ("Entrez votre message: ")
                print ("Votre message est: ", msg, "?")
                réponse = input("Répondre oui ou non: ")
                
                if réponse == "oui": # envoi message
                    print("Message validé !")
                
                elif réponse == "non":
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                
                else:
                    msg = input ("Veuillez retapez votre message: ")
                    print ("Votre message est: ", msg, "?")
                    réponse = input("Répondre oui ou non: ")
                    
                    while réponse != "oui":
                        msg = input ("Veuillez retapez votre message: ")
                        print ("Votre message est: ", msg, "?")
                        réponse = input("Répondre oui ou non: ")
                    
                    if réponse == "oui": # envoi message
                        print("Message validé !")
                

# msg = "Entrez votre message" # Pour message préenregistré ajouté
message.set_content (msg)


###########################################################################################
############## Création du client smtp + connexion à gmail et envoie du mail ##############
###########################################################################################
with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp :
    smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
    smtp.send_message(message)
    
    print ("Mail envoyé !")
