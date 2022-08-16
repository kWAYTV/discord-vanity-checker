import requests, os, threading, random, time
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
vanitys = open('check.txt', 'r').read().split('\n')
clear()
os.system(f'title Discord Vanity Checker ^- Input thread number!')
threads = input(f"Threads?: ")
os.system(f'title Discord Vanity Checker ^- Threads: ' + str(threads) + ' - Ready!')
clear()
count = 0
free = 0
taken = 0
ratelimited = 0
blocked = 0
proxyDebug = False

# Vanity Generator Logo
logo = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

def check():
    global count, free, taken, ratelimited, blocked
    while True:
        for vanity in vanitys:
            proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
            if proxyDebug == True:
                print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
            else:
                pass
            r = requests.get(f'https://discord.com/api/v9/invites/{vanity}', proxies=proxyDict)
            count += 1
            if 'vanity_url_code' in (r.text):
                taken += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: " + vanity + " - Checked: " +str(count))
                with open('taken.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Unknown Invite' in (r.text):
                free += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free/Termed: "+ vanity + " - Checked: " +str(count))
                with open('free.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Access denied' in (r.text):
                blocked += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Cloudfare has blocked this IP.")
                with open('blocked.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'retry_after' in (r.text):
                ratelimited += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Rate limited, please wait.")
                with open('ratelimited.txt', 'a') as f:
                    f.write(vanity + '\n')

clear()
printLogo()
try:
    while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
    time.sleep(1)
    exit()