
from datetime import datetime  # Date and time Library handling functionality using the datetime class.
from validate_email_address import validate_email  # Library for email address validation.

option = ""  # This the main_english input for each option

# Get the current date and time.
now = datetime.now()

# Format the current date as "mm/dd/yy".
formatted_date = now.strftime("%m/%d/%y")
# Format the current time as "HH:MM:SS".
formatted_time = now.strftime("%H:%M:%S")


def main_english():
    # Here is the main_english function that runs the first time

    evc_code = input("Enter *770# to login \n")

    # This line below checks the validation of the evc_zone code

    if evc_code != "*770#":
        # If the user enters an invalid evc_zone, the user will be asked whether to repeat the evc zone again
        retry = input("Failed to enter the evc zone \n do you want to try again Y,for yes or N for No")

        if retry.lower() == 'y':
            # If the user enters yes, the function will start over again to ask him to enter the evc_zone
            main_english()

        else:

            print("Sorry, the operation failed due to the invalid message formate")

    else:
        # Here will be asked if he has an account or not

        option = input("Do you have  an  account already  Enter y for yes or n for no")

        if option.lower() == 'y':
            # If he has an account, he will be asked to enter his pin, and the pin will be read from the Pin.txt file

            with open('Pin', 'r') as file_pin:

                file = file_pin.read()

                pin = input("Enter your pin\n")

                if pin == file:
                    # If the pin is correct, it should display the main_english menu of evc

                    menu()

                else:
                    print("[EVCPLUS-] Password is Incorrect")
                    main_english()



        elif option.lower() == 'n':
            # If the user doesn't have an account, the function below will create an account for him
            userpin()


def userpin():
    # This function is used to create an account for the user.
    while True:
        pin = input("Create your account enter a pin\n")

        if pin.isdigit() and len(pin) == 4:  # Check the validation of the user's PIN
            hubi = input("Verify your Pin  \n")

            if hubi == pin:

                with open('Pin', 'w') as pin_data:
                    # File handling code: save the user's PIN in a file named 'Pin'
                    pin_data = pin_data.write(pin)

                    deposit_money = float(input("How much money you want to deposit in your account\n"))

                    print(f"[EVCPLUS] You recive  {deposit_money}$ date {formatted_date} {formatted_time} ")

                    deposit_money = str(deposit_money)

                    with open('Haraaga', 'w') as file:
                        # If the user chooses the amount of money to deposit, it will be stored in the 'Haraaga' file
                        file.write(deposit_money)
                # If the user completes the process of entering a PIN and depositing money, return to the main_english function
                main_english()

                break

            else:
                print("The pin does not match")
        else:
            print("Invalid PIN format. Please enter a 4-digit PIN consisting of only numbers.")


def menu():
    # This function is the main_english menu

    print("1:Balanace Query")
    print("2:E-Voucher")
    print("3: Bill Payment")
    print("4: Send Money ")
    print("5: Mini  Statement ")
    print("6: Salaam Bank")
    print("7: Manage Account")
    print("8: Bill Payment")
    option = int(input())
    if option == 1:
        Haraaga()
    elif option == 2:
        kaarka_hadlka()
    elif option == 3:
        bixi_biilka()
    elif option == 4:
        Uwareeji_EVC()
    elif option == 5:
        Warbixin_Kooban()
    elif option == 6:
        salam_bank()
    elif option == 7:
        maaraynta()
    elif option == 8:
        bill_pay()
    else:
        print("please choose an option")
        main_english()



def Haraaga():
    with open('Haraaga', 'r') as file:
        Haraaga = file.read()
        print(
            f"Your current balance is : {Haraaga}$")  # The Haraaga is not is a string so you need to make it int to use it
        main_english()


def kaarka_hadlka():
    # qeebta koobad kaarka hadalka
    print('E-Voucher')
    print('1.Self Airtime')
    print('2.Friend  Airtime')
    print('3.MIFI Packages')
    print('4.Self Data Recharge')
    print('5.InternNetwork Airtime')
    dookh = int(input(""))  # dookhan waxan u qaatay inaa ku kala doorto lanbarada kore
    if dookh == 1:
        ku_shubo_aritime()
    elif dookh == 2:
        ugu_shub_airtime()
    elif dookh == 3:
        mifi_packages()
    elif dookh == 4:
        ku_shubo_internet()
    elif dookh == 5:
        ugu_shub_airtime()
    else:
        print("Choose a number")
        kaarka_hadlka()


