import os
import hashlib
import sqlite3
import getpass
import string
import random


Q = """
    1. Create a Password
    2. Show the Passwords
    """




def Gen():
    INTNUM = random.randint(0,10000000000000000)
    STR    = string.ascii_letters
    PASSWORD = "".join(random.choices(INTNUM, ))





def main():
    os.system("clear")
    print(Q)
    INPUT = int(input("Please Enter The Number of Command:")) 
    if INPUT == 1:




if __name__ == '__main__':
    main()