exit = True
inserted = False
balance = 20000
actual_pin = None
blocked = False
attempt = 0
while True:
    if not inserted:
        print('Welcome to SBI')
        print('Enter Your ATM Card')
        x=int(input("1 for yes, 2 for no :"))
        if x==1:
            inserted = True
            if blocked:
                print('Your ATM card has been Blocked. \n Contact your Branch Manager to unblock')
                inserted = False
                continue
            if not actual_pin :
                actual_pin = int(input("Set Your PIN :"))
            print("Enter the PIN")
            pin = int(input())
            if pin == actual_pin:
                print(

                    """
        1. Deposit
        2. Withdrawal
        3. Mini Statement
        4. PIN change

        """
                )
                option=int(input("Select one of the options above"))
                if option == 1:
                    print("Deposit")
                    amount = int(input("Enter the amount :"))
                    if amount % 100 == 0:
                        balance += amount
                        print("Cash has been Accepted")
                        print("Available Balance = ",balance)
                    else:
                        print("Feed only multiples of hundred")
                if option == 2:
                    print("Withdrawal")
                    amount = int(input("Enter the amount :"))
                    if amount<balance:
                        if amount % 100 == 0:
                            balance -= amount
                            print("Take the Cash")
                            print("Available Balance = ",balance)
                        else:
                            print("Enter only multiples of hundred")
                    else:
                        print("Insufficient Balance")
                if option == 4:
                    actual_pin = int(input("Enter New PIN"))

            else:
                print("Invalid PIN")
                attempt+=1
                if attempt >=2:
                    blocked = True
    else:
        inserted = False
