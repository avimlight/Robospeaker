import os

if __name__=="main":
    print("welcome to robospeaker")
    while True:
        x=int(input("enter what u want to speak"))
        if x.lower()=="q":
            os.system("say 'bye bye'")
            break
        else:
            y=f"say {x}"
            os.system(y)
