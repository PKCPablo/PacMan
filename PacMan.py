import os
import subprocess
import time
import replit
from pynput import keyboard
from colorama import Fore, init
init(autoreset=True)

#Mapa#
'''  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27
0  ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",]
1  ["-","*","*","*","*","*","*","*","*","*","*","*","*","-","-","*","*","*","*","*","*","*","*","*","*","*","*","-",]
2  ["-","*","-","-","-","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-","-","-","-","*","-",]
3  ["-","*","-"," "," ","-","*","-"," "," "," ","-","*","-","-","*","-"," "," "," ","-","*","-"," "," ","-","*","-",]
4  ["-","*","-","-","-","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-","-","-","-","*","-",]
5  ["-","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","-",]
6  ["-","*","-","-","-","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-","-","-","-","*","-",]
7  ["-","*","-","-","-","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-","-","-","-","*","-",]
8  ["-","*","*","*","*","*","*","-","-","*","*","*","*","-","-","*","*","*","*","-","-","*","*","*","*","*","*","-",]
9  ["-","-","-","-","-","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-","-","-","-","-","-",]
10 [" "," "," "," "," ","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-"," "," "," "," "," ",]
11 [" "," "," "," "," ","-","*","-","-","*","*","*","*","*","*","*","*","*","*","-","-","*","-"," "," "," "," "," ",]
12 [" "," "," "," "," ","-","*","-","-","*","-","-","-"," ","O","-","-","-","*","-","-","*","-"," "," "," "," "," ",]
13 ["-","-","-","-","-","-","*","-","-","*","-"," "," "," "," "," "," ","-","*","-","-","*","-","-","-","-","-","-",]
14 ["-","*","*","*","*","*","*","*","*","*","-"," "," "," "," "," "," ","-","*","*","*","*","*","*","*","*","*","-",]
15 ["-","-","-","-","-","-","*","-","-","*","-"," "," "," "," "," "," ","-","*","-","-","*","-","-","-","-","-","-",]
16 [" "," "," "," "," ","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-"," "," "," "," "," ",]
17 [" "," "," "," "," ","-","*","-","-","*","*","*","*","*","*","*","*","*","*","-","-","*","-"," "," "," "," "," ",]
18 [" "," "," "," "," ","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-"," "," "," "," "," ",]
19 ["-","-","-","-","-","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-","-","-","-","-","-",]
20 ["-","*","*","*","*","*","*","*","*","*","*","*","*","-","-","*","*","*","*","*","*","*","*","*","*","*","*","-",]
21 ["-","*","-","-","-","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-","-","-","-","*","-",]
22 ["-","*","-","-","-","-","*","-","-","-","-","-","*","-","-","*","-","-","-","-","-","*","-","-","-","-","*","-",]
23 ["-","*","*","*","-","-","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","-","-","*","*","*","-",]
24 ["-","-","-","*","-","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-","-","*","-","-","-",]
25 ["-","-","-","*","-","-","*","-","-","*","-","-","-","-","-","-","-","-","*","-","-","*","-","-","*","-","-","-",]
26 ["-","*","*","*","*","*","*","-","-","*","*","*","*","-","-","*","*","*","*","-","-","*","*","*","*","*","*","-",]
27 ["-","*","-","-","-","-","-","-","-","-","-","-","*","-","-","*","-","-","-","-","-","-","-","-","-","-","*","-",]
28 ["-","*","-","-","-","-","-","-","-","-","-","-","*","-","-","*","-","-","-","-","-","-","-","-","-","-","*","-",]
29 ["-","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","-",]
30 ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",]
'''
#Definiciones#

def prinMapa(mapa):
  a=""
  for f in range(31): #filas
    for c in range(28):
      a+= mapa[f][c] + " "
    print(a)
    a=""

def tiempo(x):
  time.sleep(x)

################################
################################
################################

#Programa#

pac = Fore.RED + "O"
pos = [12,14] #Fila/Columna
direcBase = [-1,0]

# [////][-1,0][////]    |    [/][1][/]
# [0,-1][////][0, 1]    |    [4][0][2]
# [////][1, 0][////]    |    [/][3][/]

mapa = [
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"," ",pac,Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [" "," "," "," "," ",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"," "," "," "," "," "],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.YELLOW + "*",Fore.BLUE + "-"],
  [Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-",Fore.BLUE + "-"]
]

################################
################################
################################

subproceso1 = subprocess.Popen(['python', 'Listener.py']) #Subproceso para detectar teclas

#Bucle tiempo#

tecla = None

with open("pos.txt","w") as f:
	f.write(str(pos[0]) + " " + str(pos[1]))

posNext = pos
posDirec = direcBase
cont = 0

aux = True

while aux==True:

  prinMapa(mapa)
  with open("log.txt","r") as f: #Leer log de teclas pulsadas
			tecla = f.readline()

  with open("log.txt","w") as f: # Borrar log
    f.write("")

  line = ""
  for i in range(len(tecla)):
    line += str(ord(tecla[i])) + " "

  if line=="75 101 121 46 117 112 10 ": # Key.Up (Arriba)
    posDirec = [-1,0]
  elif line=="75 101 121 46 100 111 119 110 10 ": # Key.Down (Abajo)
    posDirec = [1,0]
  elif line=="75 101 121 46 114 105 103 104 116 10 ": # Key.Right (Derecha)
    posDirec = [0,1]
  elif line=="75 101 121 46 108 101 102 116 10 ": # Key.Left (Izquierda)
    posDirec = [0,-1]


  with open("pos.txt","r") as f:
  	read = f.readline()

  posAnt = read.split()

  if mapa[int(posAnt[0]) + posDirec[0]][int(posAnt[1]) + posDirec[1]]!=Fore.BLUE + "-":
    direc = posDirec

  posNext[0] = int(posAnt[0]) + direc[0]
  posNext[1] = int(posAnt[1]) + direc[1]

  if posNext==[14, 0]:
  	posNext=[14, 26]
  elif posNext==[14, 27]:
  	posNext=[14, 1]

  if mapa[posNext[0]][posNext[1]]!=Fore.BLUE + "-":
  	with open("pos.txt","w") as f:
  		f.write(str(posNext[0]) + " " + str(posNext[1]))

  	if mapa[posNext[0]][posNext[1]]==Fore.YELLOW + "*": #Puntuación
  		cont+=10

  	mapa[posNext[0]][posNext[1]] = pac
  	mapa[int(posAnt[0])][int(posAnt[1])] = " "

  #Display#
  #print(posNext) #debug
  print()
  print("Score: {0}".format(cont))
  #print("Lives: <3 <3 <3") #desarrollar
  tiempo(0.1) #Tasa de tiempo entre cada recarga de imagen
  replit.clear()