
"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        creat by Amir Hossein Tadas & TAHA
"""

import os
import requests
import json
from colorama import Fore
import sys


def __start__():

    print(Fore.RED+"\n [!] Enter The Domain/ip\n")

    website = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"~"+Fore.WHITE+"@Reverse_IP"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")

    mysite = {"remoteAddress": website}

    link = requests.post(
        "https://domains.yougetsignal.com/domains.php", mysite)

    source = json.loads(link.content)

    for data in source["domainArray"]:
        print(Fore.BLUE+" "+data[0]+"\n")

    try:

        input(Fore.RED+" [!] "+Fore.GREEN+"Back To again (Press Enter...) ")
    except:
        print("")
        sys.exit()


if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()
