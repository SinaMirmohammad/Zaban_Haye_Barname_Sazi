#Sina
#!/usr/bin/env python3
import re
regex = re.compile(r'([0-9]+)([0-9])')
def check_phone():
    while True:
        try:
            phone = str(input("Enter phone => "))
            count = len(phone)
            if count == 11:
                if(re.fullmatch(regex, phone)):
                    print("Valid phone")
                    return phone
                    break
                else:
                    print("Invalid phone")
            else:
                print("phone Number is invalid")
        except:
            break

#phone = str(input("Enter phone => "))
a = check_phone()
print(a)