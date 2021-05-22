# importig funcitons that will be required to run our code
from os import system, name
from time import sleep
from typing import final


# using a list to store our inventory, each dictionary inside of the list representing the data for an item. 

def inventory():
    data=  [
        {"id": 1001, "Info":"1001    Chocolate Cupcake         Price   "+str(120),"Name":"Chocolate Cupcake","Price":120,"Stock":10},
        {"id": 1002, "Info":"1002    Butterscotch Cupcake      Price   "+str(120),"Name":"Butterscotch Cupcake","Price":120,"Stock":10},
        {"id": 1003, "Info":"1003    Red Velvet Cupcake        Price   "+str(120),"Name":"Red Velvet Cupcake","Price":120,"Stock":10},
        {"id": 1004, "Info":"1004    Hershey's Brownie         Price   "+str(80),"Name":"Hershey's Brownie","Price":80,"Stock":10},
        {"id": 1005, "Info":"1005    Fudge Brownie             Price   "+str(100),"Name":"Fudge Brownie","Price":100,"Stock":10},
        {"id": 1006, "Info":"1006    Oreo Shake                Price   "+str(499),"Name":"Oreo Shake","Price":499,"Stock":10},
        {"id": 1007, "Info":"1007    Vanilla Almond Milk       Price   "+str(499),"Name":"Vanilla Almond Milk","Price":499,"Stock":10},
        {"id": 1008, "Info":"1008    Raspberry Cupcake         Price   "+str(120),"Name":"Raspberry Cupcake","Price":120,"Stock":10},
        {"id": 1009, "Info":"1009    Lotus Brownie             Price   "+str(100),"Name":"Lotus Brownie","Price":100,"Stock":10}
    ]
    return data

# displays the inventory to the user

def userMenu(x):
    for each in x:
        print(each["Info"])

# clears the screen

def clear():
    if name == 'nt':
        _ = system('cls')

# sorts the given field
  
def bubble_sort(lst,check2):
    x=len(lst)
    if x>1:
        if check2=="l":
            for c in range(x-1):
                for i in range(0,x-c-1):
                    if lst[i]["Price"]>lst[i+1]["Price"]:
                        lst[i],lst[i+1]=lst[i+1],lst[i]
            return lst
        elif check2=="h":
            for c in range(x-1):
                for i in range(0,x-c-1):
                    if lst[i]["Price"]<lst[i+1]["Price"]:
                        lst[i],lst[i+1]=lst[i+1],lst[i]
            return lst

# searches for the given item in the list

def binary_search_iterative(lst, item):
    low,high=0, len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if item==lst[mid]["id"]:
            return mid
        elif item>lst[mid]["id"]:
            low=mid+1
        elif item<lst[mid]["id"]:
            high=mid-1
    return -1

# gives us the paths for our required list

def dijsktra(graph,start,end):
    lst_nodes=list(graph.keys())
    short_dist,visited,infinity={},[],9999
    for each_node in lst_nodes:
        if each_node==start:
            short_dist[each_node]=("", 0)
        else:
            short_dist[each_node]=("", infinity)                
    while len(visited)!=len(lst_nodes):
        lst=[]
        for value in short_dist.items(): 
            if value[0] not in visited:
                lst.append(value[1][1])
        min_d=min(lst)
        for key, value in short_dist.items():
            if min_d==value[1] and key not in visited:
                visited.append(key)
                for val in graph[key]:
                    temp=short_dist[key][1] + (val[1])
                    if temp<short_dist[val[0]][1]:
                        short_dist[val[0]]=(key,temp)
    path=[]
    x=""
    y=end
    while x!=start:
        x=short_dist[y][0]
        path.insert(0,(x,y))
        y=x
    time=0
    for each in path:
        time+=(short_dist[each[1]])[1]
    final=""
    for tuple in path:
        for each in tuple:
            if each not in final:
                final+=each+" --> "
    print()
    print("==> The path from our store to your area is ",final[:-4,"."])
    print()
    print("==> The time taken to reach your area will be  "+str(time)+" mins.")
    print()

# filters the inventory data, by either high or low using bubble sort

def filter():
    # print() statement for spacing
    print()
    # asks user if they would like to filter the prices
    check=input("Would you like to filter the prices? Y or N? ") 
    if check.lower()=="y":
        print()
        # if yes, then we ask if they would like to filter from low to high or high to low
        check2=input("To filter from low to high Enter L, Else H. ")
        if check2=="l":
            clear()
            # using bubble sort we will sort our inventory from low to high 
            x=bubble_sort(inventory(),check2)
            # display inventory 
            print("Prices filtered from low to high")
            print("ID      Model                   Price   PKR")
            userMenu(x)
        elif check2.lower()=="h":
            clear()
            # using bubble sort we will sort our inventory from low to high 
            x=bubble_sort(inventory(),check2)
            # display inventory 
            print("Prices filtered from high to low")
            print("ID      Model                   Price   PKR")
            userMenu(x)
    elif check.lower()=="n":
        # if they do not want to filter we pass
        pass

# updates the stock in the inventory when changes are made to cart

def stock(qnty,position):
    # gets current stock of item from inventory 
    x=(inventory()[position])["Stock"]
    # compares the stock with quantity entered by the user  
    # if the quantity equals to stock or if it is lower than stock then stock is updated in iventory and returns the updated stock value
    if x==qnty or x>qnty:
        y=inventory()
        d=y[position]
        d["Stock"]=x-qnty
        return x 
    # else if stock is less than our quantity then negative stock is returned
    elif x<qnty:
        return -x

# adds selected items to cart 

