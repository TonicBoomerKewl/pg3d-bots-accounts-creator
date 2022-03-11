# Made By: TonicBoomerKewl (AKA DarkOctet)
# Do Provide Credit while Using!

# Note: This is Patched from Pixel Gun 3D v21.4.0 Onwards! (Educational Purposes Only.)

# Compile to EXE Command: (Using: PyInstaller v5.0, Python v3.9.10)
# pyinstaller --onefile --name "PG3D-Bots-Accounts-Creator-v2.4.0" "TestScript15.py"

from asyncio import run
from collections import OrderedDict
from json import loads, dumps
from json.decoder import JSONDecodeError
from random import choice, randint
from string import hexdigits, ascii_uppercase, printable
from threading import Thread
from time import time, strftime, localtime, sleep, gmtime

from colorama import init, Fore
from requests import post
from websockets import ConnectionClosed
from websockets import connect

HEX = hexdigits[:16]

# Made By: TonicBoomerKewl (AKA DarkOctet)

def _hex_(n):
    return ''.join(choice(HEX) for _ in range(n))

# Made By: TonicBoomerKewl (AKA DarkOctet)

def getauthjson(device_id=_hex_(32), uniq_id='', _hash_='',
                device_model=(choice(["samsung", "huawei", "sony", "pixel", "xiaomi", "oppo", "microsoft", "motorola",
                                      "Google", "grunt", "Lenovo", "Nokia", "HTC", "panasonic", "sharp", "vivo"]),
                              ''.join(choice(ascii_uppercase) for _ in range(2)) + '-' + choice(ascii_uppercase) +
                              ''.join(str(randint(0, 9)) for _ in range(3)) + choice(ascii_uppercase)),
                cpu_model=choice(["ARMv" + str(randint(1, 9)), "armeabi", "AArch" + choice(('32', '64')),
                                  "arm" + choice(('32', '64')), "x86", "x86abi", "Qualcomm " + str(randint(100, 999)),
                                  "Exynos " + str(randint(100, 999))]) + ' ' + choice(
                    ["VFP", "Snapdragon ", ''.join(choice(ascii_uppercase) for _ in range(3))]) + 'v' + str(
                    randint(1, 9)) + ' ' + choice(  # Made By: TonicBoomerKewl (AKA DarkOctet)
                    ("NEON", ''.join(choice(ascii_uppercase) for _ in range(randint(2, 6))))),
                cpu_frequency=str(randint(1000, 9999)), cpu_cores=str(randint(2, 24)), ram=str(randint(1000, 9999)),
                platform='1', version="21.4.0", new_id_v3='0', pg3dhost="pixelgunserver.com"):
    req = post("https://server-v2." + pg3dhost + "/auth/",
               headers=OrderedDict([("Host", "server-v2." + pg3dhost), ("Accept-Encoding", "gzip, identity"),
                                    ("Connection", "Close, TE"), ("TE", "identity"), ("User-Agent", "BestHTTP"),
                                    ("Content-Type", "application/json"), ("Content-Length", ''), ("Accept", None)]),
               data='{"uniq_id":"' + uniq_id + '", "hash":"' + _hash_ + '", "device_id":"' + device_id +
                    '", "device_model":"' + device_model[0] + ' ' + device_model[1] + '", "cpu_model":"' + cpu_model +
                    '", "cpu_frequency":"' + cpu_frequency + '", "cpu_cores":"' + cpu_cores + '", "ram":"' + ram +
                    '", "platform":"' + platform + '", "version":"' + version + '"' +
                    ('' if new_id_v3 == '0' else ', "new_id_v3":"' + new_id_v3 + '"') + '}')
    return req.json(), req.cookies

# Made By: TonicBoomerKewl (AKA DarkOctet)

