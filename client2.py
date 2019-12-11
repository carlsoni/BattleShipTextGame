import socket
import select
import errno
import sys

def check_valid(message, NUMBER_LENGTH):

    while True:
        inval = False
        if len(message) == NUMBER_LENGTH:
            params = message.split()
            try:
                lo1 = int(params[1])
            except:
                inval = True
            if not inval:
                if lo1 > 0 and lo1 < 9:
                    if not(params[0].lower() != "a".lower() and params[0].lower() != 'b'.lower() and params[0].lower() != 'c'.lower() and params[0].lower() != 'd'.lower() and params[0].lower() != 'e'.lower()):
                        break
        print("invalid input, EX: C 4 (include space)")
        message = input("Try Again: ")
    return message
def process_guess(message, a, b, c, d, e):
    locations = message.split()
    locNum = int(locations[1])
    locNum -= 1
    if locations[0].lower() == "a".lower():
        if a[locNum] >= 1:
            a[locNum] = -1
            return "HIT"
    elif locations[0].lower() == "b".lower():
        if b[locNum] >= 1:
            b[locNum] = -1
            return "HIT"
    elif locations[0].lower() == "c".lower():
        if c[locNum] >= 1:
            c[locNum] = -1
            return "HIT"
    elif locations[0].lower() == "d".lower():
        if d[locNum] >= 1:
            d[locNum] = -1
            return "HIT"
    elif locations[0].lower() == "e".lower():
        if e[locNum] >= 1:
            e[locNum] = -1
            return "HIT"
    return "MIS"
def modify_guess_map (message2, message, enA, enB, enC, enD, enE):
    params = message.split()
    numParam = int(params[1])
    numParam = numParam - 1
    tile = "X"
    if message2.lower() == "mis".lower():
        tile = "-1"
    if params[0].lower() == "a".lower():
        enA[numParam] = tile
    elif params[0].lower() == "b".lower():
       enB[numParam] = tile
    elif params[0].lower() == "c".lower():
        enC[numParam] = tile
    elif params[0].lower() == "d".lower():
        enD[numParam] = tile
    elif params[0].lower() == "e".lower():
        enE[numParam] = tile
def check_if_loss(a, b, c, d, e):
    for i in range(len(a)):
        if a[i] > 0:
            return False
    for i in range(len(b)):
        if b[i] > 0:
            return False
    for i in range(len(c)):
        if c[i] > 0:
            return False
    for i in range(len(d)):
        if d[i] > 0:
            return False
    for i in range(len(e)):
        if e[i] > 0:
            return False
    return True
def print_loss_message():
    print("*************************")
    print("      You Have Lost      ")
    print("      Player 1 won!      ")
    print("  Better Luck next Time! ")
    print("*************************")
def print_win_message():
    print("*************************")
    print("      You Have Won       ")
    print("      Congratulations    ")
    print("*************************")
def create_2_tile_ship(a, b, c, d, e,vert,locHead0,locHead1,a1,b1,c1,d1,e1):
    if locHead0.lower == a1.lower:
        if vert:
            a[locHead1 - 1] += 1
            b[locHead1 - 1] += 1
            return True
        else:
            a[locHead1] += 1
            a[locHead1 - 1] += 1
            return True
    elif locHead0.lower == b1.lower:
        if vert:
            b[locHead1 - 1] += 1
            c[locHead1 - 1] += 1
            return True
        else:
            b[locHead1 - 1] += 1
            b[locHead1] += 1
            return True
    elif locHead0.lower == c1.lower:
        if vert:
            c[locHead1 - 1] += 1
            d[locHead1 - 1] += 1
            return True
        else:
            c[locHead1 - 1] += 1
            c[locHead1] += 1
            return True
    elif locHead0.lower == d1.lower:
        if vert:
            d[locHead1 - 1] += 1
            e[locHead1 - 1] += 1
            return True
        else:
            d[locHead1 - 1] += 1
            d[locHead1] += 1
            return True
    elif locHead0.lower == e1.lower:
        e[locHead1 - 1] += 1
        e[locHead1] += 1
        return True
    else:
        print("Invalid tile name")
        return False
