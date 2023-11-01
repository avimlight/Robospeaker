import os
import pyttsx3  # Import the pyttsx3 library

if __name__ == "__main__":
    print('Welcome t Robo speaker')

    while True:

        x = input("Enter what you want to me speak: ")
        if x.lower() == "q":
            print("session end")
            break
        else:
            start = pyttsx3.init()

            start.say(x)
            start.runAndWait()