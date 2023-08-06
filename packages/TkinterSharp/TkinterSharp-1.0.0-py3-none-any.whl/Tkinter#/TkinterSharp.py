#--------------#  _____  
#              #    |      | /       |        |
#   MAIN FILE  #    |      |-      --|--    --|--
#              #    |      | \       |        |
#--------------#


#-------------------------------------------------------------------------------------------------#
# FR :                                                                                            #
#                                                                                                 #
# /!\ NE PAS MODIFIER LE FICHIER SVP EN CAS DE CORRUPTION /!\                                     #
#                                                                                                 #
# Ce module est une simplification de la librairie TKINTER qui est une librairie pour créer des   #
# applications . (Si la librairie n'est pas installé veuiller l'installer)                        #                                                             
#-------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------#
# EN :                                                                                            #
#                                                                                                 #
#                                                                                                 #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------# 

# IMPORTATION

import window
from window import window
import tkinter
from tkinter import Tk

# CLASS

class tkpp():
    def root(name, size, color="white"):
        window.title(name)
        window.geometry(size)
        window.configure(bg=color)
    def title(variable, text, bgcolor="white", fontfamily="Arial", anchor="center"):
        variable = tkinter.Label(window, text=text)
        variable.configure(variable, bg=bgcolor, font=(fontfamily, 30, "bold"), anchor=anchor)
        variable.pack()
    def subtitle(variable, text, bgcolor="white", fontfamily="Arial", anchor="center"):
        variable = tkinter.Label(window, text=text)
        variable.configure(variable, bg=bgcolor, font=(fontfamily, 23, "bold"), anchor=anchor)
        variable.pack()
    def text(variable, text, bgcolor="white", fontfamily="Arial", anchor="center", size="15"):
        variable = tkinter.Label(window, text=text)
        variable.configure(variable, bg=bgcolor, font=(fontfamily, size),  anchor=anchor)
        variable.pack()
    def button(variable, text, command, bgcolor="whiteold", fontfamily="Arial", anchor="center"):
        variable = tkinter.Button(text=text, command=command, bg=bgcolor)
        variable.pack()
    def loop():
        window.mainloop()



# (C) 2023 - Vimo