def create_3_tile_ship(a, b, c, d, e, vert, locHead0, locHead1, a1, b1, c1, d1, e1):
    if locHead0.lower == a1.lower:
        if vert:
            if a[locHead1 - 1] != 1 and b[locHead1 - 1] != 1 and c[locHead1 - 1] != 1:
                a[locHead1 - 1] += 1
                b[locHead1 - 1] += 1
                c[locHead1 - 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
        else:
            if a[locHead1 - 1] != 1 and a[locHead1] != 1 and a[locHead1 + 1] != 1:
                a[locHead1 - 1] += 1
                a[locHead1] += 1
                a[locHead1 + 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
    elif locHead0.lower == b1.lower:
        if vert:
            if b[locHead1 - 1] != 1 and c[locHead1 - 1] != 1 and d[locHead1 - 1] != 1:
                b[locHead1 - 1] += 1
                c[locHead1 - 1] += 1
                d[locHead1 - 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
        else:
            if b[locHead1 - 1] != 1 and b[locHead1] != 1 and b[locHead1 + 1] != 1:
                b[locHead1 - 1] += 1
                b[locHead1] += 1
                b[locHead1 + 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False

    elif locHead0.lower == c1.lower:
        if vert:
            if c[locHead1 - 1] != 1 and d[locHead1 - 1] != 1 and e[locHead1 - 1] != 1:
                c[locHead1 - 1] += 1
                d[locHead1 - 1] += 1
                e[locHead1 - 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
        else:
            if c[locHead1 - 1] != 1 and c[locHead1] != 1 and c[locHead1 + 1] != 1:
                c[locHead1 - 1] += 1
                c[locHead1] += 1
                c[locHead1 + 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False

    elif locHead0.lower == d1.lower:
        if d[locHead1 - 1] != 1 and d[locHead1] != 1 and d[locHead1 + 1] != 1:
            d[locHead1 - 1] += 1
            d[locHead1] += 1
            d[locHead1 + 1] += 1
            return True
        else:
            print("Overlaps with other ship!")
            return False

    elif locHead0.lower == e1.lower:
        if e[locHead1 - 1] != 1 and e[locHead1] != 1 and e[locHead1 + 1] != 1:
            e[locHead1 - 1] += 1
            e[locHead1] += 1
            e[locHead1 + 1] += 1
            return True
        else:
            print("Overlaps with other ship!")
            return False
    else:
        print("Invalid Input Try again")
        return False
def create_4_tile_ship(a, b, c, d, e, vert, locHead0, locHead1, a1, b1, c1, d1, e1):
    if locHead0.lower == a1.lower:
        if vert:
            if a[locHead1 - 1] != 1 and b[locHead1 - 1] != 1 and c[locHead1 - 1] != 1 and d[locHead1 - 1] != 1:
                a[locHead1 - 1] += 1
                b[locHead1 - 1] += 1
                c[locHead1 - 1] += 1
                d[locHead1 - 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
        else:
            if a[locHead1 - 1] != 1 and a[locHead1] != 1 and a[locHead1 + 1] != 1 and a[locHead1 + 2] != 1:
                a[locHead1 - 1] += 1
                a[locHead1] += 1
                a[locHead1 + 1] += 1
                a[locHead1 + 2] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False

    elif locHead0.lower == b1.lower:
        if vert:
            if b[locHead1 - 1] != 1 and c[locHead1 - 1] != 1 and d[locHead1 - 1] != 1 and e[locHead1 - 1] != 1:
                b[locHead1 - 1] += 1
                c[locHead1 - 1] += 1
                d[locHead1 - 1] += 1
                e[locHead1 - 1] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False
        else:
            if b[locHead1 - 1] != 1 and b[locHead1] != 1 and b[locHead1 + 1] != 1 and b[locHead1 + 2] != 1:
                b[locHead1 - 1] += 1
                b[locHead1] += 1
                b[locHead1 + 1] += 1
                b[locHead1 + 2] += 1
                return True
            else:
                print("Overlaps with other ship!")
                return False

    elif locHead0.lower == c1.lower:
        if c[locHead1 - 1] != 1 and c[locHead1] != 1 and c[locHead1 + 1] != 1 and c[locHead1 + 2] != 1:
            c[locHead1 - 1] += 1
            c[locHead1] += 1
            c[locHead1 + 1] += 1
            c[locHead1 + 2] += 1
            return True
        else:
            print("Overlaps with other ship!")
            return False

    elif locHead0.lower == d1.lower:
        if d[locHead1 - 1] != 1 and d[locHead1] != 1 and d[locHead1 + 1] != 1 and d[locHead1 + 2] != 1:
            d[locHead1 - 1] += 1
            d[locHead1] += 1
            d[locHead1 + 1] += 1
            d[locHead1 + 2] += 1
            return True
        else:
            print("Overlaps with other ship!")
            return False

    elif locHead0.lower == e1.lower:
        if e[locHead1 - 1] != 1 and e[locHead1] != 1 and e[locHead1 + 1] != 1 and e[locHead1 + 2] != 1:
            e[locHead1 - 1] += 1
            e[locHead1] += 1
            e[locHead1 + 1] += 1
            e[locHead1 + 2] += 1
            return True
        else:
            print("Overlaps with other ship!")
            return False
    else:
        print("Invalid Input Try again")
        return False



vert = False
NUMBER_LENGTH = 3
IP = "127.0.0.1"
port = 5678

a1 = 'a'
b1 = 'b'
c1 = 'c'
d1 = 'd'
e1 = 'e'
name = "2"
connected = False
looped = False
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while not connected:
    try:
        clientSocket.connect((IP, port))
        clientSocket.setblocking(False)
        connected = True
    except IOError as er:
        if not looped:
            print("Turn on the Server!")
            looped = True

clientName = name.encode("utf-8")
nameHeader = f"{len(clientName):<{NUMBER_LENGTH}}".encode("utf-8")
clientSocket.send(nameHeader + clientName)
a = [0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0, 0, 0, 0]
e = [0, 0, 0, 0, 0, 0, 0, 0]

enA = [0, 0, 0, 0, 0, 0, 0, 0]
enB = [0, 0, 0, 0, 0, 0, 0, 0]
enC = [0, 0, 0, 0, 0, 0, 0, 0]
enD = [0, 0, 0, 0, 0, 0, 0, 0]
enE = [0, 0, 0, 0, 0, 0, 0, 0]

print(f"Welcome Player {name}")
print("Layout of map: ")
print("    1  2  3  4  5  6  7  8")
print("A ", a)
print("B ", b)
print("C ", c)
print("D ", d)
print("E ", e)

while True:
    invalid = False
    lay = input(f"where do you want you first ships head? (example entry: 'A 3', whitespace sensitive) (2 spaces): ")
    tail = input("Would you like it vertical? (y for yes, else it will be horizontal,"
             " row E will always default horizontal) ")
    if tail.lower == 'y'.lower:
        vert = True
    locationHead = lay.split()
    try:
        locHead0 = str(locationHead[0])
        locHead1 = int(locationHead[1])
    except:
        print("Invalid Input")
        invalid = True
    if not invalid:
        if (locHead1 > 7 and not vert) or (locHead1 > 8) or (locHead0.lower() == e1.lower() and vert):
            print("Invalid tile in array index")
        else:
            a1 = 'a'
            b1 = 'b'
            c1 = 'c'
            d1 = 'd'
            e1 = 'e'
            valid = create_2_tile_ship(a, b, c, d, e, vert, locHead0, locHead1, a1, b1, c1, d1, e1)
            if valid:
                break
vert = False

while True:
    invalid = False
    lay = input(
        f"where do you want you second ships head? (example entry: 'A 3', whitespace sensitive) (3 spaces): ")
    tail = input("Would you like it vertical? (y for yes, else it will be horizontal, rows D and E will"
                 " always default horizontal) ")

    if tail.lower == 'y'.lower:
        vert = True

    locationHead = lay.split()
    try:
        locHead0 = str(locationHead[0])
        locHead1 = int(locationHead[1])
    except:
        print("Invalid Input")
        invalid = True

    if not invalid:
        if (locHead1 > 6 and not vert) or (locHead1 > 8) or ((locHead0.lower() == e1.lower() or locHead0.lower() ==
                d1.lower()) and vert):
            print("Invalid tile in array index")
        else:
            valid = create_3_tile_ship(a, b, c, d, e, vert, locHead0, locHead1, a1, b1, c1, d1, e1)
            if valid:
                break
vert = False

while True:
    invalid = False
    lay = input(
        f"where do you want you Third ships head? (example entry: 'A 3', whitespace sensitive) (4 spaces): ")
    tail = input("Would you like it verticle? (y for yes, else it will be horizontal, "
                 "rows C, D and E will always defualt horizontal) ")

    if tail.lower == 'y'.lower:
        vert = True

    locationHead = lay.split()

    try:
        locHead0 = str(locationHead[0])
        locHead1 = int(locationHead[1])
    except:
        print("Invalid Input")
        invalid = True
    if not invalid:
        if (locHead1 > 5 and not vert) or (locHead1 > 8) or ((locHead0.lower() == e1.lower() or
                locHead0.lower() == d1.lower() or locHead0 == c1.lower()) and vert):
            print("Invalid tile: outside available index (Ship is not on the map)")
        else:
            valid = create_4_tile_ship(a, b, c, d, e, vert, locHead0, locHead1, a1, b1, c1, d1, e1)
            if valid:
                break


print("A ", a, "    Opponents A ", enA)
print("B ", b, "    Opponents B ", enB)
print("C ", c, "    Opponents C ", enC)
print("D ", d, "    Opponents D ", enD)
print("E ", e, "    Opponents E ", enE)
isTurn = False
hasLost = False
hasWon = False
while not hasLost and not hasWon:
    if isTurn:
        message = input("Make a guess: ")
        message = check_valid(message, NUMBER_LENGTH)
        message = message.encode("utf-8")
        messageHeader = f"{len(message):<{NUMBER_LENGTH}}".encode("utf-8")
        clientSocket.send(messageHeader + message)
        while True:
            try:
                message2 = clientSocket.recv(NUMBER_LENGTH)
                message2 = message2.decode("utf-8")
                if message2:
                    if message2 == "HIT":
                        print(f"You're shot at '{message.decode('utf-8')}' hit an opposing ship!")
                    else:
                        print(f"You're shot at '{message.decode('utf-8')}' was shot into the ocean!")
                    modify_guess_map(message2, message.decode("utf-8"), enA, enB, enC, enD, enE)
                    break
            except IOError as er:
                continue

        print("A ", a, "    Opponents A ", enA)
        print("B ", b, "    Opponents B ", enB)
        print("C ", c, "    Opponents C ", enC)
        print("D ", d, "    Opponents D ", enD)
        print("E ", e, "    Opponents E ", enE)

        while True:
            try:
                message3 = clientSocket.recv(NUMBER_LENGTH)
                message3 = message3.decode("utf-8")
                if message3:
                    if message3 == "win":
                        hasWon = True
                        print_win_message()
                        break
                    else:
                        break
            except IOError as er:
                continue


        isTurn = False
    else:
        try:
            message1 = clientSocket.recv(NUMBER_LENGTH)
            message1 = message1.decode("utf-8")
            if message1:
                print(message1)

                guess = process_guess(message1, a, b, c, d, e)
                if guess == "HIT":
                    print(f"you have been hit at: {message1}!")
                else:
                    print(f"The shot at '{message1}' has missed!")
                guess = guess.encode("utf-8")
                guessHeader = f"{len(guess):<{NUMBER_LENGTH}}".encode("utf-8")
                clientSocket.send(guessHeader + guess)

                print("A ", a, "    Opponents A ", enA)
                print("B ", b, "    Opponents B ", enB)
                print("C ", c, "    Opponents C ", enC)
                print("D ", d, "    Opponents D ", enD)
                print("E ", e, "    Opponents E ", enE)

                hasLost = check_if_loss(a, b, c, d, e)
                if hasLost:
                    winMessage = "win"
                    winMessage = winMessage.encode("utf-8")
                    winMessageHeader = f"{len(winMessage):<{NUMBER_LENGTH}}".encode("utf-8")
                    clientSocket.send(winMessageHeader + winMessage)
                    print_loss_message()
                else:
                    winMessage = "not"
                    winMessage = winMessage.encode("utf-8")
                    winMessageHeader = f"{len(winMessage):<{NUMBER_LENGTH}}".encode("utf-8")
                    clientSocket.send(winMessageHeader + winMessage)
                isTurn = True
        except IOError as er:
            continue
counter = 0
while counter > 50000000000000000000000000000000000000000000000000000000000:
    ++counter               
