

# gives user current balance
def show_balance(balance):
    print(f"Your current balance: {balance}")


# deposits money and updates the account
def deposit(balance):
    amount = float(input("Enter amount to deposit: \n"))
    return float(balance) + amount


# withdraws money and updates account
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: \n"))
    if amount > balance:
        print("Insufficient funds!")
        return float(balance)
    else:
        return float(balance) - amount


# loggs out of account
def log_out(name):
    print(f"Goodbye {name}!")
