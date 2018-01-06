# -*- coding: cp1252 -*-

def main():             #main funktionen
    namn = dict()       #definerar 2 dicts och 1 lista
    alias = dict()
    lista = []

    while True:
        x = raw_input('phone book>').lower()        #tar användar input
        if ';' in x:
            print'Inga semikolon pls'
        else:
            lista = x.split()
            if 'add' in lista:                  #kollar om ett kommando finns i lista, tillkallar rätt funktion
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
    try:                #kollar om tredje lementet i listan är ett nummer
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
        print namn[lista[1]]        #printar ut värdet som har lista[1] som nyckel
    elif lista[1] in alias:     
        print namn[alias[lista[1]]]     #kollar vilket namn aliaset är kopplat till tar det namnet och skriver ut värdet dvs nummret
    else:
        print 'angivet namn finns inte i telefonboken'

def alias1(lista, namn, alias):     
    if lista[1] in namn:            #om lista[1] finns i namn dict
        alias[lista[2]] = lista[1]      #ge alias dict lista[2] som nyckel och lista[1] som värde
    elif lista[1] in alias:
        alias[lista[2]] = alias[lista[1]] #gör samma sak fast om lista[1] finns i alias, sparar en ny alias
    else:
        print'Personen finns inte i telefonboken'

def change(lista, namn, alias):     #funkar på samma sätt som övriga
    if lista[1] in alias:           
        namn[alias[lista[1]]] = lista[2]
    elif lista[1] in namn:
        namn[lista[1]] = lista[2]
    else:
        print'Personen finns inte i telefonboken'
        
def save(lista, namn, alias):
    f = open(lista[1], 'w')     #skapar en ny fil med list[1] som filnamn, sätter att den ska skrivas till
    for name in namn.keys():    #for loop för att skriva in namn nycklar och värde i filnamn
        f.write(namn[name]+';'+name+';'+'\n')
    for name in alias.keys():   #gör samma sak för alias fast lite annorlunda eftersom alias{alias;namn}
        f.write(namn.get(alias.get(name))+';'+name+';'+'\n')    #skriver in så att alias paras upp med rätt nummer i filnamn
    f.close()       #stänger filen
    alias.clear()   #tömmer alias dict

def load(lista, namn):
    namn.clear()    #tömmer namn dict
    try:            #kollar så att det finns rätt antal inputs i userinput
        open(lista[1])
    except(IndexError):
        print'load tar två inputs (load filnamn)'
        return
    except(NameError, IOError):     #skriver ut ett felmedelande om filnamnet inte finns
        print'Denna fil fins inte'
        return
    with open(lista[1], 'r') as f:
        for item in f.readlines():
            namn[item.split(';')[1]] = item.split(';')[0]   #splittar upp från semikolon i filen och tar ut rätt nyckel och värde sätter in i namn dict

main()
    
