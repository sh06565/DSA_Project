# from typing import KeysView
# import keyboard
from os import system, name
from time import sleep
# check git hub saved? 
def inventory():
    data=  [
        {"id": 1001, "Info":"1001    Samsung Galaxy A20      Price   "+str(15999),"Name":"Samsung Galaxy A20","Price":15999,"Stock":5},
        {"id": 1002, "Info":"1002    Samsung Galaxy A21      Price   "+str(18999),"Name":"Samsung Galaxy A21","Price":18999,"Stock":5},
        {"id": 1003, "Info":"1003    Samsung Galaxy A30      Price   "+str(23999),"Name":"Samsung Galaxy A30","Price":23999,"Stock":5},
        {"id": 1004, "Info":"1004    Samsung Galaxy A51      Price   "+str(41999),"Name":"Samsung Galaxy A51","Price":41999,"Stock":5},
        {"id": 1005, "Info":"1005    Samsung Galaxy A52      Price   "+str(44999),"Name":"Samsung Galaxy A52","Price":44999,"Stock":5},
        {"id": 1006, "Info":"1006    Samsung Galaxy A61      Price   "+str(53499),"Name":"Samsung Galaxy A61","Price":53499,"Stock":5},
        {"id": 1007, "Info":"1007    Samsung Galaxy A72      Price   "+str(59999),"Name":"Samsung Galaxy A72","Price":59999,"Stock":5},
        {"id": 1008, "Info":"1008    Samsung Galaxy A81      Price   "+str(61999),"Name":"Samsung Galaxy A81","Price":61999,"Stock":5},
        {"id": 1009, "Info":"1009    Samsung Galaxy A82      Price   "+str(67999),"Name":"Samsung Galaxy A82","Price":67999,"Stock":5}
        ]
    return data
def userMenu(x):
    for each in x:
        print(each["Info"])
def clear():
    if name == 'nt':
        _ = system('cls')
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
        path.insert(0,(x, y))
        y=x
    print("==>The shortest path is : "+"\n",path)
    print("The paths are as follows: "+"\n")
def filter():
    print()
    check=input("Would you like to filter the prices? Y or N? ")
    if check.lower()=="y":
        print()
        check2=input("To filter from low to high Enter L, Else H. ")
        if check2=="l":
            clear()
            x=bubble_sort(inventory(),check2)
            print("Prices filtered from low to high")
            print("ID      Model                   Price   PKR")
            userMenu(x)
        elif check2.lower()=="h":
            clear()
            x=bubble_sort(inventory(),check2)
            print("Prices filtered from high to low")
            print("ID      Model                   Price   PKR")
            userMenu(x)
    elif check.lower()=="n":
        pass
def stock(qnty,position):
    x=(inventory()[position])["Stock"]
    if x==qnty or x>qnty:
        y=inventory()
        d=y[position]
        d["Stock"]=x-qnty
        return x 
    elif x<qnty:
        return -x
def add(cart):
    item=int(input("Enter the id of the item u would like to add: "))
    position=binary_search_iterative(inventory(),item)
    if position!=-1:
        qnty=int(input("Kindly enter the quantity of the item: "))
        ok=stock(qnty,position)
        if ok<0:
            print("There isn't that much stock, only "+str(-1*ok)+" pieces are available.")
            print("Kindly selecct the quantity accordingly!")
            add(cart)
        else:    
            price=(inventory()[position])["Price"]*qnty
            name=(inventory()[position])["Name"]
            cart[(inventory()[position])["id"]]=[name,qnty,price]
            print("Item added to cart!")
    else:
        print("Enter a valid id to add!")
def remove(cart):
    viewcart(cart)
    item=int(input("Enter the item that you would like to remove: "))
    if item in cart.keys():
        qnty=int(input("Also enter the quantity that you would like to remove: "))
        if cart[item][1]==qnty or cart[item][1]==1:
            del(cart[item])
        elif cart[item][1]<qnty:
            print("Entered quantity doesn't exist, enter a valid quantity to remove!")
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
            print("Your package will be delivered in 5 mins")
        else:
            dijsktra(links,"DHA",areas[choice])
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
            checkout(cart)
            location()
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
