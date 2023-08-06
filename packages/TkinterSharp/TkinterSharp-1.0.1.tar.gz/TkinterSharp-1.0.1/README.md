# Tkinterpp

## [FR] DESCRIPTION

TkinterPP / TKinter++ (TK++) est une librairie dont le but est de simplifier la librairie Tkinter qui permet de créer des interfaces graphiques, d'un coté elle
permet d'éviter d'écrire trop de code en compressent juste simplement le code et d'un autre coté elle rajoute des definition avec des paramètres déjà
préparer comme la defenition : title qui permet de générer un texte avec comme paramètre : 30 de taille et en gras .

Example de simplification : 

Sans TK++ :

root = tkinter.Tk()
root.title("TK++")
root.geometrie("800x500")
root.mainLoop()

Avec TK++ : 

tkpp.root(name="TK++", size="800x500")
tkpp.loop()