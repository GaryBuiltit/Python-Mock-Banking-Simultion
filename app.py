from banking_pkg import account
from banking_pkg import registration


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")


# User registration
while True:
    name = registration.register_name()
    pin = registration.register_pin()
    balance = 0
    print(f"{name} as been registered with a starting balance of ${balance}\n")
    break

# Login and credential verification
while True:
    print("Login")
    typedName = input("Enter Name: ")
    typedPin = input("Enter Pin: ")
    if typedName.lower() == name.lower() and typedPin == pin:
        print("Login successful\n")
        break
    else:
        print("Invalid credentials\n")
        continue


# account services
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        print(f"Your current balance: {balance}")
    elif option == "3":
        balance = account.withdraw(balance)
        print(f"Your current balance: {balance}")
    elif option == "4":
        account.log_out(name)
        break
    else:
        print("Please choose a valid option.")
