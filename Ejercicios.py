import time

def ping_pong():
    pong = input("Pong: ")
    ping = 0
    direct = 1
    while ping < int(pong):
        i = 0
        while i < 21:
            if direct == 1:
                print("[" + (" "*i) + "o" + (" "* (20 - i)) + "]")
                if i == 20:
                    i = 0
                    ping += 1
                    direct = 0
                    break
            else:
                print("[" + (" "* (20 - i)) + "o" + (" "* i) + "]")
                if i == 20:
                    i = 0
                    ping += 1
                    direct = 1
                    break
            i += 1
            time.sleep(0.02)
    print(":)")

ping_pong()