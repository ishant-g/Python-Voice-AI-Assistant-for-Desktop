import pyttsx3
import os
import bs4, requests, datetime, webbrowser, GoogleNews
import speech_recognition as sr
import random
import datetime
import time
import colorama  # Import colorama module for cross-platform colored output
from colorama import Fore
from pyautogui import *
import pywhatkit as kit # pip install pywhatkit -> cmd
import speedtest # pip install speedtest-cli -> cmd
import wikipedia
import pyjokes  # Import the pyjokes library


engine = pyttsx3.init('sapi5')
vocies = engine.getProperty('voices')
print(vocies[0].id)
engine.setProperty('voices',vocies[0].id)

def speak(audio):
    engine.setProperty("rate", 200)
    print("")
    engine.say(audio)
    print("")
    engine.runAndWait()

def takecommand():
    command1 = sr.Recognizer()
    standby_count = 0  # Counter for standby mode
    standby_threshold = 3  # Number of times to repeat "I didn't understand" before standby

    with sr.Microphone() as source:
        print("")
        print('Listening......')
        print("")
        command1.pause_threshold = 0.5
        audio = command1.listen(source,phrase_time_limit=4)

        try:
            print("")
            print('recognizing......')
            command = command1.recognize_google(audio,language='en-in')
            print(f"usersaid:{command}\n")
            return command

        except Exception as e:
            print(e)
            standby_count += 1
            if standby_count >= standby_threshold:
                standby_count = 0  # Reset standby count
                speak("I didn't understand anything. Entering standby mode.")
                time.sleep(2)  # Give a short pause before entering standby
                standby_mode()

            print("say that again please....")
            return ""

def standby_mode():
    standby_name = "Speedy"  # Replace with the wake word or name you want
    command1 = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            command1.pause_threshold = 0.5
            audio = command1.listen(source,phrase_time_limit=2)

            try:
                print("Recognizing wake word...")
                wake_word = command1.recognize_google(audio, language='en-in')
                print(f"Wake word said: {wake_word}\n")

                if standby_name.lower() in wake_word.lower():
                    return
            except Exception as e:
                print(e)
       
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak("Good Mornig!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")

    speak("Hello! I am Speedy in your service. How can I help you?")

# Program execution


def close_program(program_name):
    try:
        os.system(f"taskkill /im {program_name}.exe /f")
        speak(f"{program_name} is closed.")
    except Exception as e:
        speak("there is error cant close the program")

def continue_after_break():
    colorama.init(autoreset=True)  # Initialize colorama for cross-platform colored output
    
    speak("Do you want to continue? (yes/no): ")
    response = takecommand().lower()
    if response == "no":
        speak("Okay, taking a break. For how many minutes would you like to pause?")
        break_time = int(takecommand())
        remaining_time = break_time * 60
        speak(f"Sure! I'll be back after {break_time} minutes. Take your time!")

        while remaining_time > 0:
            # Provide reminder during the last 1 minute and 10 seconds
            if remaining_time == 70:
                speak("Just 1 minute and 10 seconds left.")

            # Change color to red during the last 10 seconds
            if remaining_time == 10:
                speak("Only 10 seconds remaining. Get ready to resume!")

            time.sleep(1)  # Sleep for 1 second
            remaining_time -= 1
            
        speak("Break time is over. I'm back!")
        return True
        
    elif "yes" in response  or "continue" in response:
        return True
    elif "close" in response:
        speak("Okay! Closing the program. See you next time.")
        return False
    else:
        speak("Sorry, I didn't understand that. Do you want to continue? (yes/no): ")
        return continue_after_break()

#main function
    

