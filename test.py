import numpy as np
list2 = list('a boy came to giorgia')
list3 =  np.array(list2)
list4 = ['']

ii = list(np.where(list3 == ' ')[0])

for i in range(len(list3)):
    for x in range(ii[i]):
        list4[0] += list2[0]

print(ii)