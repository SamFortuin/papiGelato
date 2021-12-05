# list2 = 'a boy came to giorgia'.split()
# listString = ''
# for i in range(len(list2)):
#     list2[i] = list2[i].capitalize()
#     listString += list2[i]+' '
# print(listString) #prints 'A Boy Came To Giorgia'


from string import ascii_lowercase,capwords
list2 = capwords('a boy came to giorgia')
print(list2)
