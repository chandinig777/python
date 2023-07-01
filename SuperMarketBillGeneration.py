from datetime import datetime

Name=input("Enter the Name:")
#list of items
list='''
      rice            Rs  50/kg
      sugar           Rs  20/kg
      oil             Rs  150/liter
      boost           Rs  80/kg
      salt            Rs  30/kg
      biscuits        Rs  10/packet
      moongdal        Rs  110/kg
      sooji           Rs  60/kg
'''

#declaration
#list of price
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0 
ilist=[]
qlist=[]
plist=[]

 #rates for items
items={'rice':50,
       'sugar':20,
       'oil':150,
       'boost':80,
       'salt':30,
       'biscuits':10,
       'moongdal':110,
       'sooji':60}
option=int(input("for list of items press 1 or 2 for exit"))   #select the items list
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items: ")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))    #for multiple items take it in tuple
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
        else:
           print("sorry you entered item is not available")
else:
       print("you entered wrong number")
inp=input("can i bill the item yes or no:")
if inp=='yes':
       pass
       if finalamount!=0:
          print(25*"=","Princy Super Market",25*"=")
          print(28*" " , "kukatpally")
          print("Name:",Name,30*" ","Date: ",datetime.now())
          print(75*"-")
          print("s.no",10*' ','items',3*' ',12*' ','quantity',13*' ','price')
          for i in range(len(pricelist)):
               print(i,8*' ',3*' ',ilist[i],12*' ',12*' ',qlist[i],12*' ',plist[i])
          print(75*"-")
          print(50*" ",'totalamount:','Rs',totalprice)
          print('gst amount',40*" ",'Rs',gst)
          print(75*"-")
          print(50*" ",'finalamount:','Rs',finalamount)
          print(75*"-")
          print(20*" ",'Thanks for visiting!')
          print(75*"-")
       else:
          print("Done")
else:
       print("Done")


    


