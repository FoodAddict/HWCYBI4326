# Amadeus Dutremaine

# Instructions: For each problem, submit the Python program as typed text. Ensure you type your
# solutions directly into a Word document. DO NOT include screenshots of the code.
# 1. [25pt] Create Python script that performs the following:
# a. [10pt] Create different variables using the following types: integer, float, string and
# Boolean.
# b. [15pt] Print each variables along with its type using the type() function.

# 2. [25pt] Write a Python program that asks the user to input their age and then prints a
# message based on the following conditions:
# a. [5pt] If the age is less than 18, print “You are a minor”.
# b. [10pt] If the age is between 18 and 65, print “You are an adult”.
# c. [5pt] If the age is 65 or older, print “You are a senior citizen”.

# 3. [25pt] Write a Python program that prints the sum of all even numbers from 1 to 100 using a
# while loop.

# 4. [25pt] Write a Python program that asks the user to input a sentence and then prints:
# a. [5pt] The sentence in all uppercase letters.
# b. [5pt] The number of words in the sentence.
# c. [10pt] Whether the sentence starts with the letter ‘A’ or ‘a’. In other words, the
# character must be case-insensitive.

# I am kinda Familiar with Python. I intend to add these funtions to a github website eventually however for 
# this hw i will be using the console to operate. All Questions will have a seperate function that can be 
# selected from in the menu

def dataTypes():
    integerExample = 1
    floatExample = 1.5
    stringExample = "String Example"
    booleanExample = True

    print("integerExample = ", integerExample, "DATATYPE: ", type(integerExample))   

    print("floatExample = ", floatExample , "DATATYPE: ",type(floatExample))

    print("stringExample = ", stringExample, "DATATYPE: ", type(stringExample))
    
    print("booleanExample = ", booleanExample, "DATATYPE: ", type(booleanExample))

def ageCheck():
    try:
        #Get Data
        age = input("Enter Age: ")
        age = int(age)
        #compare and output
        if age < 18:
            print("You are a Minor")
        elif age > 18 and age < 65:
            print("You are an Adult")
        else:
            print("You are a Senior")
    except ValueError:
        #Output Error Notification
        print("Invalid Input")

def evenSUM():
    number = 1
    sum = 0
    while number <= 100:
        #find the even numbers
        if number % 2 == 0:
            # Adder
            sum += number
        #Counter
        number+=1
    print(sum)

def stringData():
    dataString = input("Enter Data: ")
    print("UPPERCASE: ", dataString.upper())
    print("WORDCOUNT: ",len(dataString.split()))
    print("First Char Checker: ")
    if dataString.startswith('A'):
        print("String Starts with 'A'.")
    elif dataString.startswith('a'):
        print("String Starts with 'a'.")
    else:
        print("String doesn't start with 'A' or 'a'.")

option = 0
try:
    while option != 5:
        option = int(input("Please Select an Option: \n 1) Age Check \n 2) Data Type Examples \n 3) Sum of Evens to 100 \n 4) String Data \n 5) Exit \n"))
        if option == 1: 
            ageCheck()
        elif option == 2:
            dataTypes()
        elif option == 3:
            evenSUM()
        elif option == 4:
            stringData()
        elif option == 5:
            print("Thank You and Have a Nice Day!!")
        else:
            print("Invalid Option")
except ValueError:
        #Output Error Notification
        print("Invalid Input")   
