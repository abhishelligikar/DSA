# Use of ternary operator
totalAmount = int(input("Enter total amount : "))
print(type(totalAmount))
def calculateTaxAmount(amount: int):
    if(amount > 50000):
        print('Total tax amount would be : ', (amount * 10)/100)
    else:
        print('Total tax amount would be : ', (amount * 5)/100)
        
calculateTaxAmount(totalAmount)

# using ternanry operator
print("Total tax amount would be (using ternary operator): ", ((totalAmount * 10) / 100) if(totalAmount > 50000) else ((totalAmount * 5) / 100))