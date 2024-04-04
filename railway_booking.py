""""
1.train PNR
2.LOGIN
3.SOURCE -DESTINATION
4.SEATS AVAILABILTY
5.DATE AND TIME
6.PRICE
7.USER DETAILS -NAME, MOBILE, ADDRESS
"""
s = """
1.user details
2.source and Destination
3.Train number and seats availability
4.price
5.Book ticket
6.PNR Generate
"""
import random
import sys
import pickle
trains = {("Lingampally","hyd") : [{"Vikarabad":545,"shankerpally":446,"nagulapally":879}],
          
          ("secundrabad","hyd"):[{"Hubbali" : 1234,"Bidar" : 5678}]}
users = {"prasad": 123,"vara" : 567}
user_details = []
user  =input("enter user name : ")
if user in users.keys():
    password = int(input("enter the password : "))
    if password == users[user]:
        print(s)
        option = int(input("enter your option : "))
        if option == 1:
            mobile = int(input("enter your mobile number : "))
            age = int(input("enter your age : "))
            gender = input("enter your gender : ")
            l = [user,mobile,age,gender]
            user_details.append(l)
            print(user_details)
        elif option  ==2 :
            source = input("enter your source : ")  
            destination = input("enter your destination : ")
            print("Available trains : \n") 
            for i in trains:
                if source in trains:
                    if destination in ("Lingampally","hyd"):
                        print(trains[("Lingampaly","hyd")])
                        break
                elif source in ("secundrabad","hyd"):
                    if destination in ("secundrabad","hyd"):
                        print(trains[("secundrabad","hyd")])
                        break
                else :
                    print("No trains available ! ")   
                    break 

            
    else :
        print("Invalid password !")    
else :
    print("enter valid user name!")


       
