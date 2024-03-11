number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

election = 0

while election != 6:
    print(""" 
    Please indicate with a number the operation you wish to perform:       
          
    1) Add
    2) Subtract 
    3) Multiply
    4) Divide
    5) Change of values
    6) Exit             
    """)
    
    election = int(input())
    
    if election == 1:
        print(" ")
        print("Result: ", number_1,"+", number_2,"=",number_1+number_2)
        
    if election == 2:
        print(" ")
        print("Result: ", number_1,"-", number_2,"=",number_1-number_2)
        
    if election == 3:
        print(" ")
        print("Result: ", number_1,"*", number_2,"=",number_1*number_2)
        
    if election == 4:
        print(" ")
        print("Result: ", number_1,"÷", number_2,"=",number_1/number_2)
        
    if election == 5:
        print(" ")
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        
    if election == 6:
        print("")
        print("Thank you for using the calculator :)")
        
        
        
        
        
    