wishme()
while True:
    command = takecommand().lower()

    # Check if the command contains the word 'open'
    if "open" in command:
        command = command.replace("open","")
        press("win")
        sleep(.2)
        typewrite(command)
        sleep(.2)
        press("enter")
        standby_mode()

    elif "game" in command or "play game" in command or "play a game" in command:
        speak("great! i have 3 Games for you Would you like to play")
        print("great! i have 3 Games for you Would you like to play")

        while True:

            ak=takecommand()
            
            if "yes" in ak:

                    speak("again great! What would you like to play Snake Water Gun, guess the Number or prices less KBC")
                    print("What would you like to play"
                            "Snake Water Gun"
                            "guess the Number"
                            "prices less K.B.C")
                    gm=takecommand().lower()
                    
                    if "snake" in gm or "water" in gm or "gun" in gm:
                        os.system(f"start vswg.py")
                        standby_mode()

                    elif "guess" in gm or "number" in gm:
                        os.system(f"start guno.py")
                        standby_mode()

                    elif"kbc" in gm or "quize" in gm:
                        os.system(f"start kbc.py")
                        standby_mode()

                    else:
                        speak(" i didn't understan speak again pls")
                        print(" i didn't understan speak again pls")
                        ak="yes"

            elif "no" in ak:
                speak("no problem")
                print("no problem")
                break
            else:
                speak(" i didn't understan speak again pls")
                print(" i didn't understan speak again pls")
                command="game"

    elif "intro" in command or "introduction" in command or "intradus" in command:
        print("Welcome to Speedy - Your Smart AI Assistant!")

        # Introduction
        speak("Hey there, I'm Speedy, your trusty AI companion, here to make your digital life a breeze!")
        print("Hey there, I'm Speedy, your trusty AI companion, here to make your digital life a breeze!")

        speak(" i know you hsve many quetions for me like what i am? no! you know what i am what i can do!,how i work!, what is A I!,why my name speedy! etc")

        speak("What I Can Do!")
        print("What I Can Do")
        speak("I can open programs, search the internet, open sites, and offer three entertaining games")
        print("I can open programs, search the internet, open sites, and offer three entertaining games")

        #Closing
        speak("So, buckle up, as we embark on this AI-driven journey together. Ready for the future? Let's make it happen, one command at a time!")

    elif "joke" in command:
        speak(pyjokes.get_joke())  # Use pyjokes to get a random joke

    elif "guess" in command or "number" in command:
        os.system(f"start guno.py")
        standby_mode()

    elif"kbc" in command or "quize" in command:
        os.system(f"start kbc.py")
        standby_mode()

    elif "snake" in command or "water" in command or "gun" in command:
        os.system(f"start vswg.py")
        standby_mode()
      
    elif "close" in command:
        # Split the command to extract the program name
        parts = command.split(" ")
        if len(parts) > 1:
            program_name = parts[1]
            if program_name == "mycomputer":
                close_program(r"C:\Windows\explorer.exe")
            elif program_name == "paint":
                close_program(r"C:\Windows\System32\mspaint.exe")
            else:
                close_program(program_name)
        else:
            speak("Program ka naam nahi mila.")
    elif "exit" in command or "bye" in command:
        speak("Alwida! See you next time.")
        break  # Exit the loop and end the program
    elif "exhausted" in command or "tired" in command or "break" in command:
        if not continue_after_break():
            break

    elif "time" in command:
            # time = datetime.datetime.now().strftime("%H:%M:%S %p") # 24 hour format
            time = datetime.datetime.now().strftime("%I:%M:%S %p") # 12 hour format
            speak(time)

    elif "date" in command:
            date = datetime.datetime.now().strftime("%D")
            speak(date)
    elif "day" in command:
            day = datetime.datetime.now().strftime("%A")
            speak(day)

    elif "temperature" in command:
            q = command
            r = requests.get(f"https://www.google.com/search?q={q}")
            data = bs4.BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"the temperature outside is {temp}")
            print(f"the temperature outside is {temp}")
            
            speak("do you want another place temperature")
            place = takecommand()
            if "yes" in place or  "temperature" in place or "ya" in place:
                speak("tell me the name of the place")
                next = takecommand()
                r = requests.get(f"https://www.google.com/search?q={next}")
                data = bs4.BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"the temperature outside is {temp}")
                print(f"the temperature outside is {temp}")
            else:
                speak("no problem!")

    elif "play" in command: 
            command = command.replace("play ","")
            kit.playonyt(command)
            speak(f"playing {command}")
            print(f"playing {command}")
            standby_mode()

    elif "website" in command: 
        command = command.replace("website","")
        command = command.replace(" ","") 
        webbrowser.open(f"https://www.{command}.com")
        speak(f"opening {command}")
        print(f"opening {command}")
        standby_mode()
        
    elif "search" in command: 
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on the internet.")
        standby_mode()
            
    elif "news of" in command: 
        command = command.replace("news of ","")
        new = GoogleNews.GoogleNews()
        speak(f"getting news of {command}")
        print(f"getting news of {command}")
        new.get_news(command)
        new.result()
        a = new.gettext()
        speak(a[1:5])
        print(a[1:5])
        
    elif "headlines" in command or "headline" in command: 
        new = GoogleNews.GoogleNews()
        speak("getting fresh headlines")
        print("getting fresh headlines")
        new.get_news("headlines")
        new.result()
        a = new.gettext()
        speak(a[1:10])
        print(a[1:10])
    elif "speed test" in command or "test speed" in command:
        speed = speedtest.Speedtest()
        speak("checking")
        print("checking")
        ul = speed.upload()
        ul = int(ul/800000)
        dl = speed.download()
        dl = int(dl/800000)
        speak(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")
        print(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")

    elif "standby mode" in command or "standby" in command:
        standby_mode()

    elif'wikipedia' in command or "tell about" in command:
        command=command.replace("wikipedia","") 
        results =  wikipedia.summary(command,sentences=2)
        print(results)
        speak(results)
        standby_mode()

    elif command != "bey":
        speak(chr.get_response(command))
        print(chr.get_response(command))        
    

    # Randomly choose a message instead of always asking "Anything else?"
    random_messages = [
        "Hope my assistance was helpful!","","","","","","",
        "Feel free to ask for more assistance.","","","","","","",
        "Is there anything else I can do for you?","","","","","","",
        "I hope you are enjoying our interaction.","","","","","","",
        "If you have any more questions, feel free to ask.""","","","","","",
    ]
    random_message = random.choice(random_messages)
    
    speak(random_message)

    
