#99059050, Sam Fortuin

def listPrint(List,delay=False):
    from time import sleep    
    roomCount = len(List)
    for i in range(roomCount):
        if delay:
            sleep(0.12)
        print(List[i])

def intConvert(num):
    from string import ascii_lowercase
    numConvert1 = False;numConvert2 = True
    alphabet = list(ascii_lowercase)
    for i in range(10):
        if str(i) in num:
            numConvert1 = True
    for x in range(26):
        if alphabet[x] in num:
            numConvert2 = False
    if numConvert1 == True and numConvert2 == True:
        return int(num)
    else:
        return num

def clearScreen(sleepTime=2.5):
    from time import sleep
    from os import system
    sleep(sleepTime)
    system("cls")

def recieptString(var,equals=True):
    if equals:
        var = ' = €'+str(format((var),'.2f')).replace('.',',')
    else:
        var = '€'+str(format((var),'.2f')).replace('.',',')
    return var

def printReciept(): 
    tasteDict = { 
        'aarbei':bolList.count('aardbei'),
        'chocolade':bolList.count('chocolade'),
        'munt':bolList.count('munt'),
        'vanille':bolList.count('vanille')
    }
    recepticleDict = {
        'bakje':0.75, 
        'hoorntje':1.25
    }
    toppingDict = {
        'slagroom':0.5,
        'sprinkels':0.3*bolAantal,
        'caramelHoorn':0.6,
        'caramelBak':0.9
    }
    recieptList.append('ijsje '+str(i)+':')
    for x,y in tasteDict.items(): #loops trough the dict
        if y > 0:
            priceList.append(y*1.1)
            recieptList.append(str(y)+' bolletjes '+str(x)+recieptString(y*1.1))
    if toppingPass == 'slagroom':
        recieptList.append(str(toppingPass)+recieptString(toppingDict[toppingPass]))
        priceList.append(toppingDict[toppingPass])
    elif toppingPass == 'sprinkels':
        recieptList.append(str(toppingPass)+recieptString(toppingDict[toppingPass]))
        priceList.append(toppingDict[toppingPass])
    elif toppingPass == 'caramel':
        if bakOfHoorn == 'bakje':
            recieptList.append(str(toppingPass)+recieptString(toppingDict['caramelBak']))
            priceList.append(toppingDict['caramelBak'])
        elif bakOfHoorn == 'hoorntje':
            recieptList.append(str(toppingPass)+recieptString(toppingDict['caramelHoorn']))
            priceList.append(toppingDict['caramelHoorn'])
    else:
        pass
    priceList.append(recepticleDict[bakOfHoorn])
    recieptList.append('1 '+str(bakOfHoorn)+recieptString(recepticleDict[bakOfHoorn]))
    recieptList.append('-------------------------------')
    if again == 'n':
        recieptList[len(recieptList)-1] = ('------------[Total]------------') #total instead of totaal because of concistency with the papi gelato line
        while len(priceList) > 1: #adds up and deletes part of the list until there is only 1 value left which is then used in the total
            priceList[1] = priceList[0] + priceList[1]
            del priceList[0]
        recieptList.append(recieptString(priceList[0],False))

def papiParticulier(abiMode=False):
    clearScreen(1.5)
    global bolAantal, bolList, bakOfHoorn, again, toppingPass
    bolList = []
    bolAantal = intConvert(input('Hoeveel bolletjes wilt u?\n').lower())
    if type(bolAantal) == int:
        if bolAantal <= 3 and bolAantal >= 1:
            bakOfHoorn = input(f'Wilt u deze {bolAantal} bolletje(s) in \nA) een hoorntje\nB) een bakje\n').lower().replace("een","").replace("a","hoorntje",1).replace("b","bakje",1)
            if bakOfHoorn == "hoorntje" or bakOfHoorn == "bakje":
                #print(f'Hier is uw {bakOfHoorn} met {bolAantal} bolletje(s)')
                pass
            else:
                if abiMode:
                    if bakOfHoorn == "nee":
                        print("Dan krijg je zo abi.")
                    else:
                        print('Daar kan ik niks mee abi, ik geef je gewoon zo mee.')
                else:
                    print('Dat is geen bakje of hoortje')
        elif bolAantal >= 4 and bolAantal <= 8:
            print(f'Dan krijgt u van mij een bakje met {bolAantal} bolletjes')
            bakOfHoorn = 'bakje'
        elif bolAantal >= 9:
            print('Sorry, zulke grote bakken hebben we niet')
        elif bolAantal == 0:
            again = input('Wilt u geen ijsje?').lower().replace('a','').replace('ee','')
            if again == 'n':
                print('Okay, fijne dag verder.')
                exit()
            elif again == 'j':
                papiParticulier()
            else:
                print("invalid input")
                papiParticulier()
        if bolAantal < 9:
            target = 1
            while target <= bolAantal:
                welkeBol = str(input(f'Welke smaak wilt u voor bolletje nummer {target}? \nA) Aardbei\nC) Chocolade\nM) Munt\nV) Vanille\n')).lower().replace('a','aardbei').replace('c','chocolade').replace('m','munt').replace('v','vanille')
                if welkeBol == "aardbei" or welkeBol == "chocolade" or welkeBol == "munt" or welkeBol == "vanille":
                    bolList.append(welkeBol)
                    target+=1
                else:
                    print('Dat is geen ijs smaak.')
                    target += 0
        else:
            pass

        topping = input('Welke u een topping over uw ijsje?\nG) Geen\nSL) Slagroom\nSP) Sprinkels\nC) Caramel\n').lower().replace('g','geen').replace('sl','slagroom').replace('sp','sprinkels').replace('c','caramel').replace('geeneen','geen').replace('slagroomageenroom','slagroom').replace('sprinkelsrinkels','sprinkels').replace('caramelaramel','caramel')# fixes weird thing when user enters full word instead of shorthand
        if topping == "geen" or topping == 'slagroom' or topping == 'sprinkels' or topping == 'caramel':
            toppingPass = topping
        else:
            print('Dat is geen topping')
            toppingPass = 'geen'
        
        again = input('Wilt u nog meer ijsjes bestellen? (J/N)\n').lower()
        if again == 'n':
            global i
            i+=1
            print('Okay, hier is uw bonnetje. fijne dag verder.\n\n')
            printReciept()
        elif again == 'j' or again == 'y':
            i+=1
            printReciept()
            papiParticulier()
        else:
            print("invalid input")
            papiParticulier()
    else:
        print("Niet een getal, probeer het opnieuw.")
        papiParticulier()

def papiBusiness():
    liters = intConvert(input('Hoeveel liters ijs wilt u kopen?\n'))
    if str(type(liters)) == "<class 'int'>":
        pass
    else:
        print('Niet een cijfer. Probeer opnieuw?\n')
        papiBusiness()

#variables stored outside function otherwise they resets themselves
recieptList = ['---------[Papi Gelato]---------']
priceList = []
i = 0
print('Welkom bij Papi Gelato.') #prints welcome line only at start of code
business = input("Bent u\n1) particulier\n2) zakelijk\n")
if business == '1' or business == 'particulier':
    papiParticulier()
    listPrint(recieptList,False)
elif business == '2' or business == 'zakelijk':
    papiBusiness()
else:
    print('Niet een optie probeer opnieuw')

#TODO if ordering too much icecream still asks for sprinkles
#TODO find a way to do replace statements where aplicable