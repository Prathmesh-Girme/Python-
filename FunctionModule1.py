import Marvellous1

def main():
    
   print("Enter 1st number:")
   value1=int(input())
   
   print("Enter second number:")
   value2=int(input())
   
   Ret = Marvellous1.Addition(value1 , value2)   
   
   print("Addition is:",Ret )
   
if __name__=="__main__":
    main()