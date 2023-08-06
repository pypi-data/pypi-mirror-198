from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.0"
DESCRIPTION = "A library to simplify Tkinter"
LONG_DESCRIPTION = "[FR] \
    TkinterSharp / TKinter# (TK#) est une librairie dont le but est de simplifier la librairie Tkinter \qui permet de créer des interfaces graphiques \
    , d'un coté elle permet d'éviter d'écrire trop de code en compressent juste simplement le code et \
    d'un autre coté elle rajoute des definition avec des paramètres déjà préparer comme la defenition : \
    title qui permet de générer un texte avec comme paramètre : 30 de taille et en gras ."

setup(
    name="TkinterSharp",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    author="Rayanis55",
    url='https://github.com/Rayanis55/Tkinterpp',
    packages=find_packages(),
    keywords=['python', 'tkinter', 'addon'],
    install_requires=['tkinter'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)