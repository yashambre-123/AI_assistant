import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import pywhatkit as kit
import os
import smtplib
from email.message import EmailMessage
import pywhatkit as whatsapp
import requests
from newsapi import NewsApiClient
import random
import serial

ser=serial.Serial('COM6',9600)
computer=pyttsx3.init('sapi5') # sapi5 is the microsoft speech api . This computer will only speak with us
voices=computer.getProperty('voices') # we get the list of voices [boy voice,girl voice]
#print(voices[1].id) we get the women voice
#print(voices[0].id) we get the men voice
computer.setProperty('voice',voices[1].id) # here we set the voice , either of a girl or a boy

def speak(audio): # by this function,we can make the computer to speak
    computer.say(audio)
    computer.runAndWait()

def wishme():
    time=int(datetime.datetime.now().hour) # by this , the time variable , will get to know the time(time at which we are compiling) automatically
    if time==0:
        speak("its midnight,good night,sir")
    elif time>0 and time<6:
        speak("Its early morning,sir.i wish you will have a good sleep")
    elif time>6 and time<12:
        speak("good morning,sir")
    elif time>=12 and time<17:
        speak("good afternoon,sir")
    elif time>=17 and time<19:
        speak("good evening,sir")
    elif time>=19 and time<24:
        speak("good night,sir")
    speak("hello sir,i am siri , and i am your personal  artificial intilligence companion . how may i help you")

def roll():
    speak("ok sir,rolling a die for you")
    die=['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll=(f"{roll[0]}") # this will contain the rolled value
    speak(f"i rolled a die and i got {roll}")

def take_command():
    listener=sr.Recognizer() # will recognize what you are saying
    try:
        with sr.Microphone() as source:
            print("listening.....") # first it will print this
            voice=listener.listen(source) # it will listen to the source
            querry=listener.recognize_google(voice) # this is the mike , we should speak to this only
            print("user said:",querry)
    except Exception as e: # if not said , then the computer willl say this
        print("say that again sir")
        return "None"
    return querry
def get_news():
    newsapi=NewsApiClient(api_key='78ca950f2ce04d3798e5329ee6d12eba')
    speak("on what topic do you want the news,sir")
    topic=take_command()
    data=newsapi.get_top_headlines(q=topic,
                                   language='en',
                                   page_size=5)
    newsdata=data['articles'] # the data will be stored in the news_data
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("that's it for today,i will update you tommorow for new news")

def send_whatsapp(phone_number,message,hour,minute):
    whatsapp.sendwhatmsg(phone_number, message, hour, minute)

def email(reciever,subject,content):
    email=EmailMessage()
    email['from']='' # type your name here in the single quotes
    email['to']=reciever
    email['subject']=subject
    email.set_content(content)
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as server:
        server.ehlo()
        server.starttls()
        server.login('','') # type your mail id in the first single quotes, and type your mail account's password in the second single quotes
        server.send_message(email)
        server.close()

if __name__=="__main__":
    wishme()
    while True:
        querry=take_command().lower()
        if 'wikipedia' in querry:
            speak("searching wikipedia.....")
            querry=querry.replace("wikipedia","")
            results=wikipedia.summary(querry,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in querry:
            speak("searching youtube.com,sir....")
            webbrowser.open("youtube.com")
        elif 'chennai' in querry:
            speak("opening vit chennai in google...")
            webbrowser.open("https://vtopcc.vit.ac.in/vtop/initialProcess")
        elif 'open google' in querry:
            speak("searching google.com,sir.....")
            webbrowser.open("google.com")
        elif 'zack knight 2' in querry:
            speak("searching zack knight adhura remix")
            webbrowser.open("https://www.youtube.com/watch?v=qw9l1R3Uc-4")
        elif 'open udemy' in querry:
            speak("searching udemy.com,sir....")
            webbrowser.open("udemy.com")
        elif 'youtube' in querry:
            speak("what should i search on youtube")
            topic=take_command()
            kit.playonyt(topic)
        elif 'roll' in querry:
            roll()
        elif'weather' in querry:
            url='http://api.openweathermap.org/data/2.5/weather?q=mumbai&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd' # this is the weather api
            res=requests.get(url)
            data=res.json() # the res we will get it in the json format
            weather=data['weather'][0]['main']
            temp=data['main']['temp']
            description=data['weather'][0]['description']
            temperature1=round((temp-32)*5/9)
            speak(f'the weather in mumbai is {weather},temperature is {temperature1} degree celsius')
        elif 'date' in querry:
            year=int(datetime.datetime.now().year)
            month=int(datetime.datetime.now().month)
            date=int(datetime.datetime.now().day)
            speak(f"sir,today's date is {date} {month} {year}")
        elif 'send whatsapp message' in querry:
            speak("please say the phone number of the person to whom you need to send the message")
            phone_number=take_command()
            speak("what is the message")
            message=take_command()
            speak("say the hour at which you want to send the message")
            hour=take_command()
            speak("say the minute at which you want to send the messge")
            minute=take_command()
            send_whatsapp(phone_number,message,hour,minute)
        elif 'the time now' in querry:
            the_time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {the_time}")
        elif 'on' in querry:
            ser.write(b'Y')
        elif 'off' in querry:
            ser.write(b'N')
        elif 'open microsoft teams' in querry:
            speak("opening microsoft teams sir.....")
            path='C:\\Users\\acer\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk'
            os.startfile(path)
        elif 'news' in querry:
            get_news()
        elif 'send mail' in querry:
            try:
                reciever='' # type the reciever's email id here in the single quotes
                speak("what is the subject of the mail,sir")
                subject=take_command()
                speak("what is the content for the mail,sir")
                content=take_command()
                email(reciever,subject,content)
                speak("email has been sent,sir")
            except Exception as e:
                print(e)
                speak("sorry,sir email cannot be sent")
        # here are some of the funny comments, which you can remove if you don't want
        elif 'what is your name' in querry:
            speak("my name is siri,sir")
        elif 'are you mental' in querry:
            speak("who are you to say me mental,you idiot")
        elif 'where is your home' in querry:
            speak("my home is in yash laptop")
        elif 'who has made you' in querry:
            speak("i have been created by yash ulhas ambre")
        elif 'why has your owner made you' in querry:
            speak("yash sir has made me because in the future,there will be a good correlation between human beings and AI robots")
        elif 'bye bye siri' in querry:
            speak("bye,it was pleasure interacting with you,sir")
            exit()
















