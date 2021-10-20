#Sina
#!/usr/bin/env python3
import re

#regex = re.compile(r'([0-9]+)([.]+)([0-9])')
regex = re.compile(r'\d+\.\d+')

def check_price():
    while True:
        try:
            price = str(input("Enter price of Product => "))
            if(re.fullmatch(regex, price)):
                print("Valid price")
                return price
                break
            else:
                print("Invalid price")
        except:
            break


a = check_price()
print(a)