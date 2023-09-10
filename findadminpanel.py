import requests
from colorama import Fore

def finder_admin():
    try:
        url = input('Enter Your Target Site: ')
        subs = []
        with open("subs.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                subs.append(line.strip())

        if url[-1] != '/':
            url = f"{url}/"

        result = ""
        count = 0
        for link in subs:
            count += 1
            response = requests.get(url + link)

            if response.status_code == 200:
                print(Fore.GREEN + "[+] " + url + link + " Found")
                result = link
                break

            if count > 10:
                count = 0
                print("10 subs checked but not found...")

        print("------------------")
        print(f"This is the URL of the Admin panel: {url}{result}")
    except:
        print("Error!")

finder_admin()