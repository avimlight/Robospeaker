import os
if __name__=="__main__":

    print("Welcome ")
    while(True):
        x=input("Enter what you want me to speak: ")
        if x=="q":
             break
        command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
        os.system(command)





