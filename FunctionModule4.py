from Marvellous1 import Addition, substraction

def main(): #entry point func
    
   print("Enter 1st number:")
   value1=int(input())
   
   print("Enter second number:")
   value2=int(input())
    
   
   Ret = Addition(value1 , value2)   
   
   print("Addition is:",Ret )
   
   Ret = substraction(value1 , value2)  #error
   
   print("Substraction is:",Ret )
   
if __name__=="__main__":
    main()