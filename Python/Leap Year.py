# Solution 1

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4==0) and (year%100!=0):
        leap = True
        return leap
    elif (year%400==0):
        leap = True
        return leap
    else:
        return leap

year = int(input())
print(is_leap(year))
