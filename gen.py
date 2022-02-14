import requests
import os
from os import system
import time
from time import sleep
import colorama
from colorama import Fore
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

def clear():
    os.system('cls||clear')

def http():
    r= requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
    f= open('http.txt','wb')
    print(Fore.RED+'Got the request sending proxies to txt file')
    f.write(r.content)
    f.close()
    print(Fore.RED+'Proxies have been sent to http txt file')
    time.sleep(3)


def socks4():
    r= requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all')
    f= open('socks4.txt','wb')
    f.write(r.content)
    f.close()
    print(Fore.RED+'Proxies have been sent to socks4 txt file')
    time.sleep(2)


def socks5():
    r= requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all')
    f= open('socks5.txt','wb')
    f.write(r.content)
    f.close()
    print(Fore.RED+'Proxies have been sent to socks5 txt file')
    time.sleep(2)







def gui():
    print(f"""{Fore.LIGHTBLACK_EX}
    
        Proxy Scraper""")

    print(Fore.YELLOW+'1-Http Proxies(raiding)    2-Socks4 Proxies') 
    print(Fore.YELLOW+'3-Socks5 Proxies           4-Exit                ')


while True:
    clear()
    gui()
    choice= input("Select Type of Proxies You Want:")

    if choice =='1':
        http()

    elif choice =='2':
        socks4()

    elif choice =='3':
        socks5()

    elif choice =='4':
        exit(0)

    else:
        print('Invalid Choice')
        time.sleep(2)
