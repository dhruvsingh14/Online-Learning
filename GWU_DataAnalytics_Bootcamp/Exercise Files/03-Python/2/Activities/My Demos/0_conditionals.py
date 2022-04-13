# conditionals

# if-then 1

x=42

if x==0:
    print('zero true')
elif x==1:
    print('one true')
elif x==2:
    print('two true')
elif x==3:
    print('three true')
elif x==4:
    print('four true')
elif x==5:
    print('five true')
else:
    print('none true')

# if-then 2: user input
hungry = input("are you hungry? (yes/no)")

if hungry == "yes":
    print("Let's eat!")

# if-then 3: driver's license
age = input("Enter your age here: ")
# age = int(age)

if age < 16: 
    print("you need to be at least 16 to apply for a driver's license")
else: 
    print("proceed!")

