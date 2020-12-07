# SPECYFIKAJCA:
# wejscie: n - liczba naturalna
# wyjscie: tab - tablica liczb pierwszych w przedziale ( 2 ; n )


from wdi import *

def Eratostenes(n, tab):
    i = 2
    while i < n + 1:
        j = i + i
        while j < n + 1:
            tab[j] = 0
            j += i
        i += 1
    return tab
    
n = 100
tab = Array(n + 1)

for i in range(n+1):
    tab[i] = 1
    
Eratostenes(n, tab)
    
for i in range(2, n+1):
    printf("%d : %d \n", i, tab[i])
    
