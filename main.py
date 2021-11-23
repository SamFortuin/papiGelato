def intConvert(num):
    import string
    numConvert2 = True
    alphabet = list(string.ascii_lowercase)
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



def main(abiMode=False):
    bolAantal = intConvert(input('Hoeveel boljes wilt u?\n'))
    #bolAantal = intConvert(bolAantal)
    if str(type(bolAantal)) == "<class 'int'>":
        if bolAantal <= 3 and bolAantal >= 1:
            bakOfHoorn = input(f'Wilt u deze {bolAantal} bolletje(s) in \nA) een hoorntje of \nB) een bakje?\n').lower().replace("een","").replace("a","hoorntje",1).replace("b","bakje",1)
            if bakOfHoorn == "hoorntje" or bakOfHoorn == "bakje":
                print(f'Hier is uw {bakOfHoorn} met {bolAantal} bolletje(s)')
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
        again = input('Wilt u nog meer bestellen? (J/N)').lower()
        if again == 'n':
            print('Okay, fijne dag verder.')
            exit()
        elif again == 'j':
            main()
        else:
            print("invalid input")
            main()
    else:
        print("Niet een getal, probeer het opnieuw.")
        main()

print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
main()
#main(True)