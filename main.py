#99059050, Sam Fortuin
from time import sleep
from string import ascii_lowercase,capwords
from os import system

i = 0
priceList = []
recieptList = ['---------[Papi Gelato]---------']

tasteDict = { 
    'aarbei':0,
    'chocolade':0,
    'munt':0,
    'vanille':0
}

def listPrint(List,delay=False):
    roomCount = len(List)
    for i in range(roomCount):
        if delay:
            sleep(0.12)
        print(List[i])

def intConvert(num):
    numConvert1 = False
    numConvert2 = True
    alphabet = list(ascii_lowercase) #creates list of lowercase alphabet
    for i in range(10):
        if str(i) in num:
            numConvert1 = True
    for x in range(26):
        if alphabet[x] in num: #checks if a letter is present in the arg
            numConvert2 = False
    if numConvert1 and numConvert2: #skips == True because of if logic
        return int(num)
    else:
        return num

def clearScreen(sleepTime=2.5):
    sleep(sleepTime)
    system("cls")

def recieptString(var,var2):
    string1 = capwords(str(var))
    string2 = str(format((var2),'.2f')).replace('.',',')
    stringOut = string1 +' = €'+string2
    return stringOut
    
def toppingReciept(var):
    recieptList.append(recieptString(toppingPass,toppingDict[var]))
    priceList.append(toppingDict[var])

def printReciept(version='particulier'):
    global tasteDict,toppingDict
    ijsPrijs = 0.95
    if version == 'particulier':
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
        recieptList.append('Ijsje '+str(i)+':')
        for x,y in tasteDict.items(): #loops trough the dict
            if y > 0:
                priceList.append(y*ijsPrijs)
                recieptList.append(recieptString(str(y)+' bolletjes '+str(x),(y*ijsPrijs)))
        if toppingPass == 'slagroom':
            toppingReciept(toppingPass)
        elif toppingPass == 'sprinkels':
            toppingReciept(toppingPass)
        elif toppingPass == 'caramel':
            if bakOfHoorn == 'bakje':
                toppingReciept('caramelBak')
            elif bakOfHoorn == 'hoorntje':
                toppingReciept('caramelHoorn')
        priceList.append(recepticleDict[bakOfHoorn])
        recieptList.append(recieptString('1 '+str(bakOfHoorn),recepticleDict[bakOfHoorn]))
        recieptList.append('-------------------------------')

    elif version == 'business':
        recieptList[0] = '-----[Papi Gelato Zakelijk]-----'
        for x,y in tasteDict.items(): #loops trough the dict
            if y > 0:
                priceList.append(y*9.8)
                recieptList.append(recieptString(str(y)+' liter '+str(x),(y*9.8)))
                recieptList.append('--------------------------------')#adds extra dash compared to particulier make reciept look right

    if again == 'n':
        while len(priceList) > 1: #adds up and deletes part of the list until there is only 1 value left which is then used in the total
            priceList[1] = priceList[0] + priceList[1]
            del priceList[0]
        recieptList.append(recieptString('totaal',priceList[0]))
        if version == 'business':
            btwPercent = 6 #change if tax changes again
            recieptList.append(recieptString(f'BTW ({btwPercent}%)',((priceList[0]/(100+btwPercent))*btwPercent))) # changed from 9%

def toppingQuestion():
    global toppingPass
    topping = input('Welke u een topping over uw ijsje?\nG) Geen\nSL) Slagroom\nSP) Sprinkels\nC) Caramel\n').lower().replace('g','ge').replace('c','ca')[:2]
    toppingDict = {
        'ge':'geen',
        'sl':'slagroom',
        'sp':'sprinkels',
        'ca':'caramel'
    }
    if topping in toppingDict:
        toppingPass = toppingDict[topping]
    else:
        print('Dat is geen topping')
        toppingQuestion()

