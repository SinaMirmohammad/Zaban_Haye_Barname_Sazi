#Sina
#!/usr/bin/env python3
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check_mail():
    while True:
        try:
            mail = str(input("Enter Mail => "))
            if(re.fullmatch(regex, mail)):
                print("Valid Email")
                return mail
                break
            else:
                print("Invalid Email")
        except:
            break


a = check_mail()
print(a)