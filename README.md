from English import main_english # from english import  *# take look here again
from datetime import datetime  # Date and time Library handling functionality using the datetime class.
from validate_email_address import validate_email  # Library for email address validation.

option = ""  # This the main input for each option

# Get the current date and time.
now = datetime.now()

# Format the current date as "mm/dd/yy".
formatted_date = now.strftime("%m/%d/%y")
# Format the current time as "HH:MM:SS".
formatted_time = now.strftime("%H:%M:%S")


def main():
    # Here is the main function that runs the first time

    evc_code = input("gali *770# si aad u gashid  gudaha ")

    # This line below checks the validation of the evc_zone code

    if evc_code != "*770#":
        # If the user enters an invalid evc_zone, the user will be asked whether to repeat the evc zone again
        retry = input("Failed to enter the evc zone \n do you want to try again Y,for yes or N for No")

        if retry.lower() == 'y':
            # If the user enters yes, the function will start over again to ask him to enter the evc_zone
            main()

        else:

            print("Sorry, the operation failed due to the invalid message formate")

    else:
        # Here will be asked if he has an account or not

        option = input("account hore miyaa leedahay Enter y for haa or n for no ")

        if option.lower() == 'y':
            # If he has an account, he will be asked to enter his pin, and the pin will be read from the Pin.txt file

            with open('Pin', 'r') as file_pin:

                file = file_pin.read()

                pin = input("Enter your pin\n")

                if pin == file:
                    # If the pin is correct, it should display the main menu of evc

                    menu()

                else:
                    print("[EVCPLUS-] Nambarka Sirta ah waa Khalad ")
                    main()



        elif option.lower() == 'n':
            # If the user doesn't have an account, the function below will create an account for him
            userpin()


def userpin():
    # This function is used to create an account for the user.
    while True:
        pin = input("Samee akoonkaaga  soo geli pin\n")

        if pin.isdigit() and len(pin) == 4:  # Check the validation of the user's PIN
            hubi = input("Hubi Pinkaaga \n")

            if hubi == pin:

                with open('Pin', 'w') as pin_data:
                    # File handling code: save the user's PIN in a file named 'Pin'
                    pin_data = pin_data.write(pin)

                    deposit_money = float(input("Meeqo  lacag ayaad rabtaa inaad  ku shubto akoonkaaga\n"))

                    print(f"[EVCPLUS] Waxaad heshay {deposit_money}$ Tarikhaad {formatted_date} {formatted_time} ")

                    deposit_money = str(deposit_money)

                    with open('Haraaga', 'w') as file:
                        # If the user chooses the amount of money to deposit, it will be stored in the 'Haraaga' file
                        file.write(deposit_money)
                # If the user completes the process of entering a PIN and depositing money, return to the main function
                main()

                break

            else:
                print("the pin doesnot match")
        else:
            print("Invalid PIN format. Please enter a 4-digit PIN consisting of only numbers.")


def menu():
    # This function is the main menu

    print("1: Itus Haraaga")
    print("2: Kaarka Hadalka")
    print("3: Bixi Biil")
    print("4: Uwareeji EVCPlus")
    print("5: Warbixin Kooban")
    print("6: Salaam Bank")
    print("7: Mareeynta")
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
        print("Fadlan dooro number sax ahaa")
        main()



def Haraaga():
    with open('Haraaga', 'r') as file:
        Haraaga = file.read()
        print(
            f"Haraaga Xisaabtaadu waa: {Haraaga}$")  # The Haraaga is not is a string so you need to make it int to use it
        main()


def kaarka_hadlka():
    # qeebta koobad kaarka hadalka
    print('Kaarka hadalka')
    print('1.Ku shubo Airtime')
    print('2.Ugu shub Airtime')
    print('3.MIFI Packages')
    print('4.Ku shubo Internet')
    print('5.Ugu shub qof kale (MMT)')
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


    lacag = float(input("Fadlan geli lacagta "))

    if lacag > Haraaga:

        print("Haragaaga kuguma filna")

    elif lacag <= Haraaga:
        dookh1 = int(input(f"Ma hubtaa inaad ${lacag} ugu shubtid undefined? \n" "1.Haa \n 2.maya"))

        if dookh1 == 1:
            Haraaga -= lacag
            # This line below changes the "haraaga" that was used into a str so we can save it into a file
            Haraaga = str(Haraaga)
            with open('Haraaga', 'w') as file:
                file.write(Haraaga) # This line saves the changed value of "haraaga" into a file
            print(
                f"[-evcplus-] Waxaad ${lacag} ugu shubtay (SENDER_MOBILE_NO),Tar- {formatted_date, formatted_time},\nHaragaaga waa ${Haraaga}")
            main()
        else:
            print("Macsalama")


