# Coded by kWAY#1701
# Github: https://github.com/kWAYTV
# Discord: kWAY#1701

# Auto Import Installer
import os
try:
    import requests, os, threading, random, time, sys
    from colorama import Fore, Back, Style
    from pystyle import Colors, Colorate, Center
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)
except:
    print("\nImports failed! Trying to install...")
    z = "python -m pip install "; os.system('%srequests' % (z)); os.system('%scolorama' % (z)); os.system('%spystyle' % (z)); os.system('%sthreading' % (z)); os.system('%sos-sys' % (z)); os.system('%sthreading' % (z)); os.system('%srandom' % (z)); os.system('%stime' % (z))
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)

## Imports

import requests, os, random, time, sys
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

# Variables
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
# create check.txt if it doesn't exist, if it does, read and split lines into vanitys list
if not os.path.exists("check.txt"):
    with open("check.txt", "w") as f:
        f.write("")
else:
    with open("check.txt", "r") as f:
        vanitys = f.read().splitlines()

count = 0
free = 0
taken = 0
error = 0
ratelimited = 0
blocked = 0
proxyDebug = False
proxyless = False
started = False
os.system(f"title Discord Vanity Checker - Starting...")
clear()


# Vanity Generator Logo
logo = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

# Prints the logo
def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

# Checker
def check():
    global count, free, taken, error, proxyDebug, proxyLess, blocked, ratelimited
    session = requests.Session()
    while True:
        for vanity in vanitys: 
            vanity = vanity.lower()
            if proxyless == True:
                r = requests.get(f'https://discord.com/api/v9/invites/{vanity}',headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': '*/*',
                'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                'X-Discord-Locale': 'en-US',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://discord.com',
                'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers',
                })
            elif proxyless == False:
                proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
                r = requests.get(f'https://discord.com/api/v9/invites/{vanity}',headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': '*/*',
                'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                'X-Discord-Locale': 'en-US',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://discord.com',
                'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers',
                }, proxies=proxyDict)
                if proxyDebug == True:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.MAGENTA}{proxyDict}{Fore.RESET}")
                else:
                    pass
            count += 1
            if 'vanity_url_code' in (r.text):
                taken += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: " + vanity)
                with open('taken.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Unknown Invite' in (r.text):
                free += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free/Termed: "+ vanity)
                with open('free.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'Access denied' in (r.text):
                blocked += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Cloudfare has blocked this IP.")
                with open('blocked.txt', 'a') as f:
                    f.write(vanity + '\n')
            if 'retry_after' in (r.text):
                ratelimited += 1
                print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RESET}Ratelimited: {Fore.YELLOW}" + vanity + f"{Fore.RESET}. Sleeping for {Fore.RED}30{Fore.RESET} seconds...")
                with open('ratelimited.txt', 'a') as f:
                    f.write(vanity + '\n')
                for i in range(30,0,-1):
                    sys.stdout.write(str(i)+' ')
                    sys.stdout.flush()
                    time.sleep(1)
                print(f"\n{Fore.GREEN}[{Fore.RESET}!{Fore.GREEN}] {Fore.RESET}Continuing{Fore.GREEN}!{Fore.RESET}")
                continue
            if proxyless == True:
                os.system(f"title Discord Vanity Checker - Free: {free} - Taken: {taken} - Blocked: {blocked} - Ratelimited: {ratelimited} - Mode: Proxyless [WARNING]")
            elif proxyless == False:
                os.system(f"title Discord Vanity Checker - Free: {free} - Taken: {taken} - Blocked: {blocked} - Ratelimited: {ratelimited} - Using proxy: {proxyDict}")

# Start the tool
clear()
printLogo()
try:
    if os.stat("check.txt").st_size == 0:
        clear()
        print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RESET}No usernames in check.txt! Exiting...")
        os.system(f"title Discord Vanity Checker - check.txt is empty! Exiting...")
        time.sleep(1)
        sys.exit()
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Found {Fore.YELLOW}{len(vanitys)}{Fore.RESET} accounts to check.")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Do you want to use a proxy?")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}1.{Fore.GREEN} Yes{Fore.RESET}")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}2.{Fore.RED} No{Fore.RESET}")
    proxyChoice = input(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Choice: ")
    if proxyChoice == "1":
        proxyless = False
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Using a proxy")
    elif proxyChoice == "2":
        proxyless = True
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Not using a proxy")
    if proxyless == False and not os.path.exists("proxies.txt"):
        with open("proxies.txt", "w") as f:
            f.write("")
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} proxies.txt does not exist! Exiting...")
        os.system(f"title Discord Vanity Checker - proxies.txt does not exist! Exiting...")
        time.sleep(1)
        sys.exit()
    elif proxyless == False and os.path.exists("proxies.txt"):
        if os.stat("proxies.txt").st_size == 0:
            clear()
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}] {Fore.RESET}No proxies in proxies.txt! Exiting...")
            os.system(f"title Discord Vanity Checker - proxies.txt is empty! Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Do you want to use proxy debug?")
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}1.{Fore.GREEN} Yes{Fore.RESET}")
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}2.{Fore.RED} No{Fore.RESET}")
            proxyDebugChoice = input(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Choice: ")
            if proxyDebugChoice == "1":
                proxyDebug = True
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Using proxy debug")
            elif proxyDebugChoice == "2":
                proxyDebug = False
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Not using proxy debug")
    elif proxyless == True:
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}] {Fore.RESET}Starting the tool with proxyless mode. Be aware of your ip.")
        time.sleep(0.5)
        pass
    while True:
        check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting. If it keeps, just close the program.")
    os.system(f"title Discord Vanity Checker - Exiting. If it keeps, just close the program.")
    time.sleep(1)
    exit()