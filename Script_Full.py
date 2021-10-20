#SinaMirmohammad
#!/usr/bin/env python3

import re
from tinydb import TinyDB, Query
from termcolor import colored, cprint

#DataBase
db = TinyDB('User_db.json')

#Name
regex_1 = re.compile(r'([A-Za-z]+)([A-Za-z])')

def check_name():
    while True:
        try:
            name = str(input("Enter name => "))
            count = len(name)
            if count <= 10:
                if(re.fullmatch(regex_1, name)):
                    print(colored("[*]Valid name", 'green'))
                    return name
                    break

                else:
                    print(colored("[!]Invalid name", 'red'))

            else:
                print(colored("[!]the name is long", 'red'))
        except:
            break

#Price
regex_2 = re.compile(r'\d+\.\d+')

def check_price():
    while True:
        try:
            price = str(input("Enter price of Product => "))
            if(re.fullmatch(regex_2, price)):
                print(colored("[*]Valid price", 'green'))
                return price
                break
            else:
                print(colored("[!]Invalid price", 'red'))
        except:
            break

#Phone
regex_3 = re.compile(r'([0-9]+)([0-9])')
def check_phone():
    while True:
        try:
            phone = str(input("Enter phone => "))
            count = len(phone)
            if count == 11:
                if(re.fullmatch(regex_3, phone)):
                    print(colored("[*]Valid phone", 'green'))
                    return phone
                    break
                else:
                    print(colored("[!]Invalid phone", 'red'))
            else:
                print(colored("[!]Invalid phone", 'red'))

        except:
            break

#Mail
regex_4 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check_mail():
    while True:
        try:
            mail = str(input("Enter Mail => "))
            if(re.fullmatch(regex_4, mail)):
                print(colored("[*]Valid Email", 'green'))
                return mail
                break
            else:
                print(colored("[!]Invalid Email", 'red'))
        except:
            break

#Goverment_code
regex_5 = re.compile(r'([0-9]+)([0-9])')

def goverment_validation_code():
    while True:
        try:
            user_input = str(input("input Goverment Code => "))
            count_goverment_code = len(user_input)
            if(re.fullmatch(regex_5, user_input)):
                if count_goverment_code == 10:
                    sum_code = user_input[0] * 10 + user_input[1] * 9
                    #-------------------------------
                    i = 0
                    total = 0
                    found_digit = 0
                    for i in range(0,9):
                        sum = int(user_input[i]) * (10 - i)
                        #print(user_input[i])
                        #print(user_input[i] + " * " + str(10 - i) + " =>", sum)
                        total = total + sum
                        i += 1
                    #-------------------------------
                    #print("total => ", total)
                    save = total % 11
                    #-------------------------------
                    if save >= 2:
                        found_digit = 11 - save
                        #print("found digit => ", found_digit)
                        #print("user digit => ", user_input[9])
                        boolian = bool(int(found_digit) == int(user_input[9]))
                        #print("[*]Govermrnt code is => ", boolian)
                        if str(boolian) == "True":
                            print(colored("[*]Govermrnt code is Valid", 'green'))
                            return user_input
                            break
                        else:
                            print(colored("[*]Govermrnt code is Invalid", 'red'))
                    elif save < 2:
                        save = found_digit
                        #print("found digit => ", found_digit)
                        #print("user digit => ", user_input[9])
                        boolian = bool(int(found_digit) == int(user_input[9]))
                        if str(boolian) == "True":
                            print(colored("[*]Govermrnt code is Valid", 'green'))
                            return user_input
                            break
                        else:
                            print(colored("[*]Govermrnt code is Invalid", 'red'))
                    #-----------------------------
                else:
                    print(colored("[!]code lenth is invalid", 'red'))

            else:
                print(colored("[!]Please enter Number of code", 'red'))
        except:
            break

#Get - Inputs -> Validate !
name = check_name()
phone = check_phone()
price = check_price()
mail = check_mail()
g_code = goverment_validation_code()

user_record = {'name': name, 'phone': phone, 'price': price, 'mail': mail, 'Goverment_code': g_code}
db.insert(user_record)
print(db.all())
db.close()