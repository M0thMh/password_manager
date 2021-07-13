import os
import hashlib
import sqlite3
import getpass
import string
import random
import itertools
import threading
import time
import sys
import datetime



Q = """
    1. Create a Password
    2. Show the Passwords
    
    """



def connect(name, type , password, account, username, url, date):
    try:
        con = sqlite3.connect("DATA.db")
        cur = con.cursor()
    except Exception:
        with open("DATA.db", "+") as f:
            f.close()
        con = sqlite3.connect("DATA.db")
        cur = con.cursor()

    cur.execute("""
                    CREATE TABLE IF NOT EXISTS passwords 
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        Name TEXT NOT NULL, 
                        Type TEXT NOT NULL,
                        Password TEXT NOT NULL, 
                        Account TEXT NOT NULL, 
                        Username TEXT NOT NULL, 
                        URL TEXT NOT NULL,
                        Date TEXT NOT NULL)
                """)    
    
    try:
        cur.execute("INSERT INTO passwords VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", (name, type, password, account, username, url, date))
        con.commit()
        con.close()
        return True
    except Exception:
        return False

    
    













def ANIM(long):
    done = False
    #here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rPlease Wait ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'\rPassword Saved Successfuly!              \n\n\n')

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(int(long))
    done = True


def pASSWORD():
    STRR = str(string.ascii_letters+string.digits+string.punctuation)
    RPassword = ''.join(random.choices(STRR , k = 100))
    PASSS = hashlib.sha256(RPassword.encode()).hexdigest()
    return PASSS




def main():
    os.system("clear")
    print(Q)
    INPUT = int(input("Please Enter The Number of Command or Ctrl + c To Exit: ")) 
    if INPUT == 1:
        NAME = input("Please Enter The Name Of Password: ")
        TYPE = input("Please Enter The Type Of Password: ")
        ACCOUNT = input("Please Enter Your Account: ")
        USERNAME = input("Please Enter Your Username: ")
        URL = input("Please Enter The URL: ")
        while NAME == "" or TYPE == "" or ACCOUNT == "" or USERNAME == "" or URL == "": 
            print("\nPlease Enter All The Information ... \n")
            NAME = input("Please Enter The Name Of Password: ")
            TYPE = input("Please Enter The Type Of Password: ")
            ACCOUNT = input("Please Enter Your Account: ")
            USERNAME = input("Please Enter Your Username: ")
            URL = input("Please Enter The URL: ")
        
        PASSWORD = pASSWORD() 
        DDATE = datetime.datetime.now()
        DATE = DDATE.strftime("%d/%m/%Y %H:%M:%S")
        CONN = connect(NAME, TYPE, PASSWORD, ACCOUNT, USERNAME, URL, DATE)
        if CONN == True:
            print("\n")
            ANIM(3)
            WAIT = input("Prease Enter To Continue ...")
            main()
        else:
            print("Can\'t Save The Information Now, Please Try Again ...")
            exit()

    





if __name__ == '__main__':
    main()