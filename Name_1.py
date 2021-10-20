#Sina
#!/usr/bin/env python3
import re
regex = re.compile(r'([A-Za-z]+)([A-Za-z])')

def check_name():
    while True:
        try:
            name = str(input("Enter name => "))
            count = len(name)
            if count <= 10:
                if(re.fullmatch(regex, name)):
                    print("Valid name")
                    return name
                    break

                else:
                    print("Invalid name")

            else:
                print("the name is long")
        except:
            break

a = check_name()
print(a)