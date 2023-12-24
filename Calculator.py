"""Simple calculator for basic Arithmetic operations"""

def calculator(n1,n2,operator):
    if operator == '+':
        print("The sum is:",n1+n2)
    
    elif operator ==  '-' :
        print("The substraction is:",n1-n2) 
          
    elif operator ==  '*' :
        print("The substraction is:",n1*n2) 
          
        
    elif operator ==  '/' :
        print("The substraction is:",n1/n2) 
        
    else:
        print("Invalid operator")      
        
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))

operator=input("Enter the operator [+,-,*,/]")

calculator(n1,n2,operator)
        
        
        
        
        
    