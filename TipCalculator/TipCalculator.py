bill = float(input("Enter Your Bill: "))
Persons = float(input("Number Of Persons: "))


totalBill = bill * 1.12

print(f"Total Bill is: {round(totalBill,2)} and each person has to pay {round(totalBill/int(Persons),2)}")

