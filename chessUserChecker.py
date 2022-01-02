import requests
from termcolor import colored
import time
import concurrent.futures
import os
os.system('title Chess.com Username Checker @socialmediaboosterlb')

available = open('availableChess.txt', 'a+')
notAvailable = open('notAvailableChess.txt', 'a+')
def check(user):
    validtxt='"valid":true'
    invalidtxt='"valid":false'
    link = "https://www.chess.com/callback/user/valid?username="+user
    response= requests.get(link).text
    if validtxt in response:
        print(colored("[+]AVAILABLE "+ user,'green'))
        available.write(user + "\n")
    elif invalidtxt in response:
        print(colored("[-]TAKEN "+ user,'red'))
        notAvailable.write(user + "\n")
    else:
        pass    
print(colored('''
░█████╗░██╗░░██╗███████╗░██████╗░██████╗░░░░█████╗░░█████╗░███╗░░░███╗
██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝░░░██╔══██╗██╔══██╗████╗░████║
██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░░░░██║░░╚═╝██║░░██║██╔████╔██║
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗░░░██║░░██╗██║░░██║██║╚██╔╝██║
╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝██╗╚█████╔╝╚█████╔╝██║░╚═╝░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝

██╗░░░██╗░██████╗███████╗██████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░████║██╔════╝
██║░░░██║╚█████╗░█████╗░░██████╔╝██╔██╗██║███████║██╔████╔██║█████╗░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██████╔╝███████╗██║░░██║██║░╚███║██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

https://github.com/socialmediaboosterlb Discord:socialmediabooster#9199
''','yellow'))

lol = input(colored("press Enter to start checking","yellow"))
time.sleep(.5)
with open('usernames.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)