def add(cart):
    # asks user for the item that they would like to add to cart
    item=int(input("Enter the id of the item u would like to add: "))
    # we get the index of our dictionary from the list 
    position=binary_search_iterative(inventory(),item)
    # check for if index in list 
    if position!=-1:
        # ask for the required quantity of the item
        qnty=int(input("Kindly enter the quantity of the item: "))
        # check, using our stock fucniton, that if the entered quantity is available 
        ok=stock(qnty,position)
        if ok<0:
            # if there isnt enough stock it displays an error msg and calls the add(cart) fucntion back
            print("There isn't that much stock, only "+str(-1*ok)+" pieces are available.")
            print("Kindly selecct the quantity accordingly!")
            add(cart)
        else:    
            # if stock is present then it adds the to the cart with the set quantity and their total price
            price=(inventory()[position])["Price"]*qnty
            name=(inventory()[position])["Name"]
            cart[(inventory()[position])["id"]]=[name,qnty,price]
            print("Item added to cart!")
    else:
        # if id not in inventory then it outputs an error msg
        print("Enter a valid id to add!")

# deletes the selected item from the cart 

def remove(cart):
    # displays cart to user 
    viewcart(cart)
    # inputs for the item id to be removed  
    item=int(input("Enter the item id that you would like to remove: "))
    # checks if item is present in cart
    if item in cart.keys():
        # inputs the quantity of that item to be removed
        qnty=int(input("Also enter the quantity that you would like to remove: "))
        # if the cart quantity matches the entered quantity 
        if cart[item][1]==qnty or cart[item][1]==1:
            # deletes that item from cart  
            del(cart[item])
        # else if quantitiy does not match the items quantity in cart then it tells the user to enter a valid quantity  
        elif cart[item][1]<qnty:
            print("Entered quantity doesn't exist, enter a valid quantity to remove!")
        # else, then it removes the set quantity and updates the 
        else:
            intial=cart[item][1]
            cart[item][1]=(cart[item][1])-qnty
            cart[item][2]=(cart[item][2])-((cart[item][2]/intial)*qnty)
        print("Item removed from cart!")
    else:
        print("Enter a valid id to remove!")    
def viewcart(cart):
    print("ID   Name                        Quantity    Price")
    for key, value in cart.items():
        print(str(key)+" "+value[0]+"          "+str(value[1])+"           "+str(value[2]))
def checkout(cart):
    total=0
    for key, value in cart.items():
        total+=value[2]
    viewcart(cart)
    print()
    print("===================================================")
    print("Total:                                      ",total)
    print("===================================================")
    if total<=0:
        print()
        print("Your cart is empty, you can not proceed to checkout!")
        print()
def location():
    areas={
            1:"DHA",
            2:"Bahadrabad",
            3:"Clifton",
            4:"Cantt",
            5:"Saddar",
            6:"Nazimabad",
            7:"Saki Hassan",
            8:"Garden",
            9:"North Nazimabad",
            10:"North KArachi"
    }
    links={
          "DHA" : [("Bahadrabad",22), ("Clifton",12),("Cantt",12)],
          "Bahadrabad" : [("Saki Hassan",19), ("Saddar",9),("DHA",20)],
          "Clifton" : [("Saddar",12), ("Cantt",10), ("Garden",20), ("DHA",11)],
          "Cantt" : [("DHA",14), ("Clifton",11), ("Saddar",8)],
          "Saddar" : [("Clifton", 14), ("Cantt",7), ("Bahadrabad",14), ("North Nazimabad",25), ("Nazimabad",18), ("Garden",9)],
          "Nazimabad" : [("North Nazimabad",10), ("North KArachi",17),("Saddar",20)],
          "Saki Hassan":[("Bahadrabad",21)],
          "Garden":[("Clifton",18),("Saddar",9)],
          "North Nazimabad":[("Nazimabad",11)],
          "North KArachi":[("Nazimabad",18)]
    }
    print("""
    Our Store is located in DHA and below are the available delivery options

    Delivery options
    ================================
    1:"DHA",
    2:"Bahadrabad",
    3:"Clifton",
    4:"Cantt",
    5:"Saddar",
    6:"Nazimabad",
    7:"Saki Hassan",
    8:"Garden",
    9:"North Nazimabad",
    10:"North KArachi"
    """)
    choice=int(input("Kindly choose your residential area: "))
    print("-----------------------------------")
    if choice in areas.keys():
        if choice==1:
            print("==> Our Store is located in your area.")
            print() 
            print("==> The time taken to reach your area will be  "+str(5)+" mins.")
            print()
        else:
            dijsktra(links,"DHA",areas[choice])
        print("-----------------------------------")
    else:
        print("You have entered an invalid choice, kindly enter again!")
        location()  
def shoppingCart():
    print("""
    Shopping basket options
    ================================
    1: Add item 
    2: Remove item
    3: View cart
    0: Proceed to checkout

    """)
    cart={}
    choice=int(input("Kindly choose your choice: "))
    print("----------------------------")
    while True:
        if choice==1:
            add(cart)
        elif choice==2:
            remove(cart)
        elif choice==3:
            viewcart(cart)
        elif choice==0:
            clear()
            x=location()
            checkout(cart)
            break
        print()
        choice=int(input("Kindly choose your choice: "))
        print("----------------------------")
            
def main():
    print("""
    ========================================

        
       Welcome to our online samsung store
        
         
    ========================================
    """)
    # sleep(1)
    # clear()
    print("These are the available products.")
    print()
    print("************************************************")
    print()
    print("ID      Model                   Price   PKR")
    userMenu(inventory())
    print()
    print("************************************************")
    filter()
    shoppingCart()
    OK=input("TYPE Enter for a new user or End to end program: ")
    if OK.lower()=="enter":
        clear()
        main()
    elif OK.lower()=="exit":
        exit()

    
main()
