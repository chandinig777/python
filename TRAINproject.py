import datetime  #importing time module
import random #random to take random pnr numbers
list_of_trains={"chennai_express":'1234',"eastcoast_express":'5678',"narsapur_express":'9102',"krishna_express":'3456'}
print(list_of_trains)
name=input("Enter your name:")
age=int(input("Enter your age:"))
gender=input("Enter your gender:")
train=input("Enter required Train:")
for k,v in list_of_trains.items():
    print("trainname:",k,"trainnum:",v)
ticketrate={"chennai_express":350,"eastcoast_express":280,"narsapur_express":350,"krishna_express":250}


for t,r in ticketrate.items():
    print("select_train:",t,"ticketrates:",r)
pas=int(input("enter num of passengers:"))
if train in ticketrate:
    print1=(("train_rate:",int(ticketrate[train])))
    price=(int(ticketrate[train])*pas)
    print(price)

    user_date=int(input("Enter your reservation date:"))
    date=datetime.datetime(2023,6,user_date)
    print("your reservation date:",date)
    print("your ticket was reserverd:",datetime.datetime.now())
    seat=input("select_seattype:")
    class Train():
        def __init__(self ,train_num,select_seat, source, destination,seats,):
            self.train_num = train_num
            self.select_seat = select_seat
            self.source = source
            self.destination = destination
            self.seats = seats
        def display_info(self):
            print("Train number:",self.train_num)
            print("Select_seat:",self.select_seat)
            print("Source:",self.source)
            print("Destination:",self.destination)
            print("Seat_availability:",self.seats)
            print()  #lines breaks for each trian info displays
    tr=Train('1234',"AC","hyd","vij",3)
    print(25*"__","WELCOME TO IRCTC",25*"__")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Trainname:",train)
    print(70*" ","PNRNO:",random.randint(11111,100000))
    print(70*" ","Reservationdate:",date)
    tr.display_info()
    print(70*" ","number of passengers:",pas,"TOTALFARE:",price)
    print(70*" ","TOTALFARE:",price)
    print(25*"--","HAPPY_JOURNEY",25*"--")









            


    

