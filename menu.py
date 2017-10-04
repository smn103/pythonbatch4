class menu:
        def __init__(self):
                self.menu = {'Burger':'60','French Fries':'80','Chicken Wings':'90'}
        def show(self):
                print (self.menu)
        def add(self,i,n):
                self.menu[i]=n


c=menu()
while(1):
    ch=int(input("Enter your Choice as\n1.To Display the Menu.\n2.To Add item.\n3.To Exit.\n"))
    if ch==1:
        c.show()
    elif ch==2:
        i=input("Enter the Item to be Added\n")
        p=input("Enter the Price\n")
        c.add(i,p)
    elif ch==3:
        break
    else: print("Invalid Choice")
