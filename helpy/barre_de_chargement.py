import time
import sys
import os
from os import *




#1  

done = 'false'
a = 1
b = 2
#here is the animation

while a != b:
    a += 1
    sys.stdout.write('\rloading |')
    time.sleep(0.5)
    sys.stdout.write('\rloading /')
    time.sleep(0.5)
    sys.stdout.write('\rloading -')
    time.sleep(0.5)
    sys.stdout.write('\rloading \\')
    time.sleep(0.5)
sys.stdout.write('\rDone!     ')


#2
from tqdm import tqdm
for i in tqdm(range(0,int(10000000))):
  continue

system('cls')
#3
#pip install os
#pip install time
#pip install colorama
#pip install tqdm
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

for i in tqdm (range (101),  
               desc=Fore.GREEN + "Loading. . .",  
               ascii=False, ncols=75): 
    time.sleep(0.01)       

#the Fore.GREEN adds colour to the loading bar
print(Fore.GREEN + "Complete. . .") 
time.sleep(1) 
#this will clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')
