####################################################
##################  Bibliothèques ##################
####################################################


import tkinter
from tkinter import messagebox


####################################################
###################  Interface 2 ###################
####################################################


def lancer_analyse():
    url_page = entry_url.get()
    mots_cles = entry_mots_cles.get()

    if not url_page or not mots_cles:
        messagebox.showerror("Erreur", "Veuillez entrer l'URL de la page et les mots-clés.")
        return

    print("URL de la page :", url_page)
    print("Mots-clés :", mots_cles)


root = tkinter.Tk()
root.title("Analyse de page")

label_url = tkinter.Label(root, text="Entrez l'URL de la page :")
label_url.pack()

entry_url = tkinter.Entry(root, width=50)
entry_url.pack()

label_mots_cles = tkinter.Label(root, text="Entrez les mots-clés (séparés par des virgules) :")
label_mots_cles.pack()

entry_mots_cles = tkinter.Entry(root, width=50)
entry_mots_cles.pack()

bouton_analyse = tkinter.Button(root, text="Lancer l'analyse", command=lancer_analyse)
bouton_analyse.pack()

root.mainloop()


####################################################
###################  Interface 2 ###################
####################################################


def afficher_details():
    selected_url = liste_urls.get(liste_urls.curselection())

    print("Détails pour l'URL :", selected_url)



def sauvegarder_rapport():
    messagebox.showinfo("Rapport sauvegardé", "Le rapport de référencement a été sauvegardé.")


def mettre_a_jour_mots_cles():
    messagebox.showinfo("Mise à jour des mots-clés", "La liste des mots-clés parasites a été mise à jour.")


def afficher_interface_deux():
    root_deux = tkinter.Tk()
    root_deux.title("Détails des URLs")

    label_select_url = tkinter.Label(root_deux, text="Sélectionnez une URL :")
    label_select_url.pack()

    liste_urls = tkinter.Listbox(root_deux, width=50)
    liste_urls.pack()


    urls = [
        "https://exemple.com/page1",
        "https://exemple.com/page2",
        "https://exemple.com/page3"
    ]

    for url in urls:
        liste_urls.insert(tkinter.END, url)

    bouton_details = tkinter.Button(root_deux, text="Afficher les détails", command=afficher_details)
    bouton_details.pack()

    bouton_sauvegarder = tkinter.Button(root_deux, text="Sauvegarder le rapport", command=sauvegarder_rapport)
    bouton_sauvegarder.pack()

    bouton_maj_mots_cles = tkinter.Button(root_deux, text="Mettre à jour les mots-clés parasites", command=mettre_a_jour_mots_cles)
    bouton_maj_mots_cles.pack()

    root_deux.mainloop()


afficher_interface_deux()