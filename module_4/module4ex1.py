length = float(input("Enter the length of the zander in centimeters: "))
difference = (42 - length)
if length <= 42:
    print("The zander does not meet the size limit. ")
    print("Please release the fish back into the lake. ")
    print(f"The fish was {difference} centimeters below the size limit. ")

if length >= 42: 
    print("The zander meets the size limit")
    