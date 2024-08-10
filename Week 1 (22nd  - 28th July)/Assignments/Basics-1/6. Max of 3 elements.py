a, b, c = map(int,(input("Enter 3 numbers separated by comma : ").split(",")))

print(f"Value of a : {a} \n" f"Value of b : {b} \n" f"Value of c : {c}")

def find_max_of_three_numbers(a,b,c):
    # Always use int_min or int_max for return value
    if((a > b and a > c) or (a == b and a == c) or (a == b and c < a)):
        return a
    elif((b > a and b > c) or (b == c and a < b) or (c == a and b > c)):
        return b
    else:
        return c
    
    
print(f"Maximum of three numbers : {a}, {b} and {c} is : {find_max_of_three_numbers(a,b,c)}")

print(f"Maximum of three numbers : {a}, {b} and {c} is : {max(a,b,c)}")
