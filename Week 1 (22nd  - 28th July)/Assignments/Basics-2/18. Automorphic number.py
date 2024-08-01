originalNum = input("Enter the number : ")
num = int(originalNum)

square = pow(num, 2)
mod = pow(10, len(str(num)))

print(f"{num} is a Automorphic number" if square % mod == num else f"{num} is not a Automorphic number")

# Method - 2

# square = num ** 2
# square_string = str(square)
# len_square_string = len(square_string)
# print(square_string[len_square_string-1])
# print(square_string[-len_square_string])
# print(square_string[-len_square_string::])
print(f"{num} is a Automorphic number" if int(str(num**2)[-len(str(num))::]) == num else f"{num} is not a Automorphic number")

# Method - 3
a = str(num)

num1 = num ** 2
b = str(num1)

print(f"{num} is a Automorphic number" if b.endswith(a) else f"{num} is not a Automorphic number")
