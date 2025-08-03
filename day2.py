#Q1 Additin of number
# num1 = int(input('Enter your first number: '))
# num2 = int(input('Enter Your Second Number: '))
# addition  = num1+num2
# print(f'Your Sum is {addition}')

#Q2 Swap of number
# num1 = int(input('Enter First Number: '))
# num2  = int(input('Enter Second Number'))

# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2

# print(f'updated value of num1 is : {num1}')
# print(f'updated value of num2 is : {num2}')

#Q3 Square of a number

# num1 = int(input('Enter a number: '))
# square_of_number = num1**2
# print(f'Square of a number is: {square_of_number}')

#Q4 Area of rectangle
# length = int(input("Enter the length of a number: "))
# breadth = int(input('Enter the breadth of a number: '))
# area_of_rectangle = length * breadth
# print(f'Area of rectangle is : {area_of_rectangle}')

#Q5 convert Kilometer into meter

# value_in_km = int(input('Enter the value in Kilometer: '))
# value_in_meter = value_in_km * 1000
# print(f'value in meter is: {value_in_meter}')

#Q6 convert meter into kilometer
# value_in_meter = int(input('Enter value in meter: '))
# value_in_kilometer = value_in_meter / 1000
# print(f'value in kilometer is : {value_in_kilometer} Kilometer')

#Q7 conver celcius to fahrenheit
# temp_in_celcius = float(input('Enter temperature in celcius : '))
# temperature_in_fehr = (temp_in_celcius*(9/5))+32
# print(f'temperature in fehrenhite is : {temperature_in_fehr}')

#Q8 convert ferhanite to celcius
# temp_in_feh = float(input("Enter temperature in fehr : "))
# temp_in_celcius = float(temp_in_feh-32)*(5/9)
# print(f'Temp in celcius is {temp_in_celcius}')

#Q9 calculate the simple intrest

# principal = int(input('enter the principal amount: '))
# rate = float(input('Enter the rate of intrest : '))
# time = float(input('Enter the time period in years : '))
# si = (principal*rate*time)/100
# print(f'simple intrest is {si}')

#Q10 calculate the compound intrest 
principal = int(input('enter the principal amount: '))
rate = float(input('Enter the rate of intrest : '))
time = float(input('Enter the time period in years : '))
ci = principal*((1+(rate/100))**time)-principal
print(f'compound intrestr is : {ci}')