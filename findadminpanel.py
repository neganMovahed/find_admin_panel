import requests
from colorama import Fore
import urllib

def finder_admin():
    try:
        domain = input('Enter Your Target Site: ')
        subs = []
        with open("subs.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                subs.append(line.strip())

        result = ""
        count = 0
        for path in subs:
            count += 1
            url = urllib.parse.urljoin(domain, path)
            response = requests.head(url, allow_redirects=True)

            if response.status_code == 200:
                print(Fore.GREEN + "[+] " + url + " Found")
                result = url
                break

            if count > 10:
                count = 0
                print("10 subs checked but not found...")

        print("------------------")
        print(f"This is the URL of the Admin panel: {url}")

    except Exception as e:
        print(e)
        print("Error!")

finder_admin()