if __name__ == "__main__":
    init(autoreset=True)

    print(Fore.LIGHTGREEN_EX + "You are Currently Using" + Fore.GREEN +
          " Pixel Gun 3D Bots Accounts Creator Version 2.4.0" + Fore.LIGHTGREEN_EX + " Made By" + Fore.GREEN +
          " TonicBoomerKewl#8349 !" + Fore.RESET)

    successAccounts = 0
    attemptedAccounts = 0
    startTime = time()

    log = ['=' * 19 + "[Begin Log(s):]=[" + strftime("%H:%M:%S", localtime()) + "]" + '=' * 19]

    wssUrl = "wss://server-v2.pixelgunserver.com:443/socket.io/?EIO=4&transport=websocket&client_ver=v2"
    # Made By: TonicBoomerKewl (AKA DarkOctet)

    print(Fore.LIGHTBLUE_EX + '=' * 20 + Fore.BLUE + "[Important Setting(s):]" + Fore.LIGHTBLUE_EX + '=' * 21 +
          Fore.RESET)

    try:
        threads = int(input("(Default: 2) Number of Thread(s): "))
    except ValueError:
        threads = 2

    if not threads or threads <= 0:
        threads = 2

    print(Fore.CYAN + "Number of Thread(s) have been Set to " + Fore.LIGHTCYAN_EX + str(threads) + Fore.CYAN +
          " Thread(s)!" + Fore.RESET)

    logs = input("(Recommended) Name of Text File to Log Account(s) Information: ")

    if logs:  # Made By: TonicBoomerKewl (AKA DarkOctet)
        if logs[-4:] != ".txt":
            logs += ".txt"
        print(Fore.CYAN + 'Name of Text File to Log Account(s) Information have been Set to "' + Fore.LIGHTCYAN_EX +
              logs + Fore.CYAN + '"!' + Fore.RESET)
        print(Fore.CYAN + 'Logging Format: "' + Fore.LIGHTCYAN_EX + "<Player ID>" + Fore.CYAN + '|' + Fore.LIGHTCYAN_EX
              + "<Player Hash>" + Fore.CYAN + '|' + Fore.LIGHTCYAN_EX + "<Device ID>" + Fore.CYAN + '"' + Fore.RESET)
    else:
        print(Fore.CYAN + "Account(s) Information Logging to Text File have been " + Fore.RED + "Disabled" + Fore.CYAN +
              '!' + Fore.RESET)

    try:  # Made By: TonicBoomerKewl (AKA DarkOctet)
        maxaccounts = int(input("(Default: 32) Maximum Number of Account(s): "))
    except ValueError:
        maxaccounts = 32

    if not maxaccounts or maxaccounts <= 0:
        maxaccounts = 32

    print(Fore.CYAN + "Maximum Number of Accounts(s) have been Set to " + Fore.LIGHTCYAN_EX + str(maxaccounts) + Fore
          .CYAN + " Accounts(s)!" + Fore.RESET)

    print(Fore.LIGHTBLUE_EX + '=' * 14 + Fore.BLUE + "[Option(s):]==[Leave Blank to Skip:]" + Fore.LIGHTBLUE_EX + '=' *
          14 + Fore.RESET)

    options = [  # Made By: TonicBoomerKewl (AKA DarkOctet)
        input("Nickname of Bot(s): "),
        input("Clan ID to Join Per Bot: "),
        input("Join Clan Request Text: "),
        input("Player ID to Spam Friend Request: "),
        input("Player ID to Spam Like Lobby: "),
        input("Number of Likes to Send Per Bot: "),
        input("Name of Clan to Spam Create: ")
    ]  # Made By: TonicBoomerKewl (AKA DarkOctet)

    if not options[5]:
        options[5] = '1'

    print(Fore.LIGHTBLUE_EX + '=' * 9 + Fore.BLUE + "[Advanced Option(s):]==[Leave Blank to Skip:]" + Fore.LIGHTBLUE_EX
          + '=' * 10 + Fore.RESET)

    print(Fore.CYAN + "Custom Websocket Request(s) (" + Fore.LIGHTCYAN_EX + "Separated" + Fore.CYAN + " By '" +
          Fore.LIGHTCYAN_EX + ';' + Fore.CYAN + "') (" + Fore.LIGHTCYAN_EX + "Variable(s)" + Fore.CYAN +
          " Allowed) (Include " + Fore.LIGHTCYAN_EX + "Quote(s)" + Fore.CYAN + "): " + Fore.RESET, end='')

    custom = [input()]

    for r in [h.strip() for h in custom[0].split(';')]:
        if r:
            custom.append(r)

    custom = custom[1:]  # Made By: TonicBoomerKewl (AKA DarkOctet)

    if custom:
        print(Fore.LIGHTCYAN_EX + str(len(custom)) + Fore.CYAN + " Custom Websocket Request(s) has " + Fore.GREEN +
              "Loaded" + Fore.CYAN + '!' + Fore.RESET)
    else:
        print(Fore.CYAN + "Custom Websocket Request(s) " + Fore.RED + "Disabled" + Fore.CYAN + '!' + Fore.RESET)

    print(Fore.LIGHTBLUE_EX + '=' * 21 + Fore.BLUE + "[Preparing Thread(s):]" + Fore.LIGHTBLUE_EX + '=' * 21 +
          Fore.RESET)


    async def creatorthread():  # Made By: TonicBoomerKewl (AKA DarkOctet)
        global successAccounts, attemptedAccounts
        while maxaccounts > successAccounts:
            attemptedAccounts += 1
            d = _hex_(32)
            try:
                t, cookie = getauthjson(device_id=d)
                if "err_code" in t and t["err_code"] == 3000:
                    print(Fore.RED + "Warning: You may have been IP-Banned! (Fake Server Maintenance)" + Fore.RESET)
                t = t["token"]
                cookie = dict(cookie)["AWSALB"]
            except (ValueError, KeyError, JSONDecodeError):
                del d
                continue
            if t.startswith("b7efbb998dc0273e"):
                print(Fore.RED + "Warning: You may have been IP-Banned! (Old Token)" + Fore.RESET)
            async with connect(uri=wssUrl, ping_interval=15, ping_timeout=60,  # Made By: TonicBoomerKewl (AKA DarkOctet)
                               extra_headers=[("Cache-Control", "no-cache"),
                                              ("Pragma", "no-cache"),
                                              ("Accept-Encoding", "gzip, identity"),
                                              ("TE", "identity"),
                                              ("User-Agent", "BestHTTP"),
                                              ("Content-Length", '0'),
                                              ("Cookie",
                                               "AWSALB=" + cookie + "; SameSite=None" if cookie else None)]) as w:
                await w.send('40/sio')
                try:
                    sid = loads((await w.recv())[1:])["sid"]
                except (KeyError, JSONDecodeError):
                    del t  # Made By: TonicBoomerKewl (AKA DarkOctet)
                    del cookie
                    del d
                    continue
                await w.send('42/sio,["auth",{"uniq_id":"","hash":"","device":"' + d + '","token":"' + t +
                             '","platform":"1","device_model":"","type_device":2,"abuse_method":1,"block_param":1,' +
                             '"req_id":1,"sid":"' + sid + '"}]')
                req_id = 2
                for _ in range(4):  # Made By: TonicBoomerKewl (AKA DarkOctet)
                    try:
                        j = await w.recv()
                        if j == '41/sio':
                            print(Fore.RED + "Warning: You may have been IP-Banned! (Received 41/sio)" + Fore.RESET)
                        j = loads(j[7:])[1]
                    except (ConnectionClosed, JSONDecodeError, IndexError):
                        continue
                    if "id" in j:
                        if j["id"] == 244098477:  # Made By: TonicBoomerKewl (AKA DarkOctet)
                            print(Fore.RED + "Warning: You may have been IP-Banned! (Old Player)" + Fore.RESET)
                        if "secret" in j and "new_player" in j and j["new_player"]:
                            successAccounts += 1
                            if logs:
                                log.append(str(j["id"]) + '|' + j["secret"] + '|' + d)
                            if options[0]:
                                await w.send('42/sio,["update_player",{"nick":"' + options[0] + '","req_id":' + str(
                                    req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                            if options[1]:
                                await w.send('42/sio,["ask_to_join_clan",{"clan_id":"' + options[1] + '","text":"' +
                                             options[2] + '","req_id":' + str(req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                                await w.send('42/sio,["accept_invite_to_join_clan",{"clan_id":"' + options[1] +
                                             '","req_id":' + str(req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                            if options[3]:
                                await w.send('42/sio,["friend_request",{"whom":"' + options[3] + '","type":0,"req_id":'
                                             + str(req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                            if options[4]:
                                await w.send('42/sio,["evaluate_lobby",{"like":' + options[5] + ',"player_id":"' +
                                             options[4] + '","req_id":' + str(req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                            if options[6]:
                                await w.send('42/sio,["create_clan_v2",{"name":"' + (options[6] + ' ' + ''.join(
                                    choice(printable) for _ in range(6))).replace('\\', '\\\\').replace('"', '\\"') +
                                             '","logo":"","slogan":"","type":1,"continent":"","min_rank":0,"req_id":' +
                                             str(req_id) + ',"sid":"' + sid + '"}]')
                                req_id += 1
                            for n in custom:  # Made By: TonicBoomerKewl (AKA DarkOctet)
                                try:
                                    e = str(eval(n))
                                except:
                                    print(Fore.RED + 'Error: An Error Occurred while Evaluating "' + Fore.LIGHTRED_EX +
                                          str(n) + Fore.RED + '", Skipping! (Python Syntax Error(s))' + Fore.RESET)
                                    continue
                                if e.startswith('42/sio,["') and e[-2:] == '}]':
                                    try:
                                        e = loads(e[7:])
                                        e[1]["req_id"] = req_id
                                        e[1]["sid"] = sid
                                        e = "42/sio," + dumps(e)
                                    except (ValueError, KeyError, JSONDecodeError):
                                        print(Fore.RED + 'Error: An Error Occurred while Parsing "' + Fore.LIGHTRED_EX +
                                              str(n) + Fore.RED + '", Skipping! (JSON Syntax Error(s))' + Fore.RESET)
                                        del e
                                        continue
                                    req_id += 1
                                await w.send(e)
                                del e
                            del j
                            break
                    del j
            del t
            del cookie
            del d
            del req_id
            del sid  # Made By: TonicBoomerKewl (AKA DarkOctet)


    def newthread():
        run(creatorthread())


    try:
        for i in range(1, threads + 1):
            Thread(target=newthread).start()
            print("Thread-" + Fore.LIGHTWHITE_EX + str(i) + Fore.RESET + " has " + Fore.GREEN + "Started" + Fore.RESET +
                  '!')
            sleep(0.01)
    except:  # Made By: TonicBoomerKewl (AKA DarkOctet)
        print(Fore.RED + "Error: A Very Rare Type of Error has Occurred while Starting " + Fore.LIGHTRED_EX + str(
            threads) + Fore.RED + " Thread(s)! (To Fix: Restart this Program, and Use Less Thread(s))" + Fore.RESET)

    print(Fore.LIGHTBLUE_EX + '=' * 18 + Fore.BLUE + "[Begin Creating Account(s):]" + Fore.LIGHTBLUE_EX + '=' * 18 +
          Fore.RESET)


    def gettimestamp():
        return Fore.RESET + '[' + Fore.LIGHTWHITE_EX + strftime("%H:%M:%S", gmtime(time() - startTime)) + Fore.RESET + \
               ']'


    while attemptedAccounts <= 0:
        continue  # Made By: TonicBoomerKewl (AKA DarkOctet)

    while maxaccounts > successAccounts:
        sleep(1)
        print(gettimestamp() + " Total Acc(s): " + Fore.LIGHTWHITE_EX + str(successAccounts) + Fore.RESET +
              " | Acc(s) / Sec: " + Fore.LIGHTWHITE_EX + str(round(successAccounts / (time() - startTime), 2)) +
              Fore.RESET + " | Success: " + Fore.LIGHTWHITE_EX + str(round((successAccounts / attemptedAccounts) * 100))
              + '%' + Fore.RESET)
        if logs and log:
            k = len(log)
            with open(logs, 'a') as f:
                for i in log[:k]:
                    f.write(i + '\n')
            log = log[k:]
            del k

    print(gettimestamp() + " Maximum Number of Account(s) (" + Fore.LIGHTWHITE_EX + str(maxaccounts) + Fore.RESET +
          " Acc(s)) has Been Reached; " + Fore.RED + "Stopping" + Fore.RESET + '!')

    print("Press Enter to " + Fore.RED + "Exit" + Fore.RESET + "... ", end='')
    input()
    exit()

# Made By: TonicBoomerKewl (AKA DarkOctet)
