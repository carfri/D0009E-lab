# -*- coding: cp1252 -*-
def meny():                             #meny funktion
    print('Ordlista meny')
    print
    print('1: Lägg in ord')
    print('2: Sök ord')
    print('3: Avsluta program')

def dic1():                             #uppgift 1 funktion
    
    word = []                           #ordlistan
    beskrivning = []                    #beskrivningslistan
    
    while True:                         
        meny()                          #kallar meny funktionen
        val = raw_input('välj alternativ: ')        #ger 'val' det värde som matas in

        if val == '1':                                #om man matar in 1 så körs den
            x = raw_input('Skriv in ordet du vill lägga till: ')        #x får värdet som = det ord som anvndaren matar in

            if x in word:                                               #om 'x' redan finns i 'word' listan så körs denna
                print('Detta ordet finns redan, ta ett annat! ')

            else:                                                       #annars körs denna
                y = raw_input('Beskriv ordet: ')                        #y får värdet av ordets beskrivelse
                word.append(x)                                          #skriver in ordet 'x' i 'word' listan
                beskrivning.append(y)                                   #skriver in beskrivning 'y' i 'beskrivning' listan
                print('Ord sparat!')

        elif val == '2':                                                  #körs om 2 matas in 
            z = raw_input('Ordet du söker: ')                           #z får värdet av ordet som söks
            if z in word:                                               #om z finns i 'word' listan skrivs följande ut
                print 'Ditt ord', z, 'har följande beskrivning: ', beskrivning[word.index(z)]       #beskrivning[word.index(z)] skriver ut den beskrivning som har samma plats som ordet z i respektive listor

            else:
                print('Detta ord finns inte i ordlistan! ')

        elif val == '3':                          #om 3 matades in avslutas programmet
            print('Ordlistan Stängs...')
            break
        else:
            print('skriv in ett tal mellan 1-3.')
            
        
#############################################################################################


def dic2():

    tupp_list = []      #listan som ska bli tuppar
    final_list = []     #listan som innehåller alla tuppar

    while True:
        meny()          #kallar meny funktionen
        print
        val = raw_input('Välj alternativ: ')        #ger 'val' det värde som matas in

        if val == '1':
            x = raw_input('Skriv in ordet du vill lägga till: ')        #x får samma värde som matas in
            for z, y in final_list:                                     #en for loop som letar igenom listan efter x ??
                if z == x:                                              #om ordet redan finns uppmanas användaren att skriva in ett nytt ord
                    print 'Detta ordet finns redan! Välj ett annat. \n '
                    break
            

            else:                                                       #om ordet inte finns så uppmanas användaren att skriva in en beskrivning
                y = raw_input('Beskriv ordet: ')
                print('ord sparat!\n')
                tupp_list.append(x)                                     #skriver in ord och beskrivning i tupp listan
                tupp_list.append(y)
                tupp = tuple(tupp_list)                                 #omvandlar tupp_list till en tupp
                final_list.append(tupp)                                 #sätter in tuppen som just skapas i sista listan, den ultimata listan
                del tupp_list[:];                                       #tar bort det som finns i tupp_list för att göra plats för ett nytt ord och en ny beskrivning

        elif val == '2':
            hittad = False
            z = raw_input('Ordet du söker: ')                           #ger z värdet av det som skrevs in
            for x, y in final_list:                                     #en for loop som letar efter samma värde i final_list
                if x == z:
                    print 'Ditt ord ', x, 'har följande beskrivning:', y           #om det hittas i listan så skrivs detta ut
                    hittad = True
                    break
            if hittad == False:
                print('Hoppsan, detta ordet finns inte i listan, försök med ett annat!')

                    
        elif val == '3':                            #stänger ordlistan
            print('Stänger ordlistan...')
            break
        else:                                   #skrivs ut om man inte skriver in något mella 1-3
            print('Vänligen mata in ett värde mellan 1-3')


##############################################################################################


def dic3():

    ordlista = dict()           #gör om ordlista till ett dict

    while True:
        meny()
        print
        val = raw_input('Välj alternativ: ')

        if val == '1':
            x = raw_input('Skriv in ordet du vill lägga till: ')

            if x in ordlista:
                print('Detta ordet finns redan, ta ett annat!')

            else:
                y = raw_input('Beskriv ordet: ')
                ordlista[x] = y             #sätter in x som nyckel och gör y till det andra värdet

        elif val == '2':
            z = raw_input('Ordet du söker: ')
            if z in ordlista:
                print 'Ditt ord', z, 'har följande betydelse:', ordlista[z]
            else:
                print('Hoppsan, detta ordet finns inte i listan, försök med ett annat!')

        elif val == '3':
            print('Stänger ordlistan...')
            break

        else:
            print('Vänligen mata in ett värde mellan 1-3')
            

