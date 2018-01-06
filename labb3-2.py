# -*- coding: cp1252 -*-
def meny():                             #meny funktion
    print('Ordlista meny')
    print
    print('1: L�gg in ord')
    print('2: S�k ord')
    print('3: Avsluta program')

def dic1():                             #uppgift 1 funktion
    
    word = []                           #ordlistan
    beskrivning = []                    #beskrivningslistan
    
    while True:                         
        meny()                          #kallar meny funktionen
        val = raw_input('v�lj alternativ: ')        #ger 'val' det v�rde som matas in

        if val == '1':                                #om man matar in 1 s� k�rs den
            x = raw_input('Skriv in ordet du vill l�gga till: ')        #x f�r v�rdet som = det ord som anvndaren matar in

            if x in word:                                               #om 'x' redan finns i 'word' listan s� k�rs denna
                print('Detta ordet finns redan, ta ett annat! ')

            else:                                                       #annars k�rs denna
                y = raw_input('Beskriv ordet: ')                        #y f�r v�rdet av ordets beskrivelse
                word.append(x)                                          #skriver in ordet 'x' i 'word' listan
                beskrivning.append(y)                                   #skriver in beskrivning 'y' i 'beskrivning' listan
                print('Ord sparat!')

        elif val == '2':                                                  #k�rs om 2 matas in 
            z = raw_input('Ordet du s�ker: ')                           #z f�r v�rdet av ordet som s�ks
            if z in word:                                               #om z finns i 'word' listan skrivs f�ljande ut
                print 'Ditt ord', z, 'har f�ljande beskrivning: ', beskrivning[word.index(z)]       #beskrivning[word.index(z)] skriver ut den beskrivning som har samma plats som ordet z i respektive listor

            else:
                print('Detta ord finns inte i ordlistan! ')

        elif val == '3':                          #om 3 matades in avslutas programmet
            print('Ordlistan St�ngs...')
            break
        else:
            print('skriv in ett tal mellan 1-3.')
            
        
#############################################################################################


def dic2():

    tupp_list = []      #listan som ska bli tuppar
    final_list = []     #listan som inneh�ller alla tuppar

    while True:
        meny()          #kallar meny funktionen
        print
        val = raw_input('V�lj alternativ: ')        #ger 'val' det v�rde som matas in

        if val == '1':
            x = raw_input('Skriv in ordet du vill l�gga till: ')        #x f�r samma v�rde som matas in
            for z, y in final_list:                                     #en for loop som letar igenom listan efter x ??
                if z == x:                                              #om ordet redan finns uppmanas anv�ndaren att skriva in ett nytt ord
                    print 'Detta ordet finns redan! V�lj ett annat. \n '
                    break
            

            else:                                                       #om ordet inte finns s� uppmanas anv�ndaren att skriva in en beskrivning
                y = raw_input('Beskriv ordet: ')
                print('ord sparat!\n')
                tupp_list.append(x)                                     #skriver in ord och beskrivning i tupp listan
                tupp_list.append(y)
                tupp = tuple(tupp_list)                                 #omvandlar tupp_list till en tupp
                final_list.append(tupp)                                 #s�tter in tuppen som just skapas i sista listan, den ultimata listan
                del tupp_list[:];                                       #tar bort det som finns i tupp_list f�r att g�ra plats f�r ett nytt ord och en ny beskrivning

        elif val == '2':
            hittad = False
            z = raw_input('Ordet du s�ker: ')                           #ger z v�rdet av det som skrevs in
            for x, y in final_list:                                     #en for loop som letar efter samma v�rde i final_list
                if x == z:
                    print 'Ditt ord ', x, 'har f�ljande beskrivning:', y           #om det hittas i listan s� skrivs detta ut
                    hittad = True
                    break
            if hittad == False:
                print('Hoppsan, detta ordet finns inte i listan, f�rs�k med ett annat!')

                    
        elif val == '3':                            #st�nger ordlistan
            print('St�nger ordlistan...')
            break
        else:                                   #skrivs ut om man inte skriver in n�got mella 1-3
            print('V�nligen mata in ett v�rde mellan 1-3')


##############################################################################################


def dic3():

    ordlista = dict()           #g�r om ordlista till ett dict

    while True:
        meny()
        print
        val = raw_input('V�lj alternativ: ')

        if val == '1':
            x = raw_input('Skriv in ordet du vill l�gga till: ')

            if x in ordlista:
                print('Detta ordet finns redan, ta ett annat!')

            else:
                y = raw_input('Beskriv ordet: ')
                ordlista[x] = y             #s�tter in x som nyckel och g�r y till det andra v�rdet

        elif val == '2':
            z = raw_input('Ordet du s�ker: ')
            if z in ordlista:
                print 'Ditt ord', z, 'har f�ljande betydelse:', ordlista[z]
            else:
                print('Hoppsan, detta ordet finns inte i listan, f�rs�k med ett annat!')

        elif val == '3':
            print('St�nger ordlistan...')
            break

        else:
            print('V�nligen mata in ett v�rde mellan 1-3')
            

