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
    global count
    while True:
        for vanity in vanitys:
            proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
            if proxyDebug == True:
                print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
            else:
                pass
            r = requests.get(f'https://discord.com/api/v9/invites/{vanity}', proxies=proxyDict)
            if 'vanity_url_code' in (r.text):
                count +=1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: " + vanity + " - Checked: " +str(count))
                os.system(f'title Discord Vanity Checker ^- Checking: ' + vanity + ' ^- Status: taken')
                with open('taken.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Unknown Invite' in (r.text):
                count +=1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free/Termed: "+ vanity + " - Checked: " +str(count))
                os.system(f'title Discord Vanity Checker ^- Checking: ' + vanity + ' ^- Status: avail/termed')
                with open('free.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Access denied' in (r.text):
                count +=1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Cloudfare has blocked this IP.")
                os.system(f'title Discord Vanity Checker ^- Checking: ' + vanity + ' ^- Status: Cloudfare Blocked - Checked: ' +str(count))
                with open('blocked.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'retry_after' in (r.text):
                count +=1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Rate limited, please wait.")
                os.system(f'title Discord Vanity Checker ^- Checking: ' + vanity + ' ^- Status: Rate Limited - Checked: ' +str(count))
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