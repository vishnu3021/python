year=int(input('enter a year:'))
if year%400==0:
    print(f"{year} is a leap year")
elif year%4==0 and year%100!=0:
    print(f'{year} leap year')
else:
    print(f'{year} not a leap year')