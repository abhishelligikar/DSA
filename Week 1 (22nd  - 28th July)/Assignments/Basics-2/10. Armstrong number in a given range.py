low, high = map(int, input("Enter the range of number separted by '-' : ").split("-"))
armstrong_numbers = []

def getArmstrongNumbers(low, high):
    
    while low <= high:
        if low == high:
            return armstrong_numbers
        
        if low == 0:
            return armstrong_numbers
        
        low_length = len(str(low))
        sumValue = 0
        num = low
        for i in range(low_length):
            digit = int(num%10)
            num = num/10
            sumValue += pow(digit,low_length)
            
        if low == sumValue:
            armstrong_numbers.append(low)
            
        low += 1
        
    return armstrong_numbers
            
print(getArmstrongNumbers(low,high))