def findEligibilityForMarriage(girlAge, boyAge):
    if(girlAge < 18 or boyAge < 21):
        return 'No'
    elif(girlAge > 18 and boyAge < 21):
        return 'No'
    elif(girlAge < 18 and boyAge > 21):
        return 'No'
    elif(girlAge > 18 and boyAge > 21):
        return 'Yes'
    else:
        return 'No'

girlAge, boyAge = map(int, input("Enter Girl and Boy age separated by space: ").split())
print("GirlAge is : ", girlAge)
print("BoyAge is : ", boyAge)
print("Are they eligible for marraiage? :", findEligibilityForMarriage(girlAge, boyAge))


        