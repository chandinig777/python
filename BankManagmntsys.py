
print("="*20)

customerNames = ['princy','tinu','yuvan','ashy','willy']
customerPins = ['1214','0918','0609','1016','5452']
customerBalances = [100000,90000,80000,70000,50000]
deposition = 0
withdraw = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0
# this statement helps to run program continously.

while True:
    #os.system("cls")
    print("=======================================")
    print("----Welcome to HDFC Bank----           ")
    print("***************************************")
    print("=<< 1. Open a new account           >>=")
    print("=<< 2. Withdraw money               >>=")
    print("=<< 3. Deposit money                >>=")
    print("=<< 4. Check Customers and Balance  >>=")
    print("=<< 5. Exit/Quit                    >>=")
    print("***************************************") 

    # This below statement takes the choice number from the user
    choiceNumber = input("Select your choiceNumber from the above menu")
    if choiceNumber == "1":
        print("choiceNumber 1 is selected by the customer")
        #the below line will take the num of customers from the user'
        NOC = eval(input("Number of customers:"))

        i = i + NOC
        # The if condition will restrict the number of new account to 5
        if i > 5:
            print("/n")
            print("customer registration exceed reached or customer registration too low")
            i = i - NOC
        else:
            # The while loop vll run according to the  num of customer
            while counter_1 <= i:
                # These few lines will take information from customer
                name = input("Input FullName :")
                customerNames.append(name)
                pin = str(input("please input a pin of ur choice:"))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value:"))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=",end=" ")
                print(customerNames[counter_2])
                print("Pin=",end=" ")
                print(customerPins[counter_2])
                print("Balance=",end=" ")
                print(customerBalances[counter_2], end=" ")  
                print("/-Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("/nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("-----New account created successfully  !------")
                print("/n")
                print("Your name is availabile int the customers list now : ")
                print(customerNames)
                print("/n")
                print("Note! Please remember the Name and Pin")
                print("===========================================")
        # This statement below helps the user to go back to start the program (main menu)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        # This while loop vll prevent the user using the account if the username or pin is incorrect 
        while j < 1:
            k = -1
            name = input("Please enter name:")
            pin = input("Please enter pin:")
            # This while loop will keep the function running when variable k is less than length of the customers list
            while k < len(customerNames) - 1:
                k = k + 1
                #These two if conditions find where both the name and pin matches
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j+1
                        # These two statements show the balance taken from the list
                        print("Your current balance:", end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        # below statement would take the amt to withdraw from the user
                        withdrawal = eval(input("input value to withdraw: "))
                        # if condition below would look wheater the withdraw is greater than the balance
                        if withdrawal > balance:
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input("Please Deposit a higher Value because mentioned above is not enough : "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:",end=" ")
                            print(balance, end=" ")
                            print("-/nRs\n") #  1000 - 500= 500
                            balance = balance - withdrawal
                            print("-/n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ",balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is 
                            # greater than the withdraw amount
                            balance = balance - withdrawal
                            # These few statements would update the values in the list and show it to the customer
                            print("\n")
                            print("----Withdraw Successfull!---")
                            customerBalances[k] = balance
                            print("Your New Balance: ",balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                # the if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n") 
                break
            # This statement below helps the user to go back to start the program(main menu)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        # while loop vll work when the pin or the user name is wrong
        while n < 1:
            k = -1
            name = input("Please input name: ")
            pin = input("Please input pin: ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(customerNames) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name are correct
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        # These statement below would show the customer balance and update list values according
                        # to the deposition made
                        print("Your Current Balance: ",end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        # This statement below takes the deposition from the customer.
                        deposition = eval(input("Enter the value you want to deposit: "))
                        balance = balance + deposition  #1000+500=1500
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition Successfull!----")
                        print("your new balance: ",balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to start the program(main menu)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below: ")
        print("\n")
        # This while loop below will keep running untill all the customers and balances are shown
        while k <= len(customerNames) -1:
            print("->/customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
                # This statement below helps the user to go back to start the program(main menu)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "5":
        # This statements would just showed to the customer
        print("Choice number 5 is selected by the customer")
        print("Thankyou for using our Banking System!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
         # This statement below helps the user to go back to start the program(main menu)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")





















                        