def bakOfHoornFunc():
    bakOfHoornDict = {
        'a':'hoorntje',
        'b':'bakje'
    }

    inVar = input(f'Wilt u deze {bolAantal} bolletje(s) in \nA) een hoorntje\nB) een bakje\n').lower().replace("een","")[:1].replace('h','a')
    
    if inVar in bakOfHoornDict:
        return bakOfHoornDict[inVar]
    else:
        print('Dat is niet een optie die we aanbieden. probeer opnieuw.')
        return 7
        
def papiParticulier():
    clearScreen(1.5)
    global bolAantal, bolList, bakOfHoorn, again
    bolList = []
    bolDict = {
    'a':'aardbei',
    'c':'chocolade',
    #'m':'munt', uncomment to add mint back
    'v':'vanille'
    }
    bolAantal = intConvert(input('Hoeveel bolletjes wilt u?\n').lower())
    if isinstance(bolAantal, int): #changed from type(bolAantal) == int
        if bolAantal <= 3 and bolAantal >= 1:
            bakType = True
            while bakType:
                bakOfHoorn = bakOfHoornFunc()
                if type(bakOfHoorn) == str:
                    bakType = False
        elif bolAantal >= 4 and bolAantal <= 8:
            print(f'Dan krijgt u van mij een bakje met {bolAantal} bolletjes')
            bakOfHoorn = 'bakje'
        elif bolAantal > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            papiParticulier()
        elif bolAantal < 1 :
            print("Sorry dat is geen optie die we aanbieden...")
            papiParticulier()
        target = 1
        if bolAantal > 0 and bolAantal < 9:
            while target <= bolAantal:
                welkeBol = input(f'Welke smaak wilt u voor bolletje nummer {target}? \nA) Aardbei\nC) Chocolade\nV) Vanille\n').lower()[:1]#M) Munt\nV) Vanille\n').lower()[:1] uncomment to add mint back in
                if welkeBol in bolDict:
                    bolList.append(bolDict[welkeBol])
                    target+=1
                else:
                    print('Sorry dat is geen optie die we aanbieden...')
                    target += 0
            
            toppingQuestion()
        
            again = input('Wilt u nog meer ijsjes bestellen? (J/N)\n').lower()[:1]
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
                print("Sorry dat is geen optie die we aanbieden...")
                papiParticulier()
    else:
        print("Niet een getal, probeer het opnieuw.")
        papiParticulier()

def papiBusiness():
    global again
    target = 0
    tasteDictList = list(tasteDict)
    del tasteDictList[tasteDictList.index("munt")] #comment out if mint returns
    if "munt" in tasteDictList:
        targetNum = 4
    else:
        targetNum = 3
    while target < targetNum:
        if target == 0:
            liters = intConvert(input(f'Hoeveel liters {tasteDictList[target]}en ijs wilt u kopen?\n'))
        else:
            liters = intConvert(input(f'Hoeveel liters {tasteDictList[target]} ijs wilt u kopen?\n'))
        if isinstance(liters,int) and liters > 0: #changed from type(liters) == int
            tasteDict[tasteDictList[target]] = liters
            target+=1
        elif type(liters) != int:
            print('Dat is niet een getal.')
            target+=0
        elif liters < 1:
            print('Dat is een negatief getal.')
            target +=0
        again = 'n'
    
    clearScreen(0)
    printReciept('business')

def main():
    print('Welkom bij Papi Gelato.') #prints welcome line only at start of code
    business = input("Bent u\n1) particulier\n2) zakelijk\n")[:1]
    if business == '1' or business == 'p':#p is van particulier
        papiParticulier()
        # listPrint(recieptList)
        #[ ] check why this^ failed to print
        #[~]implemented less messy way, still no clue why it failed
        print(*recieptList,sep='\n')
    elif business == '2' or business == 'z': #z is van zakelijk
        papiBusiness()
        print(*recieptList,sep='\n')
        # listPrint(recieptList)
    else:
        print('Sorry dat is geen optie die we aanbieden...')
        clearScreen(0.8)
        main()

main()