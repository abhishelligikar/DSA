num, power = map(int, input("Enter the range of number separted by space: ").split(" "))

print(pow(num,power))

# Method - 2
output = 1
for i in range(power):
  output*=num
print(output)

# Method - 3
print(num**power)

# Method - 4
def find_power_of_numbers(num, power):
    if power == 0:
        return 1
    
    return num * find_power_of_numbers(num, power - 1)

print(find_power_of_numbers(num, power))