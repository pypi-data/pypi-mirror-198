import TkinterSharp
from TkinterSharp import tkpp
import tkinter
from tkinter import Tk

# With Tkinter++

def commandButton():
    tkpp.text(variable="buttonet", text="Here is a text", bgcolor="red", anchor="sw")

tkpp.root(name="TK#", size="800x500", color="red")
tkpp.title(variable="l1w", text="Welcome", bgcolor="red")
tkpp.title(variable="lw2", text="to example", bgcolor="red")
tkpp.subtitle(variable="lws1", text="Button", bgcolor="red")
tkpp.button(variable="buttone", text="Click my", command=commandButton ,bgcolor="red")
tkpp.loop()



