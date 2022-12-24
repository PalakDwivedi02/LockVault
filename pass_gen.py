import random
import string

alpha_lower="abcdefghijklmnopqrstuvwxyz"

alpha_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers="123456789012345678901234567890"

symbols="!@#$%^&*-_+!@#$%^&*-_+!@#$%^&*-_+"

length=16

str=alpha_lower+numbers+alpha_upper+symbols

ch="".join(random.sample(str,length))

print(ch)
f=open("Names.csv","a")
f.write("\n"+ch)
#f.truncate(0)
f.close()
f=open("Names.csv","r")
print(f.read())