def ugu_shub_airtime():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())# This line changes the "haraaga" read from a file into a float so we can use it

    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Fadlan geli mobile-ka \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # Change the "recipt_num" into str so we can make validation on it
    money = float(input("Fadlan geli lacagta \n"))

    confirm = int(input(f"Ma hubtaa inaad ${money} u wareejisid {recipt_num} \n"
                        f"1.Haa\n"
                        f"2.Maya\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraage = str(Haraage)
                print(
                    f"[-EVCPlus-] ${money} ayaad uwareejisay {recipt_num}, Tar: {formatted_date} {formatted_time}, Haraagaagu waa ${Haraage}."
                    f"La soo deg App - ka WAAFI")

                    # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main()


def mifi_packages():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = int(haraaga_file.read())

    print("EVCPlus \n" "1.Ku shubo Data-da MIFI")
    doorasho3 = int(input())

    if doorasho3 == 1:  # doorashan3 waxan u sameeye inaa data mifi ku wacdo
        print("--Internet Bundle Recharge-- \n" "1. Isbuucle(Weekly)\n2.Maalinle(Daily) \n3. Bile(MiFi)")
        doorasho4 = int(input(""))  # doorasho4 kana waxaan u sameye 3 lanbar kore ka wacdo

        if doorasho4 == 1:
            print("Fadlan dooro bundle Ka \n" "1.$5 = 10 GB \n2.$10 = 25 GB ")

        elif doorasho4 == 2:
            print("Fadlan dooro bundle Ka \n" "1.$1 = 2 GB \n2.$2 = 5 GB")

        elif doorasho4 == 3:
            print(
                "Fadlan dooro bundle ka \n" "1.$20 = 40 GB \n2.$40 = 85 GB \n3.$60 = 150 GB \n4.$30 = Monthly Unlimit")

def ku_shubo_internet():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())

    print("Fadlan dooro number-Ka Ku shubeyso \n"
          "1. Isbuucle(Weekly) \n"
          "2. TIME BASED PACKAGES \n"
          "3. DATA \n"
          "4. Maalinle(Daily) \n"
          "5. Bile (MIFI)")

    doorasho4 = int(input())

    dookh1 = 0  # Provide a default value for dookh1

    if doorasho4 in [1, 2, 3, 4, 5]:
        # Prompt the user to enter the amount for internet usage.
        lacag = float(input("Fadlan geli lacagta "))

        if lacag > Haraaga:
            # Display a message for insufficient balance.
            print("haragaaga xisaabta kuguma filna, mobile /n" "No: (SENDER_MOBILE_NO)")

        elif lacag <= Haraaga:
            # Prompt the user to confirm the internet usage.
            dookh1 = int(input(f"Ma hubtaa inaad ${lacag} ugu shubtid undefined? \n" "1.Haa \n 2.maya"))

            if dookh1 == 1:
                # Update the balance after successful internet usage.
                Haraaga -= lacag
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraaga = str(Haraaga)
                # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraaga)

                # Display a success message for internet usage.
                print(f"[-evcplus-] Waxaad ${lacag} ku shubtid [SENDER_MOBILE_NO], Tar- {formatted_date}{formatted_time},\n"
                      f"Haragaaga waa ${Haraaga}")
                main()

            else:
                # Display a cancellation message.
                print("Macsalama")

    else:
        # Display a message for choosing an invalid option.
        print("Fadlan dooro number sax ah ")
        main()



def ugu_shub_qof_kale_MMT():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())
    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Fadlan geli mobile-ka \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # Change the "recipt_num" into str so we can make validation on it
    money = float(input("Fadlan geli lacagta \n"))

    confirm = int(input(f"Ma hubtaa inaad ${money} u wareejisid {recipt_num} \n"
                        f"1.Haa\n"
                        f"2.Maya\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # This line below changes the "haraaga" that was used into a str so we can save it into a file
                Haraage = str(Haraage)
                print(
                    f"[-EVCPlus-] ${money} ayaad uwareejisay {recipt_num}, Tar: {formatted_date} {formatted_time}, Haraagaagu waa ${Haraage}."
                    f"La soo deg App - ka WAAFI")
                # This line saves the changed value of "haraaga" into a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main()
            else:
                print("Haraaga kugama filnaa")
        else:
            print("Invalid number format ")


def bixi_biilka():
    # This line of code below reads the balance or "haraaga" from a file
    with open('Haraaga', 'r') as file:
        Haraaga = file.read()
    Haraaga = float(Haraaga) # This line changes the "haraaga" read from a file into a float so we can use it

    print('Bixi Biil')
    print('1.Post Paid')
    print('2.Ku Iibso')
    dookh = int(input())

    if dookh == 1:
        print('1.Ogow Biilka.')
        print('2.Bixi Biil.')
        print('3.Ka Bixi Biil')
        doorasho = int(input())

        if doorasho == 1:
            print('error occurred, please try again later')
            main()
        elif doorasho == 2:
            lacag = float(input("fadlan geli lacagta: "))

            if lacag <= Haraaga:
                doorasho2 = int(
                    input(f'ma hubtaa inaad bixisid bill lacagtiisu  tahay: $ {lacag} \n1. Haa \n2. Maya\n'))

                if doorasho2 == 1:
                    print('error occurred, please try again later')
                    main()

                if doorasho2 == 2:
                    print("Mahadsanid.")
                    main()
            else:
                print("haragaaga kugu ma filna")
                main()
        if doorasho == 3:
            number = int(input("fadlan geli lambarka: "))
            lacag = float(input("fadlan geli lacagta: "))
            number = str(number) # We convert the number to a string for validation purposes

            if len(number) == 9 and number.startswith('61') or number.startswith("77"):
                if lacag <= Haraaga:
                    doorasho3 = int(
                        input(f'ma hubtaa inaad bixisid bill lacagtiisu  tahay: $ {lacag} \n1. Haa \n2. Maya'))
                    if doorasho3 == 1:
                        print('error occurred, please try again later')
                        main()
                    else:
                        print("Mahadsanid.")
                        main()
                else:
                    print("haragaaga kugu ma filna")
                    main()
            else:
                print("Inavalid number formate ")
                main()


def Uwareeji_EVC():
    # This function is used for money transfer

    # Read the current balance from the 'Haraaga' file
    with open('Haraaga', 'r') as haraaga_file:
        Haraaga = float(haraaga_file.read())


    # This loop will remain running until the user enters a valid number
    while True:
        # Error handling code if the user enters an invalid number
        try:
            recipt_num = int(input("Fadlan geli mobile-ka \n"))
            break  # Break out of the loop if the input is a valid number
        except ValueError:
            print("You have to enter a number ")

    recipt_num = str(recipt_num) # We convert the "recipt_num" to a string for validation purposes
    money = float(input("Fadlan geli lacagta \n"))

    confirm = int(input(f"Ma hubtaa inaad ${money} u wareejisid {recipt_num} \n"
                        f"1.Haa\n"
                        f"2.Maya\n"))
    if confirm == 1:
        # Check if the recipient number is valid
        if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")) and confirm == 1:
            if money <= Haraaga:
                Haraage = Haraaga - money
                # Convert the "haraaga" value to a string before saving it to a file
                Haraage = str(Haraage)
                print(
                    f"[-EVCPlus-] ${money} ayaad uwareejisay {recipt_num}, Tar: {formatted_date} {formatted_time}, Haraagaagu waa ${Haraage}."
                    f"La soo deg App - ka WAAFI")
                trans = (
                    f"\n[-EVCPlus-] ${money} ayaad uwareejisay {recipt_num}, Tar: {formatted_date} {formatted_time}, Haraagaagu waa ${Haraage}."
                    f"La soo deg App - ka WAAFI")
                # Save the transaction information to a file named "trans.txt"
                with open('trans.txt', 'a') as file:
                    file.write(trans)
                    # Save the updated "haraaga" value to a file
                with open('Haraaga', 'w') as file:
                    file.write(Haraage)
                main()
            else:
                print("Haraaga kugama filnaa")
        else:
            print("Invalid number format ")
            # Recursive call to restart the function if there's an invalid number
            Uwareeji_EVC()
    else:
        print("Bye")
        main()


def last_action():
    try:
        # This line of code reads the last transaction from a file
        with open("trans.txt", "r") as file:
            lines = file.readlines()
            print(lines[-1])
            main()
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
            # Call the main function when you finish.
        main()


def Wareejint_dambesay():
    # Open the "trans.txt" file in read mode and read all lines.
    with open('trans.txt', 'r') as file:
        line = file.readlines()

    # Prompt the user to input a mobile number and convert it to a string
    recipt_num = int(input("Fadlan geli mobile-ka "))
    recipt_num = str(recipt_num)

    # Check if the entered mobile number is valid
    if len(recipt_num) == 9 and (recipt_num.startswith("61") or recipt_num.startswith("77")):
        # Iterate through each line in the file
        for num in line:
            # Check if the entered mobile number is present in any transaction line
            if recipt_num in num:
                print(num)
                # Call the main function
                main()
            else:
                print("Operation succeeded. No transactions to display!")
                # Call the main function
                main()
    else:
        print("Invalid number formate ")
        Wareejint_dambesay()


def Warbixin_Kooban():
    # This function displays a menu of transaction options for the user

    # Display menu options for the user to choose from.
    print("1. Last Action")
    print("2. Wareejintii u dambesay")
    print("3. Iibsashadi u dambeysay")
    print("4. Last 3 Actions")
    print("5. Email Me My Activity")

    option = int(input())  # Prompt the user to enter their choice

    if option == 1:
        last_action()  # Call the last_action function

    elif option == 2:
        print("Statementiga:")
        print("1. U dirtay")
        print("2. Kaheshay")
        option = int(input())

        if option == 1:
            Wareejint_dambesay()  # Call the Wareejint_dambesay function

        elif option == 2:
            recipt_num = input("Fadlan geli mobile-ka ")

            if len(recipt_num) == 9 and recipt_num.startswith("61"):
                print("Operation succeeded. No Transactions to display!")
                main()

            else:
                print("Error: Please enter a 9-digit number starting with '61'")
                Warbixin_Kooban()

    elif option == 3:
        Aqoonsi = input("Fadlan Geli aqoonsiga ganacsiga \n")
        print("Operation succeeded. No Transactions to display!")
        main()

    elif option == 4:
        last_3action()  # Call the last_3action function

    elif option == 5:
        Email = input("Fadalan geli email kaaga \n ")
        is_valid = validate_email(Email, verify=True)  # Check the validation of the email

        if is_valid:
            # If the email is valid, prompt the user to enter the duration of the activity
            date_hore = input("Fadlan Geli taarikhda hore (MAALIN/BISHA/SANAD, e.g: 05/07/2017)\n")
            date_danbe = input("Fadlan Geli taarikhda danbe (MAALIN/BISHA/SANAD, e.g: 16/10/2017)\n")

            try:
                # Check the validation of the date. If correct, an email will be sent
                now.strptime(date_hore, '%d/%m/%Y')
                now.strptime(date_danbe, '%d/%m/%Y')
                print(f"Your email is being processed, and the activity will be emailed to {Email}")
                main()

            except ValueError:
                # If the user enters an invalid date, print an invalid date message
                print("Invalid Date format")
                main()

        else:
            # If the email is not correct, print the message below
            print("The email you provided is not valid ")
            Warbixin_Kooban()



def salam_bank():
    # Prompt the user to choose an option for EVC Plus transaction
    option = int(input("1. Ka wareeji EVC Plus"))

    if option == 1:
        # Prompt the user to select a bank for the transaction
        print("Fadlan dooro xisaabta bangiga")
        print("1. Bank Beeraha")
        print("2. Salaam Sch")
        print("3. SALAAM SOMALI BANK")
        print("4. Darasalaam Bank")
        option = int(input())

        if option in [1, 2, 3, 4]:
            # Get account information and transaction details
            accountga = input("Fadlan geli account-ga: ")
            macluumad = input("Fadlan geli macluumaad: ")
            lacagta = float(input("Fadlan geli lacagta: "))
            print("ma jiro akoon lambar oo ku xidhan taleefoonka")
            main()

        else:
            print("Fadlan dooro number sax ah ")
            salam_bank()

    else:
        print("Fadlan dooro number sax ah ")
        main()



def maaraynta():
    # Display the options available for MAAREYNTA
    print("MAAREYNTA")
    print("1: bedel lambarka sirta ah")
    print("2: bedel luqada")
    print("3: wargelin mobile lumay")
    print("4: lacag xirasho")
    print("5: U Celi lacag qaldanty")
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
        main()


def bedel_pin():
    # Prompt the user to enter a new PIN
    pin = int(input("Fadlan Geli Pinkaga  Cusub"))

    # Prompt the user to confirm the new PIN
    hubi = int(input("Hubi Pinkaga Cusub"))
    if (pin == hubi):
        # Display a success message and save the new PIN to a file
        print("<-EVCPlus-> Waad ku guuleysatay in aad badasho PIN-Kaaga\n")
        pin = str(pin)
        with open('Pin', 'w') as file:
            bedel = file.write(pin)

        main()
    else:
        # Display an error message for PIN mismatch and prompt the user to try again
        print("Input Mismatch Plz try again Later:")
        bedel_pin()


def luqada():
    # Prompt the user to choose a language
    print("Fadlan dooro luqada:")
    print("1. Somali")
    print("2. English")

    lang = int(input(""))

    if lang == 1:
        # Display a success message for changing the language to Somali
        print("[EVCPlus] waad ku guulaysatay in aad badasho Luqadda")
        main()
    if lang == 2:
        # Display a success message for changing the language to English
        print("[-EVCPlus]You have successfully changed your language")
        main_english()
        



def mobile_lumay():
    # Prompt the user to enter the mobile number
    num = int(input("Fadlan Geli Mobileka lumay:  "))
    num = str(num)

    # Check if the entered mobile number is valid
    if len(num) == 9 and num.startswith("61") or num.startswith("77"):
        # Prompt the user to enter their PIN for confirmation
        pin = int(input("Fadlan Geli Numberkisa Sirta Ah:  "))
        print(f"Ma hubtaa in aad u diiwan Geliso Lumid number-kan {num}?")
        print("1:Haa")
        print("2:Maya")

        # Ask the user for confirmation
        check = int(input())

        # Read the PIN from the file.
        with open('Pin', 'r') as pin_file:
            pinka = int(pin_file.read())


        if pin == pinka:
            if check == 1:
                print("Waa laguu Diwangeliyey Mahadsanid ")
                main()
            else:
                print("Mahadsanid!")
                main()
        else:
            print("[EVCPLUS-] Nambarka Sirta ah waa Khalad ")
            main()

    else:
        print("invalid number format")
        main()


def lacag_xirsho():
    # Prompt the user to enter the incorrect transaction number
    mistake = int(input("Fadlan Geli number-ka Khalad-ka ah"))

    # Prompt the user to enter the correct transaction number
    corct = int(input("Fadlan Geli number-kii loo rabay"))

    # Prompt the user to enter additional information (macluumaad)
    maclumad = input("Fadlan Geli Macluumaad")

    # Ask the user if they confirm the transaction
    print("Ma hubtaa in aad xirato lacagtaan")
    print("1:Haa")
    print("2:Maya")
    check = int(input(""))


    if check == 1:
        # Display a success message for completing the transaction
        print("Waa laguu xiray lacagta Mahadsanid.")
        main()
    elif check == 2:
        # Display a message  cancellation
        print("Mahadsanid!")
        main()
    else:
        print("Mahadsanid!")
        main()


def lacag_qaladantay():
    enter = input("Fadlan Geli aqoonsiga lacag dirida")
    print("Invalid input format")
    main()


def mobile_bank():
    check = int(input("Fadlan Geli number-ka is diiwangelinta"))
    print("Activiation Record not found")
    main()


def bill_pay():
    # Display options for bill payment
    print("1. Itus Haraaga Bill ka ")
    print("2. Wada bixi Bill-ka ")
    print("3. Qeyb ka bixi Bill-ka ")

    # Prompt the user to choose an option
    option = int(input())

    if option in [1, 2, 3]:
        # Prompt the user to enter the bill reference number
        reference_num = input("Fadlan geli Bill reference number\n")

        # Display a message indicating  errors
        print("Some parameters are missing, please check your request")
        main()

    else:
        # Display a message for choosing an invalid option
        print("Fadlan dooro number sax ah ")
        main()


main()
