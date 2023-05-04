def diagonal_name():
    name=input("Enter your name")
    
    for i in range(0,len(name)):
         for a in range(0,len(name)):
             if(i==a):
                 print(name[a],sep=" ",end=" ")
             else:
                print("*",sep=" ",end=" ")
         print()
diagonal_name()

         
    
    
