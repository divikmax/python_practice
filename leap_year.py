# Check if a Year is a Leap Year or Not 
year=int(input("enter the year:"))
print("It's a leap year" if(year%4==0 or (year%400==0 and year%100!=0)) else "It's not a leap year")