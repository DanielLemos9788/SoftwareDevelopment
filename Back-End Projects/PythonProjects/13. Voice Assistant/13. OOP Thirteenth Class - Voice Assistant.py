import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Voice Options
voice_id_1 = "com.apple.speech.synthesis.voice.samantha"
voice_id_2 = "com.apple.speech.synthesis.voice.moira"
voice_id_3 = "com.apple.speech.synthesis.voice.monica"
voice_id_4 = "com.apple.speech.synthesis.voice.paulina"

#Function to Make the Voice Assistant Talk
def talk(message):
    #Start the Engine of PYTTSX3
    engine = pyttsx3.init()
    #Set the VOICE ACTOR
    engine.setProperty("voice", voice_id_2)

    #Say the Message
    engine.say(message)
    engine.runAndWait()

#Listen to the Microphone and Convert the Audio to Text
def transform_audio_to_text():
    #Recognizer Variable Creation
    r = sr.Recognizer()
    #Configure the Microphone
    with sr.Microphone() as origin:
        #Waiting time to start hearing
        r.pause_threshold = 0.8
        #Inform the start of the recording
        print("Now You Can Talk")
        #Save the Audio
        audio = r.listen(origin)

        try:
            #Search in Google what the Machine Heard
            request = r.recognize_google(audio, language="eng-us")
            #Test the audio response
            print("You said:" + request)
            #Get the Request
            return request

        #In case of not understanding the audio
        except sr.UnknownValueError:
            #Test the audio
            print("I didn't understand what you said, ¡Please Try Again!")
            #Return Error
            return "Still Waiting"

        #In case of not solving the Request
        except sr.RequestError:
            # Test the audio
            print("The service is NOT working, ¡Please Try Again!")
            # Return Error
            return "Still Waiting"

        #In case of unexpected error
        except:
            # Test the audio
            print("Unexpected Error:Something Went Wrong, ¡Please Try Again!")
            # Return Error
            return "Still Waiting"

#Inform current day of the week
def get_today():
    day = datetime.date.today()
    print(day)
    #Value day of the week
    weekday = day.weekday()
    print(weekday)
    #Dictionary names of the week
    week_calendar = {0:"Monday",
                     1:"Tuesday",
                     2:"Wednesday",
                     3:"Thursday",
                     4:"Friday",
                     5:"Saturday",
                     6:"Sunday"}

    #Say day of week
    talk(f"Today is {week_calendar[weekday]}")

#Inform current hour
def get_current_hour():
    hour = datetime.datetime.now()
    if hour.hour > 12:
        hour = f"And in this moment the time is: {hour.hour} {hour.minute} PM with {hour.second} seconds"
    else:
        hour = f"And in this moment the time is: {hour.hour} {hour.minute} AM with {hour.second} seconds"

    print(hour)
    #Say the time
    talk(hour)

#Initial Greeting
def initial_greeting():
    hour = datetime.datetime.now()

    if hour.hour > 6 and hour.hour <= 24:
        moment = "Good Night"
    elif hour.hour <= 6 and hour.hour > 12:
        moment = "Good Afternoon"
    else:
        moment = "Good Morning"

    #Greet
    talk(f"{moment}, I am Nemesis, your personal assistant. ¡Please tell me what can I do for you today!")

#Central Fuctionality of the Voice Assistant
def assistant_operation():
    # Greet
    initial_greeting()
    #Process variable
    start = True
    #Central Loop
    while start:
        # Activate microphone and get the request in a string variable
        main_request = transform_audio_to_text().upper()

        #Open Youtube on Chrome
        if "OPEN YOUTUBE" in main_request:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            continue
        #Open Google Chrome
        elif "OPEN GOOGLE CHROME" in main_request:
            talk("Heading to your search engine")
            webbrowser.open("https://www.google.com")
            continue
        #Return Name of Current Day
        elif "WHAT DAY IS TODAY" in main_request:
            get_today()
            continue
        #Return Current Hour
        elif "WHAT TIME IS IT" in main_request:
            get_current_hour()
            continue
        #Search on Wikipedia + Reading of the Result
        elif "LOOK ON WIKIPEDIA" in main_request:
            talk("Searching in wikipedia")
            main_request = main_request.replace("WIKIPEDIA", "")
            wikipedia.set_lang("en")
            result = wikipedia.summary(main_request, sentences=1)
            talk(f"I found the following on Wikipedia: {result}")
            continue
        #Search on Google (Simple)
        elif "SEARCH ON GOOGLE" in main_request:
            talk("I'm searching it up")
            main_request = main_request.replace("SEARCH ON GOOGLE", "")
            pywhatkit.search(main_request)
            talk("This is what I found")
            continue
        #Play Music or Videos on YouTube
        elif "PLAY" in main_request:
            talk("I'd play your video my Lord")
            main_request = main_request.replace("PLAY", "")
            pywhatkit.playonyt(main_request)
            continue
        #Make a Random Joke
        elif "JOKE" in main_request:
            talk(pyjokes.get_joke("en", "all"))
            continue
        #Look for the Stock Price and Market Value of Public Traded Companies
        elif "STOCK PRICE OF" in main_request:
            stock = main_request.split("OF")[-1].strip()
            stock_name_dic = {"apple":"APPL",
                          "amazon":"AMZN",
                          "google":"GOOGL",
                          "tesla":"TSLA"}
            try:
                search_stock = stock_name_dic[stock]
                search_stock = yf.Ticker(search_stock)
                current_price = search_stock.info("regularMarketPrice")
                market_value = search_stock.info("MarketValue")
                talk(f"The price of {stock} is {current_price} dollars,"
                     f"and the current market value is {market_value}")
                continue
            except:
                talk("Pardon me, I was not able to find the stock you were looking for")
                continue
        #Turn Off Nemesis
        elif "GO TO SLEEP" in main_request:
            talk("I'm going to sleep, ¡Take Care Darling!")
            break

        talk("Do you want something else today?")

#Nemesis Process
assistant_operation()








