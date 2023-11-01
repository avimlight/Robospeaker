import os
if __name__=="__main__":
    x=input("enter what do you want to prononunce")
    command=f"say{x}"
    os.system(command)