number_to_check = int(input("Enter number to check for Odd or even :"))

print(f"{number_to_check} is a Even number" if(number_to_check % 2 == 0) else f"{number_to_check} is a Odd number")

def check_OddOrEven_Number(num):
    return (num % 2 == 0)

print(f"{number_to_check} is a Even number" if(check_OddOrEven_Number(number_to_check)) else f"{number_to_check} is a Odd number")