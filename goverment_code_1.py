#SinaMirmohammad
#!/usr/bin/env python3

import re

regex = re.compile(r'([0-9]+)([0-9])')

def goverment_validation_code():
    while True:
        try:
            user_input = str(input("input Goverment Code => "))
            count_goverment_code = len(user_input)
            if(re.fullmatch(regex, user_input)):
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
                        print("[*]Govermrnt code is => ", boolian)
                        if str(boolian) == "True":
                            return user_input
                            break
                    elif save < 2:
                        save = found_digit
                        #print("found digit => ", found_digit)
                        #print("user digit => ", user_input[9])
                        boolian = bool(int(found_digit) == int(user_input[9]))
                        print("[*]Goverment code is => ", boolian)
                        if str(boolian) == "True":
                            return user_input
                            break
                    #-----------------------------
                else:
                    print("[!]code lenth is not valid")

            else:
                print("[!]Please enter Number of code")
        except:
            break

#-----------------------------------------

a = goverment_validation_code()
print(a)