def ku_shubo_aritime():
    # This line of code below reads the balance or "haraaga" from a file.
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read()) # This line changes the "haraaga" read from a file into a float so we can use it


    lacag = float(input("Please enter the money"))

    if lacag > Haraaga:

        print("Your balance is not enough")

    elif lacag <= Haraaga:
        dookh1 = int(input(f"Confirm Recharge of  ${lacag} to undefined? \n" "1.YES \n 2.NO"))

        if dookh1 == 1:
            Haraaga -= lacag
            # This line below changes the "haraaga" that was used into a str so we can save it into a file
            Haraaga = str(Haraaga)
            with open('Haraaga', 'w') as file:
                file.write(Haraaga) # This line saves the changed value of "haraaga" into a file
            print(
                f"[-evcplus-] You ${lacag} DEPOSIT INTO  (SENDER_MOBILE_NO),Tar- {formatted_date, formatted_time},\nYour balanace is  ${Haraaga}")
            main_english()
        else:
            print("Bye")


def ugu_shub_airtime():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())# This line changes the "haraaga" read from a file into a float so we can use it

    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Please enter the mobile \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # Change the "recipt_num" into str so we can make validation on it
    money = float(input("Please enter the money \n"))

    confirm = int(input(f"Confirm  ${money} to Send {recipt_num} \n"
                        f"1.YES\n"
                        f"2.NO\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraage = str(Haraage)
                print(
                    f"[-EVCPlus-] ${money}You transferred to  {recipt_num}, date: {formatted_date} {formatted_time}, Your balance is ${Haraage}."
                    f"Download  App -  WAAFI")

                    # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main_english()
            else:
                print("Your account balance is insufficient")
        else:
            print("invalid number formate ")
            main_english()
    elif confirm ==2:
        print("Bye")
        main_english()
    else:
        print("choose a number ")
        main_english()


def mifi_packages():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = int(haraaga_file.read())

    print("EVCPlus \n" "1.MIFI data Recharge ")
    doorasho3 = int(input())

    if doorasho3 == 1:  # doorashan3 waxan u sameeye inaa data mifi ku wacdo
        print("--Internet Bundle Recharge-- \n" "1. Isbuucle(Weekly)\n2.Maalinle(Daily) \n3. Bile(MiFi)")
        doorasho4 = int(input(""))  # doorasho4 kana waxaan u sameye 3 lanbar kore ka wacdo

        if doorasho4 == 1:
            print("Please  select a  bundle  \n" "1.$5 = 10 GB \n2.$10 = 25 GB ")
            main_english()

        elif doorasho4 == 2:
            print("Please Select a  bundle \n" "1.$1 = 2 GB \n2.$2 = 5 GB")
            main_english()

        elif doorasho4 == 3:
            print("Please Select a  bundle \n" "1.$20 = 40 GB \n2.$40 = 85 GB \n3.$60 = 150 GB \n4.$30 = Monthly Unlimit")
            main_english()
        else:
            print("choose a number ")
            main_english()
    else:
        print("Fadlan dooro number sax ahaa")
        main_english()


def ku_shubo_internet():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())

    print("Please select a number to top up \n"
          "1. Isbuucle(Weekly) \n"
          "2. TIME BASED PACKAGES \n"
          "3. DATA \n"
          "4. Maalinle(Daily) \n"
          "5. Bile (MIFI)")

    doorasho4 = int(input())

    dookh1 = 0  # Provide a default value for dookh1

    if doorasho4 in [1, 2, 3, 4, 5]:
        # Prompt the user to enter the amount for internet usage.
        lacag = float(input("Please enter the money "))

        if lacag > Haraaga:
            # Display a message for insufficient balance.
            print("Your account balance is insufficient \n" "No: (SENDER_MOBILE_NO)")

        elif lacag <= Haraaga:
            # Prompt the user to confirm the internet usage.
            dookh1 = int(input(f"Are you sure you want to deposit ${lacag} into undefined? \n" "1.YES \n 2.NO"))

            if dookh1 == 1:
                # Update the balance after successful internet usage.
                Haraaga -= lacag
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraaga = str(Haraaga)
                # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraaga)

                # Display a success message for internet usage.
                print(f"[-evcplus-] You deposit ${lacag} into  [SENDER_MOBILE_NO], date- {formatted_date}{formatted_time},\n"
                      f"your balance  is  ${Haraaga}")
                main_english()

            else:
                # Display a cancellation message.
                print("bye")
                main_english()



    else:
        # Display a message for choosing an invalid option.
        print("choose a number ")
        main_english()



def ugu_shub_qof_kale_MMT():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())
    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Please enter a number  \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # Change the "recipt_num" into str so we can make validation on it
    money = float(input("Please enter the amount of money  \n"))

    confirm = int(input(f"Confirm ${money} send to {recipt_num} \n"
                        f"1.YES\n"
                        f"2.NO\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraage = str(Haraage)
                print(
                    f"[-EVCPlus-] ${money} You transferred {recipt_num}, Date: {formatted_date} {formatted_time}, Your balance is  ${Haraage}."
                    f"Download -  WAAFI")
                # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main_english()
            else:
                print("Your account balance is insufficient")
                main_english()
        else:
            print("Invalid number format ")
            main_english()
    else:
        print("bye")
        main_english()


def bixi_biilka():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as file:
        Haraaga = file.read()
    Haraaga = float(Haraaga) # This line changes the "haraaga" read from a file into a float so we can use it

    print('Bixi Biil')
    print('1.Post Paid')
    print('2.Pay Bill')
    dookh = int(input())

    if dookh == 1:
        print('1.Query Bill Payment')
        print('2.Pay Post Paid Bill')
        print('3.Pay Friend Post Paid Bill')
        doorasho = int(input())

        if doorasho == 1:
            print('error occurred, please try again later')
            main_english()
        elif doorasho == 2:
            lacag = float(input("Please enter the amount money : "))

            if lacag <= Haraaga:
                doorasho2 = int(input(f'Are you sure you want to pay a bill that costs: $ {lacag} \n1. YES \n2. NO\n'))

                if doorasho2 == 1:
                    print('error occurred, please try again later')
                    main_english()

                else:
                    print("Bye.")
                    main_english()
            else:
                print("Your account balance is insufficient")
                main_english()
        elif doorasho == 3:
            number = int(input("Please enter a number : "))
            lacag = float(input("please enter the amount of money : "))
            number = str(number) # We convert the number to a string for validation purposes

            if len(number) == 9 and number.startswith('61') or number.startswith("77"):
                if lacag <= Haraaga:
                    doorasho3 = int(
                        input(f'Are you sure you want to pay a bill that costs: $ {lacag} \n1. YES \n2. NO'))
                    if doorasho3 == 1:
                        print('error occurred, please try again later')
                        main_english()
                    else:
                        print("Mahadsanid.")
                        main_english()
                else:
                    print("Your account balance is insufficient")
                    main_english()
            else:
                print("Inavalid number formate ")
                main_english()
        else:
            print("choose a number ")
            main_english()
    elif dookh == 2:
        Marchent=input("Please enter  marchent id ")
        print("sorry")
        main_english()
    else:
        print("choose a number ")
        main_english()



def Uwareeji_EVC():
    # This function is used for money transfer

    # Read the current balance from the 'Haraaga' file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())


    # This loop will remain_english running until the user enters a valid number
    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Please enter the mobile \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # We convert the "recipt_num" to a string for validation purposes
    money = float(input("Please enter the money \n"))

    confirm = int(input(f"Confirm ${money} send to  {recipt_num} \n"
                        f"1.YES\n"
                        f"2.NO\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # Convert the "haraaga" value to a string before saving it to a file
                Haraage = str(Haraage)
                print(f"[-EVCPlus-] You have successfully transferred ${money} to {recipt_num} at {formatted_date} {formatted_time}, Your Balance is ${Haraage}.")
                trans = (
                    f"\n[-EVCPlus-] You have successfully transferred ${money} to {recipt_num} at {formatted_date} {formatted_time}, Your Balance is ${Haraage}.")
                # Save the transaction information to a file named "trans.txt"
                with open('trans.txt', 'a') as file:
                    file.write(trans)
                    # Save the updated "haraaga" value to a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main_english()
            else:
                print("Your account balance is insufficient")
                main_english()
        else:
            print("Invalid number format ")
            # Recursive call to restart the function if there's an invalid number
            Uwareeji_EVC()
    else:
        print("Bye")
        main_english()


def last_action():
    try:
        # This line of code reads the last transaction from a file
        with open("trans.txt", "r") as file:
            lines = file.readlines()
            print(lines[-1])
            main_english()
            # If the file was not found, display the message below
    except FileNotFoundError:
        print("That file does not found :(")


def last_3action():
    # Open the "trans.txt" file in read mode
    with open("trans.txt", 'r') as file:
        # Read all lines from the file
        last = file.readlines()
        # Extract the last three lines from the list of all lines
        last_three_lines = last[-3:]
        # Print each of the last three transactions
        for line in last_three_lines:
            print(line)
            # Call the main_english function when you finish.
        main_english()


def Wareejint_dambesay():
    # Open the "trans.txt" file in read mode and read all lines.
    with open('trans.txt', 'r') as file:
        line = file.readlines()

    # Prompt the user to input a mobile number and convert it to a string
    recipt_num = int(input("Please enter a number  "))
    recipt_num = str(recipt_num)

    # Check if the entered mobile number is valid
    if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")):
        # Iterate through each line in the file
        for num in line:
            # Check if the entered mobile number is present in any transaction line
            if recipt_num in num:
                print(num)
                # Call the main_english function
                main_english()
            else:
                print("Operation succeeded. No transactions to display!")
                # Call the main_english function
                main_english()
    else:
        print("Invalid number formate ")
        Wareejint_dambesay()


def Warbixin_Kooban():
    # This function displays a menu of transaction options for the user

    # Display menu options for the user to choose from.
    print("Mini Statement")
    print("1. Last Action")
    print("2. Last Transfer ")
    print("3. Last Payment ")
    print("4. Last 3 Transactions")
    print("5. Email Me My Activity")

    option = int(input())  # Prompt the user to enter their choice

    if option == 1:
        last_action()  # Call the last_action function

    elif option == 2:
        print("Statement of :")
        print("1. Sent ")
        print("2. Recieved")
        option = int(input())

        if option == 1:
            Wareejint_dambesay()  # Call the Wareejint_dambesay function

        elif option == 2:
            recipt_num = input("Please enter a number  ")

            if len(recipt_num) == 9 and recipt_num.startswith("61"):
                print("Operation succeeded. No Transactions to display!")
                main_english()

            else:
                print("Error: Please enter a 9-digit number starting with '61'")
                Warbixin_Kooban()
        else:
            print("choose a number ")
            main_english()

    elif option == 3:
        Aqoonsi = input("Please enter Merchant ID \n")
        print("Operation succeeded. No Transactions to display!")
        main_english()

    elif option == 4:
        last_3action()  # Call the last_3action function

    elif option == 5:
        Email = input("Please enter your email  \n ")
        is_valid = validate_email(Email, verify=True)  # Check the validation of the email

        if is_valid:
            # If the email is valid, prompt the user to enter the duration of the activity
            date_hore = input("Please Enter the previous date (DAY/MONTH/YEAR, e.g: 05/07/2017)\n")
            date_danbe = input("Please Enter the next date (DAY/MONTH/YEAR, eg: 16/10/2017)\n")

            try:
                # Check the validation of the date. If correct, an email will be sent
                now.strptime(date_hore, '%d/%m/%Y')
                now.strptime(date_danbe, '%d/%m/%Y')
                print(f"Your email is being processed, and the activity will be emailed to {Email}")
                main_english()

            except ValueError:
                # If the user enters an invalid date, print an invalid date message
                print("Invalid Date format")
                main_english()

        else:
            # If the email is not correct, print the message below
            print("The email you provided is not valid ")
            Warbixin_Kooban()
    else:
        print("Please choose a correct a number ")
        main_english()



def salam_bank():
    # Prompt the user to choose an option for EVC Plus transaction
    option = int(input("1. Transfer from EVC Plus"))

    if option == 1:
        # Prompt the user to select a bank for the transaction
        print("Please choose Bank Account ")
        print("1. Bank Beeraha")
        print("2. Salaam Sch")
        print("3. SALAAM SOMALI BANK")
        print("4. Darasalaam Bank")
        option = int(input())

        if option in [1, 2, 3, 4]:
            # Get account information and transaction details
            accountga = input("Please Enter benficiary account: ")
            macluumad = input("Please comment: ")
            lacagta = float(input("Please enter the money: "))
            print("There is no account number linked to the phone")
            main_english()

        else:
            print("Fadlan dooro number sax ah ")
            salam_bank()

    else:
        print("Fadlan dooro number sax ah ")
        main_english()



def maaraynta():
    # Display the options available for MAAREYNTA
    print("Manage Account ")
    print("1: Chnage PIN")
    print("2: Change Language")
    print("3: Report Lost")
    print("4: Block Transaction")
    print("5: Return Tranasction")
    print("6:Enable Mobile Banking")

    choice = int(input("")) # Prompt the user to enter their choice

    # Execute the corresponding function based on the user's choice
    if choice == 1:
        bedel_pin()
    elif choice == 2:
        luqada()
    elif choice == 3:
        mobile_lumay()
    elif choice == 4:
        lacag_xirsho()
    elif choice == 5:
        lacag_qaladantay()
    elif choice == 6:
        mobile_bank()
    else:
        print("Fadlan dooro number sax ah ")
        main_english()


def bedel_pin():
    # Prompt the user to enter a new PIN
    pin = int(input("Enter Your new Pin"))

    # Prompt the user to confirm the new PIN
    hubi = int(input("Confirm your new Pin"))
    if (pin == hubi):
        # Display a success message and save the new PIN to a file
        print("<-EVCPlus-> You have successfully changed your   PIN-\n")
        pin = str(pin)
        with open('Pin', 'w') as file:
            bedel = file.write(pin)

        main_english()
    else:
        # Display an error message for PIN mismatch and prompt the user to try again
        print("Input Mismatch Plz try again Later:")
        bedel_pin()


def luqada():
    from Somali import somali_main
    # Prompt the user to choose a language
    print("Choose Language:")
    print("1. Somali")
    print("2. English")

    lang = int(input(""))

    if lang == 1:
        # Display a success message for changing the language to Somali
        print("[EVCPlus] waad ku guulaysatay in aad badasho Luqadda")
        somali_main()
    if lang == 2:
        # Display a success message for changing the language to English
        print("[-EVCPlus]You have successfully changed your language")
        main_english()



def mobile_lumay():
    # Prompt the user to enter the mobile number
    num = int(input("Enter the number mobile lost :  "))
    num = str(num)

    # Check if the entered mobile number is valid
    if len(num) == 9 and num.startswith("61") or num.startswith("77"):
        # Prompt the user to enter their PIN for confirmation
        pin = int(input("Enter your Pin:  "))
        print(f"Confirm to register the lost mobile number {num}?")
        print("1:YES\n")
        print("2:NO\n")

        # Ask the user for confirmation
        check = int(input())

        # Read the PIN from the file.
        with open('Pin', 'r') as pin_file:
            pinka = int(pin_file.read())


        if pin == pinka:
            if check == 1:
                print("You have successfully registerd  Thanks  ")
                main_english()
            else:
                print("Thanks!")
                main_english()
        else:
            print("[EVCPLUS-] Your pin is incorrect")
            main_english()

    else:
        print("invalid number format")
        main_english()


def lacag_xirsho():
    # Prompt the user to enter the incorrect transaction number
    mistake = int(input("Please enter the mistaken number "))

    # Prompt the user to enter the correct transaction number
    corct = int(input("Please enter the intended number"))

    # Prompt the user to enter additional information (macluumaad)
    maclumad = input("Please comment ")

    # Ask the user if they confirm the transaction
    print("Confirm to block the transaction")
    print("1:YES")
    print("2:NO")
    check = int(input(""))


    if check == 1:
        # Display a success message for completing the transaction
        print("The transaction was blocked thanks ")
        main_english()
    elif check == 2:
        # Display a message  cancellation
        print("Thanks!")
        main_english()
    else:# if he choose another option
        print("Thanks!")
        main_english()


def lacag_qaladantay():
    enter = input("Fadlan Geli aqoonsiga lacag dirida")
    print("Invalid input format")
    main_english()


def mobile_bank():
    check = int(input("Please enter Transferld"))
    print("Activiation Record not found")
    main_english()


def bill_pay():
    # Display options for bill payment
    print("EVC_PLUS")
    print("1.Query Bill info")
    print("2. Full Bill Payment ")
    print("3. Partial Bill Payment")

    # Prompt the user to choose an option
    option = int(input())

    if option in [1, 2, 3]:
        # Prompt the user to enter the bill reference number
        reference_num = input("please enter bill reference no\n")

        # Display a message indicating  errors
        print("Some parameters are missing, please check your request")
        main_english()

    else:
        # Display a message for choosing an invalid option
        print("Fadlan dooro number sax ah ")
        main_english()


