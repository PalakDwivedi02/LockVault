import random
import string
import csv
import os

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789012345678901234567890"
symbols = "!@#$%^&*-_+!@#$%^&*-_+!@#$%^&*-_+"
length = 16

def generate_password():
    #with open("pws.csv", "a") as file:
    str = alpha_lower+numbers+alpha_upper+symbols
    ch = "".join(random.sample(str, length))
    #file.write("\n"+ch)
    # f.truncate(0)
    return ch

def read_password(site):
    with open("pws.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Site"]
            if name == site:
                return row["Password"]
        print("Password not found!")
        return ""

def write_password(site, password):
    with open("pws.csv", "a") as file:
        file.write(f"\n{site},{password}")

def delete_password(site): #not working (WIP)
    with open("pws.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Site"]
            if name == site:
                with open("pws.csv", "r+") as file:
                    d = file.readlines()
                    file.seek(0)
                    for i in d:
                        if i != row:
                            file.write(i)
                    file.truncate()
                return
    print("Password not found")

def update_password(site, password):
    with open("pws.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Site"]
            if name == site:
                with open("pws.csv", "r+") as file:
                    inst = file.readlines()
                    file.seek(0)
                    for i in inst:
                        if i != row:
                            file.write(i)
                        else:
                            file.write(f"\n{site},{password}")
                    file.truncate()
                return
    write_password(site, password)

def clean_csv():
    with open("pws.csv", "w") as file:
        file.write("Site,Password")

# def merge_duplicates():
#     with open("pws.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             name = row[0]
#             names[name] += 1

#menu drven program
while (True):
    print("\nMAIN MENU")
    print("Enter your choice")
    print("1.Generate Password\n2.Read Password\n3.Write Password\n4.Delete Password\n5.Update Password\n6.Clean File\n7.Exit")
    ch=int(input())
    if(ch==1):
        generate_password()
        break
    elif(ch==2):
        s=str(input("Enter the site for which password is to be set"))
        read_password(s)
        break
    elif(ch==3):
        s=str(input("Enter the site for which password is to be set"))
        p= generate_password()
        write_password(s,p)
        break
    elif(ch==4):
        s=str(input("Enter the site for which password is to be set"))
        delete_password(s)
        break
    elif(ch==5):
        s=str(input("Enter the site for which password is to be set"))
        p=generate_password()
        update_password(s,p)
        break
    elif(ch==6):
        clean_csv()
        break
    elif(ch==7):
        break
    else:
        print("Enter a valid choice")
        break

#content to be deleted after testing
fd = read_password("alergia")
print(f"Found Password: {fd}") #lines to be used for user choice function

print(f"Generated Password: {generate_password()}")
write_password("alergia", "1234567890")
update_password("alergia", "12345590")
delete_password("alergia")
clean_csv()
write_password("goggle", generate_password())
write_password("facebook", generate_password())
write_password("instagram", generate_password())
write_password("twitter", generate_password())
write_password("youtube", generate_password())
write_password("github", generate_password())
gog = read_password("goggle")
print(f"Goggle Password: {gog}")
read_password("facebook")
read_password("insta")
delete_password("goggle") #not working
delete_password("facebook") #not working

# def rp():
#     f = open("Names.csv", "r")
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     f.close()
