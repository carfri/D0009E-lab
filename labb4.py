# -*- coding: cp1252 -*-

def main():             #main funktionen
    namn = dict()       #definerar 2 dicts och 1 lista
    alias = dict()
    lista = []

    while True:
        x = raw_input('phone book>').lower()        #tar anv�ndar input
        if ';' in x:
            print'Inga semikolon pls'
        else:
            lista = x.split()
            if 'add' in lista:                  #kollar om ett kommando finns i lista, tillkallar r�tt funktion
                add(lista, namn)
            elif 'lookup' in lista:
                lookup(lista, namn, alias)
            elif 'alias' in lista:
                alias1(lista, namn, alias)
            elif 'change' in lista:
                change(lista, namn, alias)
            elif 'save' in lista:
                save(lista, namn, alias)            
            elif 'load' in lista:
                load(lista, namn)
            elif 'print' in lista:
                print namn
                print alias
            elif 'quit' in lista:
                break

def add(lista, namn):
    try:                #kollar om tredje lementet i listan �r ett nummer
        float(lista[2])
    except (IndexError, ValueError):
        print'add tar tre inputs (add, namn, nummer)'
        return
    if lista[1] in namn:
        print 'Detta namnet finns redan!'
    else:
        namn[lista[1]] = lista[2]
        
def lookup(lista, namn, alias):     #kollar om lista[1] finns i namn dict
    if lista[1] in namn:
        print namn[lista[1]]        #printar ut v�rdet som har lista[1] som nyckel
    elif lista[1] in alias:     
        print namn[alias[lista[1]]]     #kollar vilket namn aliaset �r kopplat till tar det namnet och skriver ut v�rdet dvs nummret
    else:
        print 'angivet namn finns inte i telefonboken'

def alias1(lista, namn, alias):     
    if lista[1] in namn:            #om lista[1] finns i namn dict
        alias[lista[2]] = lista[1]      #ge alias dict lista[2] som nyckel och lista[1] som v�rde
    elif lista[1] in alias:
        alias[lista[2]] = alias[lista[1]] #g�r samma sak fast om lista[1] finns i alias, sparar en ny alias
    else:
        print'Personen finns inte i telefonboken'

def change(lista, namn, alias):     #funkar p� samma s�tt som �vriga
    if lista[1] in alias:           
        namn[alias[lista[1]]] = lista[2]
    elif lista[1] in namn:
        namn[lista[1]] = lista[2]
    else:
        print'Personen finns inte i telefonboken'
        
def save(lista, namn, alias):
    f = open(lista[1], 'w')     #skapar en ny fil med list[1] som filnamn, s�tter att den ska skrivas till
    for name in namn.keys():    #for loop f�r att skriva in namn nycklar och v�rde i filnamn
        f.write(namn[name]+';'+name+';'+'\n')
    for name in alias.keys():   #g�r samma sak f�r alias fast lite annorlunda eftersom alias{alias;namn}
        f.write(namn.get(alias.get(name))+';'+name+';'+'\n')    #skriver in s� att alias paras upp med r�tt nummer i filnamn
    f.close()       #st�nger filen
    alias.clear()   #t�mmer alias dict

def load(lista, namn):
    namn.clear()    #t�mmer namn dict
    try:            #kollar s� att det finns r�tt antal inputs i userinput
        open(lista[1])
    except(IndexError):
        print'load tar tv� inputs (load filnamn)'
        return
    except(NameError, IOError):     #skriver ut ett felmedelande om filnamnet inte finns
        print'Denna fil fins inte'
        return
    with open(lista[1], 'r') as f:
        for item in f.readlines():
            namn[item.split(';')[1]] = item.split(';')[0]   #splittar upp fr�n semikolon i filen och tar ut r�tt nyckel och v�rde s�tter in i namn dict

main()
    
