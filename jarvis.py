import speech_recognition as sr
import pyttsx3
import subprocess
import pywhatkit as kit
import webbrowser
import pyjokes
import datetime
import wikipedia
import os


# creating speech engine for pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


# creating the speak funcion to speak any text giving


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = 3000
        print("listening...")
        audio = r.listen(source)
        command = " "

        try:
            command = r.recognize_google(audio)
            print(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("network error")

    return command.lower()


def play_youtube():
    try:
        speak("what should i play")
        search = take_command()
        kit.playonyt(search)
        speak("playing" + search)

    except kit.InternetException:
        pass

def search_browser():
    try:
        speak("what should i search")
        openbws = take_command()
        kit.search(openbws)
        speak("searching" + openbws)

    except kit.InternetException:
        pass

def location():
    speak("what is the name of the location")
    locate = take_command()
    url = 'google.com/maps/place/' + locate
    webbrowser.open(url)
    speak("This what i found for " + locate)

def wiki():
    try:
        speak("what should i search on wikipedia")
        wiki_s = take_command()
        result = wikipedia.summary(wiki_s, sentences=3)
        speak("This is what i found on wikipedia")
        speak(result)
    except wikipedia.PageError:
        speak("i can't found the page on wikipedia")


def weather():
    speak("opening the weather website")
    url = 'openweathermap.org/city'
    webbrowser.open(url)
    speak(" the weather website is opened ")

def play_music():
    songs_dir = "c:/Users/USER/Music"
    speak('opening music')
    song = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, song[0]))

def play_video():
    video_dir = "c:/Users/USER/Videos"
    speak('opening video')
    video = os.listdir(video_dir)
    os.startfile(os.path.join(video_dir, video[0]))

def open_microsoft_word():
    word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
    speak('opening microsoft word')
    os.startfile(word)

def open_excel():
    excel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    speak('opening microsoft excel')
    os.startfile(excel)

def open_opera():
    opera = "C:\\Users\\user\\AppData\\Local\\Programs\\Opera\\launcher.exe"
    speak('opening opera mini')
    os.startfile(opera)

def make_note(data):
    date = datetime.datetime.now()
    file_name =str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(data)

    subprocess.Popen(["notepad.exe", file_name])

greet = "good day, how can i help you"
speak(greet)

cmd = ["hi siri","siri"]
for phrase in cmd:
    WAKE = phrase

while True:
    query = take_command()
    if query.count(WAKE) > 0:
        speak("am listening")

        query = take_command()

        if "what is your name" in query:
            speak("my name is siri")

        elif 'play video' in query:
            play_video()

        elif "play music" in query:
            play_music()

        joke_str = ["tell a joke", "joke"]
        for words in joke_str:
            if words in query:
                joke = pyjokes.get_joke("en")
                print(joke)
                speak(joke)

        you_str = ["open on youtube", "play on youtube", "get on youtube"]
        for words in you_str:
            if words in query:
                play_youtube()

        time_str = ["what is the time", " time ", "tell me the time"]
        for words in time_str:
            if words in query:

                speak("getting the time ")
                my_time = datetime.datetime.now().strftime('%I:%M %p')
                speak("the current time is" + my_time)

        brow_str = ["search", " browse", "search on browser"]
        for words in brow_str:
            if words in query:
                search_browser()

        locate_str = ["find location", " location ", "get location"]
        for words in locate_str:
            if words in query:
                location()

        wiki_str = ["wikipedia", " get on wikipedia ", "open on wikipedia"]
        for words in wiki_str:
            if words in query:
                wiki()

        wea_str = ["what is the weather", " get weather ", "weather"]
        for words in wea_str:
            if words in query:
                weather()

        word_str = ["open microsoft word", " microsoft word ", "word"]
        for words in word_str:
            if words in query:
                open_microsoft_word()

        excel_str = ["open microsoft excel", " microsoft excel ", "excel"]
        for words in excel_str:
            if words in query:
                open_excel()

        opera_str = ["open opera mini", "search opera mini", "opera mini"]
        for words in opera_str:
            if words in query:
                open_opera()

        note_str = ["make a note", "take note", "write a note"]
        for words in note_str:
            if words in query:

                speak("what should i write down")
                note_data = take_command()
                make_note(note_data)
                speak("i have write down the note")



