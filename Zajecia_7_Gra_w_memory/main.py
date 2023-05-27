'''
Emoji - https://getemoji.com/
Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
import time

symbole = ['🐶','🐱','🐭','🐹','🐰','🦊','🐼','🐻','🐨','🐯','🦁','🐮','🐷','🐥','🦆']
plansza = list()
elementy = 2*len(symbole)
planszaCzyOdkryte = [False]*30

for symbol in symbole:
    plansza.append(symbol)
    plansza.append(symbol)
    
random.shuffle(plansza)

for i, symbol in enumerate(plansza):
    print(symbol, end=" ")
    
    if ((i+1) % 6 == 0):
        print(' ')
        
punkty = 0
while punkty < 15:
    for i, czyOdkryte in enumerate(planszaCzyOdkryte):
        if czyOdkryte == True:
            print(' ', end=" ")
        else:
            print("#", end=" ")
            
        if ((i+1) % 6 == 0):
            print(' ')
            
    wiersz1 = int(input('Podaj pierwszego wiersz: '))          
    kolumna1 = int(input('Podaj pierwszego kolumne: '))
    
    wiersz2 = int(input('Podaj pierwszego wiersz: '))
    kolumna2 = int(input('Podaj pierwszego kolumne: '))
    
    figura1 = (wiersz1 - 1)*6 + kolumna1 -1
    figura2 = (wiersz2 - 1)*6 + kolumna2 -1
    
    #print(figura1)
    #print(figura2)
    
    for i, symbol in enumerate(plansza):
        if (i == figura1 or i == figura2):
            print(symbol, end=" ")
        elif planszaCzyOdkryte[i] == True:
            print(" ", end=" ")
        else:
            print("#", end=" ")
        
        if ((i+1) % 6 == 0):
            print(' ')
            
    time.sleep(5)
    
    if plansza[figura1] == plansza[figura2]:
        planszaCzyOdkryte[figura1] = True
        planszaCzyOdkryte[figura2] = True
        punkty += 1
        print('\nBrawo! Zdobywasz punkt! Masz: ' + str(punkty) + ' punkty')
    else:
        print('\nNiesety! Spróbuj ponownie! Masz: ' + str(punkty) + ' punkty')
    
