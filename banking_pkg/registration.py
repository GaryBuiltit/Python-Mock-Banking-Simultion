
def register_name():
    while True:
        name = input("Enter name to register: ")
        if len(name) < 1:
            print("You must enter a name")
            continue
        elif len(name) > 10:
            print("Maximum name length is 10 characters")
            continue
        else:
            break
    return name


def register_pin():
    while True:
        pin = input("Enter PIN: ")
        if len(pin) != 4:
            print("Pin must be 4 numbers")
            continue
        else:
            break
    return pin
