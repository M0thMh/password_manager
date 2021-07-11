import random
import string


'''
for i in range(10):
    r = random.randint(0,100000000000000000000)
    print(r)


'''    


#INTNUM = for i in range(1):random.randint(0,10000000000000000)

#INTNUM = random.randint(0,100000000000000000000)
INTNUM = string.printable

#sTR = "".join(random.choices(INTNUM) for i in range(10))

#print(sTR)


INTNUM = random.randint(0, 10000000000000000)
STR = string.ascii_letters
PASSWORD = "".join(random.choices(INTNUM, STR))

print(PASSWORD)
