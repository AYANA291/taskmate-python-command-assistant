import webbrowser
import datetime
import pyjokes

print("🧠 TaskMate Started")

while True:
    query = input("Enter command: ").lower()

    if "youtube" in query:
        webbrowser.open("https://youtube.com")
        print("Opening YouTube")

    elif "google" in query:
        webbrowser.open("https://google.com")
        print("Opening Google")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time:", current_time)

    elif "joke" in query:
        print(pyjokes.get_joke())

    elif "exit" in query:
        print("Goodbye 👋")
        break

    else:
        print("Searching on Google...")
        webbrowser.open(f"https://www.google.com/search?q={query}")
