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
    numConvert2 = True
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

def clearScreen(sleepTime):
    from time import sleep
    from os import system
    sleep(sleepTime)
    system("cls")

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
        'geen':0,
        'slagroom':0.5,
        'sprinkles':0.3,#per bol
        'caramelHoorn':0.6,
        'caramelBak':0.9
    }
    recieptList.append('ijsje '+str(i)+':')
    for x,y in tasteDict.items(): #loops trough the dict
        if y > 0:
            priceList.append(y*1.1)
            recieptList.append(str(y)+' bolletjes '+str(x)+' = €'+str(format((y*1.1),'.2f')).replace('.',','))
    priceList.append(recepticleDict[bakOfHoorn])
    recieptList.append('1 '+str(bakOfHoorn)+' = € '+str(recepticleDict[bakOfHoorn]).replace('.',','))
    recieptList.append('-------------------------------')
    if again == 'n':
        recieptList[len(recieptList)-1] = ('------------[Total]------------') #total instead of totaal because of concistency with the papi gelato line
        while len(priceList) > 1: #adds up and deletes part of the list until there is only 1 value left which is then used in the total
            priceList[1] = priceList[0] + priceList[1]
            del priceList[0]
        recieptList.append('€'+str(format(priceList[0],'.2f')).replace('.',','))

def papi(abiMode=False):
    clearScreen(1.5)
    global bolAantal, bolList, bakOfHoorn, again
    bolList = []
    bolAantal = intConvert(input('Hoeveel bolletjes wilt u?\n').lower())
    if str(type(bolAantal)) == "<class 'int'>":
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
                main()
            else:
                print("invalid input")
                main()
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
        
        again = input('Wilt u nog meer ijsjes bestellen? (J/N)\n').lower()
        if again == 'n':
            global i
            i+=1
            print('Okay, hier is uw bonnetje. fijne dag verder.\n\n')
            printReciept()
        elif again == 'j' or again == 'y':
            i+=1
            printReciept()
            main()
        else:
            print("invalid input")
            main()
    else:
        print("Niet een getal, probeer het opnieuw.")
        main()

#variables stored outside function otherwise they resets themselves
recieptList = ['---------[Papi Gelato]---------']
priceList = []
i = 0
print('Welkom bij Papi Gelato.') #prints welcome line only at start of code
papi()
listPrint(recieptList,False)