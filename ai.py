#Module Area

import os
import webbrowser
import datetime
import pyjokes
from gnewsclient import gnewsclient
import time



#Define

def help():
    print("AI Version 1.0 Help Desk")
    print("Commands                      Discription")
    print("webapp               Asks for the Link of WebApp and then opens into Web")
    print("jokes                Tells Funny Jokes ")
    print("News                 Get Daily News Based on Your Intrest")


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(" Good Morning ")
     
    if hour>=12 and hour<18:
        print(" Good Afternoon ")
       
    if hour>=18 and hour<24:
        print(" Good Evening ")

print("Welcome to Linux AI ")
       


def open():
    appname= input("App Name : ")
    os.system(appname)

def webapp():
    web= input(" Link : ")
    webbrowser.open(web)

def yrepo():
    webbrowser.open("https://github.com/yatharthgeek")

def news():
    language=input("Language : ")
    location = input("location : ")
    topics = input("Topic : ")
    client = gnewsclient.NewsClient(language=language,
                                location=location,
                                topic=topics,
                                max_results=3)
 
    news_list = client.get_news()
 
    for item in news_list:
        print("Title : ", item['title'])
        print("")
        print("Link : ", item['link'])
        print("")


def timer():
    # define the countdown func.
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        
        print('Time Up !!!!! ')
    
    
    # input time in seconds
    t = input("Enter the time in seconds: ")
    
    # function call
    countdown(int(t))
    

def jokes():
    joke=pyjokes.get_joke(language="en" , category="neutral")
    print(joke)








greeting()









#Bash Area

while True :
        
    entry = input("\nCommand : ")

    #Condition Area

    if "help" in entry :
        help()

    if "webapp" in entry :
        webapp()

    if "news" in entry :
        news()

    if "jokes" in entry :
        jokes()

    if "open" in entry :
        open()

    if "exit" in entry:
        print("Thanks For Using !! ")
        break

    if "timer" in entry :
        timer()

    if "hack time" in entry :
        os.system("sudo apt install hollywood")
        os.system("hollywood")

    if "yrepo" in entry:
        yrepo()
    
