from pynput import keyboard

def log_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter=="Key.up" or letter=="Key.right" or letter=="Key.down" or letter=="Key.left":
        with open("log.txt","a") as f:
            f.write(letter)
            f.write("\n")
            return False

aux = True
while aux==True:
    with keyboard.Listener(on_press=log_to_file) as listener:
        listener.join()