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
    print()
    print("1.Read Password\n2.Write Password\n3.Delete Password\n4.Update Password\n5.Clean File\n6.Exit")
    ch=int(input("\nChoice: "))
    if(ch==1):
        s=str(input("Enter the site: "))
        print(read_password(s))
    elif(ch==2):
        s=str(input("Enter the site: "))
        p= generate_password()
        write_password(s,p)
    elif(ch==3):
        s=str(input("Enter the site: "))
        delete_password(s)
    elif(ch==4):
        s=str(input("Enter the site: "))
        p=generate_password()
        update_password(s,p)
    elif(ch==5):
        clean_csv()
    elif(ch==6):
        break
    else:
        print("Enter a valid choice")
        break

# def rp():
#     f = open("Names.csv", "r")
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     f.close()
