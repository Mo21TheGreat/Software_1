def check_number(number):
    if number >= 1:
        return True 
    else:
        return False

number = int(input("Number: "))

if check_number(number):
    print("ok")
else:
    print("error")