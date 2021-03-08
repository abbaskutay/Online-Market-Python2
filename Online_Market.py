import datetime

print "****Welcome to Sehir Online Market****"
global basket
basket = {'ahmet':{},'meryem':{}}

def logging_system():
  global user
  name = dict ()
  name["ahmet"]="sehir123"
  name["meryem"]="4444"

  print  ("Please log in by providing your user credentials:")
  username= raw_input("username")
  password= raw_input("password")
  while (1):
       for user in name:

           if user==username:
               if password==name[user]:
                    print "Successfully logged in!"
                    return user
       #         we wrote this code to get username and passsword from the dict that we created above.

       print 'Your user name and/or password is not correct. Please try again!'
       username = raw_input("username")
       password = raw_input("password")


print "Welcome," +logging_system() + " " + "! Please choose one of the following options by entering the corresponding menu number."
global inventory
inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7],
                 'apples': [20, 5], 'banana': [10, 8], 'berries': [30, 3],
                 'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12],
                 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9], }


def selecting ():
    global inventory, selection, u,selected, amount,adding_to_basket1,count,adding_to_basket
    count = 1
    u = []
    choosing = raw_input("What are you searching for?").lower()
    while True:
        for selected in inventory.keys():
            if choosing in selected:
                u.append(selected)
        #         we wrote this code when we search items we will put them into the lsit to use it after.
        if len(u) == 0:
            choosing = raw_input("Your search did not match any items. Please try something else (Enter 0 for main menu):")
        #     when we search sth has not in the inventory the program will ask again.
        else:
            break
    print 'found ' + str(len(u)) + " similar items"
    for selected in u:
        print str(count) + ".", selected, str(inventory[selected][1]) + "" + "$"
        count += 1
    #     firstly we used for loop to get item i our which  called "u" and then we got the items anf their prices
    adding_to_basket = int(raw_input("Please select which item you want to add to your basket (Enter 0 for main menu):"))
    adding_to_basket1 = str(u[adding_to_basket - 1])
    # we used adding_to_basket1 to get item that we choosed, we used count in for loop and and there we decreased 1 to get item.
    amount = int(raw_input("adding " + adding_to_basket1 + " Enter Amount:"))

    while True:
        if amount == inventory[str(adding_to_basket1)][0] or amount <= inventory[str(adding_to_basket1)][0]:
            basket[user][adding_to_basket1]=int(amount)
            print"Going back to main menu..."
            menu()
            break
        #     when amount equal or less than it will add the item to the basket which we created.
        else:
            while True:
                if amount > inventory[str(adding_to_basket1)][0]:
                    print "Sorry! The amount exceeds the limit, Please try again with smaller amount"
                    amount= int(raw_input("Amount (Enter 0 for main menu):"))
                else:
                    break

def basket_sub_menu():
    print "Please choose an option:"
    print "1.Update amount"
    print "2.Remove an item"
    print "3.Check out"
    print "4.Go back to main menu"
    selection_sub =input("Your selection:")
    if selection_sub == 1:
        update()
    elif selection_sub == 2:
        remove_basket()
        see_basket()
    elif selection_sub == 3:
        print "Processing your receipt..."
        print "******* Sehir Online Market **************"
        print "****************************************** "
        print       "44 44 0 34"
        print      "sehir.edu.tr"
        print " ------------------------------------------"
        totallist = []
        for i in basket[user]:
            price = inventory[i][1]
            amount = basket[user][i]
            total_price = price * int(amount)
            totallist.append(total_price)
            print  i, "price=", price, "amount=", amount, "total=", total_price
            inventory[i][0]=inventory[i][0]-basket[user][i]
        #     we used data time import to get real time and date, and we decreased here the amounts of items that we choosed from invetory.

        print "------------------------------------"
        print "TOTAL", sum(totallist),"$"
        print "------------------------------------"
        now = datetime.datetime.now()
        print  now.strftime("%Y-%m-%d %H:%M")
        print "Thank You for using our Market!"

    else:
         if selection_sub == 4:
            menu()

def see_basket():
    global count1,basket_cont,price,amount,total_price,totallist
    basket_cont=[]
    totallist=[]
    count1= 1
    print "Your basket contains:"
    # amount_selected=basket[user][adding_to_basket1] = amount
    for i in basket[user]:
        price = inventory[i][1]
        amount=basket[user][i]
        total_price= price*int(amount)
        totallist.append(total_price)
        basket_cont.append(i)
        print str(count1),i,"price=",price,"amount=",amount,"total=",total_price
        count1+= 1
    basket_sub_menu()
def update():
    global user,basket,basket_cont, inventory,new_amount
    select_item = int(raw_input("Please select which item to change its amount:"))
    new_amount = int(raw_input("Please enter new amount: "))
    while select_item>len(basket_cont):
         select_item = int(raw_input("Please select which item to change its amount:"))
         new_amount = int(raw_input("Please enter new amount: "))
    sel = basket_cont[select_item - 1]
    inventory[sel][0] = inventory[sel][0] + basket[user][sel]
    while True:
        if new_amount == inventory[str(sel)][0] or new_amount <= inventory[str(sel)][0]:
            basket[user][sel]= basket[user][sel]+ new_amount
            print"Going back to main menu..."
            see_basket()
            basket_sub_menu()
            break
        else:
            while True:
                if new_amount > inventory[str(sel)][0]:
                    print "Sorry! The amount exceeds the limit, Please try again with smaller amount"
                    new_amount= int(raw_input("Amount (Enter 0 for main menu):"))
                if new_amount == 0:
                        menu()
                else:
                    break
def remove_basket():
    global user, basket, basket_cont, inventory
    select_item = int(raw_input("Please select which item to remove:"))
    sel = basket_cont[select_item - 1]
    del basket[user][sel]
    see_basket()
    basket_sub_menu()

def menu():
    print "Please choose one of the following services:"
    print "1. Search for a product"
    print "2. See Basket"
    print "3. Check Out"
    print "4. Logout"
    print "5. Exit"
    selection = int(raw_input("Your choice:"))
    while selection > 5:
           menu()
    if selection == 1:
        selecting()
    elif selection == 2:
        see_basket()
    elif selection == 3:
        print "Processing your receipt..."
        print "******* Sehir Online Market ********"
        print  "************************************ "
        print       "44 44 0 34"
        print      "sehir.edu.tr"
        print " ------------------------------------"
        totallist = []
        for i in basket[user]:
            price = inventory[i][1]
            amount = basket[user][i]
            total_price = price * int(amount)
            totallist.append(total_price)
            print  i, "price=", price, "amount=", amount, "total=", total_price
            inventory[i][0]=inventory[i][0]-basket[user][i]
        print "------------------------------------"
        print "TOTAL", sum(totallist),"$"
        # we created the totallist list to put the all prices and we used "sum" code to sum the all prices.
        print "------------------------------------"
        now = datetime.datetime.now()
        print  now.strftime("%Y-%m-%d %H:%M")
        print "Thank You for using our Market!"



    elif selection == 4:
        logging_system()
        menu()
    elif selection == 5:
        print
        exit()
#         we used exit code exit from the system
menu()
