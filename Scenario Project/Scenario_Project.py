date = "14th of November 2023"
print("Hi, welcome to the Copington Adventure Theme Park!")
print("The price for adult tickets are £20")
print("For children it is £12")
print("And Senior Citizen it is £11")
Adult_price = 20.00
child_price = 12.00
Senior_price = 11.00
wristband_cost = 20.00
parking_cost = 0.00
print("how many adult tickets do you need: ")
y = input("Type amount: ")
sum = int(Adult_price) * int(y)
print("how many child tickets would you like: ")
y = input("Type amount: ")
ct = int(child_price) * int(y)
print("how many citizen tickets would you like: ")
y = input("Type amount: ")
st = int(Senior_price) * int(y)
print("how many visitors would like wristbands for the rides?: ")
y = input("Type amount: ")
wb = int(wristband_cost) * int(y)
print("what is the lead booker surname?: ")
lead_name = input("Type leads name: ")
x = input("Would you like a car pass: ")
if x == "yes":
    print("here is your car pass")
else:
    print("alright no problem")
print("The Reciept")
Total_cost = int(wb) + int(sum) + int(ct) + int(st)
print(lead_name, Total_cost , wb , date )
x = input("Would you like to pay with cash or card?: ")
print(x)
if x == "cash": 
    y = input("Enter amount: ")
    Change = int(y) - int(Total_cost)
    print(Change)
    print("here is your change")
else: 
    print("Thank you for your purchase")