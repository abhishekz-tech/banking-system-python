# ==========================================
# Python Banking System Project
# ==========================================

balance = 1000


# Function to check balance
def check_balance():
    print(f"\nYour current balance is: ₹{balance}\n")


# Function to deposit money
def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid deposit amount!\n")
    else:
        balance += amount
        print(f"₹{amount} deposited successfully!\n")


# Function to withdraw money
def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > balance:
        print("Insufficient balance!\n")

    elif amount <= 0:
        print("Invalid withdrawal amount!\n")

    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully!\n")


# Main Program
while True:

    print("====== Python Banking System ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid choice! Please try again.\n")