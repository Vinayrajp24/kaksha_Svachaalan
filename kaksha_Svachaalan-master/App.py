mail_address = ''#put your mail address here
password = ''#put you password here
import os
import sys
os.path.dirname(sys.executable)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase
from plyer import notification
import pyautogui
import pyttsx3
import datetime
import datetime
from datetime import datetime
import speech_recognition as sr
import firebase_admin
from textblob import TextBlob
from win10toast import ToastNotifier
engine = pyttsx3.init('sapi5')
import time
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
name_to_be_searched="David"
toaster =ToastNotifier()
z=1
def firebase1():
    fb = firebase.FirebaseApplication("https://kaksha-svachaalan-default-rtdb.firebaseio.com/", None)
    result = fb.put("","LED_STATUS","ON")
    print(result)
def firebase2():
    fb = firebase.FirebaseApplication("https://kaksha-svachaalan-default-rtdb.firebaseio.com/", None)
    result = fb.put("","LED_STATUS","OFF")
    print(result)
def notifier():
        print(44444444444)
        toaster.show_toast("APP","Hey!your name has been taken in class",duration=10)
        firebase1()
        sleep(10)
        firebase2()
def screenshot(browser,date1):
    
    str1=date1+"/str.png"
    print(str1)
    browser.save_screenshot(str1)
    image = Image.open(str1)
    image.show()
    return
def sentiment():
    with open('C:/Users/prave/Desktop/kaksha_Svachaalan/guru00.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
    blob= TextBlob(data)
    senti=blob.sentiment
    print(data)
    print(senti[0])
    if senti[0]<(0):
        with open('sentiment_check.txt', 'w') as f:
            f.write('Strong words were used in the class.Please look into thee issue')
    else:
        with open('sentiment_check.txt', 'w') as f:
            f.write('Strong words were not used in the class.')

def takeCommand(browser,date1):
    now1=datetime.now()
    t_string=now1.strftime("%H:%M")
    print(date1)
    last_time="";
    p=1
    if(t_string[0]=='0'):
        if(t_string[1]=='9'):
            last_time="10"+":"+t_string[3]+t_string[4]
        else:
            last_time="0"+str(int(t_string[1])+1)+":"+t_string[3]+t_string[4]
    elif(t_string[0]=='1'):
        if(t_string[1]=='9'):
            last_time="20"+":"+t_string[3]+t_string[4]
        else:
            last_time="1"+str(int(t_string[1])+1)+":"+t_string[3]+t_string[4]
    else:
        if(t_string[1]=='4'):
            last_time="00"+":"+t_string[3]+t_string[4]
        else:
            last_time="2"+str(int(t_string[1])+1)+":"+t_string[3]+t_string[4]
    # if(t_string[4]=='9'):
    #     last_time=t_string[0]+t_string[1]+':'+str(int(t_string[2])+1)+'0'
    # else:
    #     last_time=t_string[0]+t_string[1]+':'+t_string[3]+str(int(t_string[4])+1)
    while t_string!=last_time:  
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening")
            r.energy_threshold=100
            r.pause_threshold = 0.6
            audio = r.listen(source)   
            try:
                print("recognising...")
                print(55555555555)
                query = r.recognize_google(audio,language='en-in')
                print(type(query))
                if name_to_be_searched in query:
                   notifier()
                print("user said:",query)
                print(p)
                if p%6==0:
                    screenshot(browser,date1)
                f=open("NOTES_TEXT/"+date1+".txt","a+")
                f.write(query+" ")
            except Exception as e:
                print("say that again please...")
            if os.path.isfile(date1+"/str.png"):
                dt = str(p)
                print(dt)
                newname =str(date1)+'/img'+dt+'.png'
                os.rename(str(date1)+ "/str.png",newname)
            p=p+1
            now1=datetime.now()
            t_string=now1.strftime("%H:%M")
    return None
def web_automation(meetlink,date1):
    global z
    PATH="C:\Program Files (x86)\chromedriver.exe"
    # this is tested on Firefox or you can use "webdriver.Chrome()"
    browser = webdriver.Chrome(PATH)
    browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    browser.find_element_by_name("identifier").send_keys(mail_address)
    browser.find_element_by_class_name("VfPpkd-vQzf8d").click()
    sleep(5)
    browser.find_element_by_class_name("whsOnd").send_keys(password)
    browser.find_element_by_class_name("VfPpkd-vQzf8d").click()
    sleep(2)
    browser.get(meetlink)
    sleep(2) 
    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER).perform()
    print(55555555555)
    print(55555555555)
    sleep(2)
    browser.find_element_by_class_name("NPEfkd").click()
    sleep(10)
    takeCommand(browser,date1)
    actions.send_keys(Keys.TAB).perform()
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(10)
    browser.close()
    sentiment()
    if os.path.isfile('NOTES_TEXT/guru00.txt'):
        dt = str(z)
        z=z+1
        print(dt)
        newname =r'notes'+dt+'.txt'
        os.rename(r"NOTES_TEXT/guru00.txt",newname)
    return None
meet_link=['','']#meet-link list..edit the list to customize
def start():
    for _ in range(N):#N=no.of meeting you want to join
        now=datetime.now()
        t_string=now.strftime("%H:%M")
        last_time="0"+str(int(t_string[1])+1)+":"+t_string[3]+t_string[4]
        print(last_time)
        print(t_string)
        firebase1()
        sleep(20)
        firebase2()
        sleep(20)
        #if t_string=='19:26':
        now1=datetime.now()
        date1=now1.strftime("%m%d%y%H%M")
        path=date1
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directiories %s failed",path)
        else:
            print("SUCCESS")
        web_automation(meet_link[_],date1)      
if __name__=="__main__":
    start()
    ##print(str)
    ##start()