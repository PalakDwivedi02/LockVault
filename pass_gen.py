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
    with open("pws.csv", "a") as file:
        str = alpha_lower+numbers+alpha_upper+symbols
        ch = "".join(random.sample(str, length))
        file.write("\n"+ch)
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

def delete_password(site):
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
read_password("goggle")
read_password("facebook")
read_password("insta")
delete_password("goggle")
delete_password("facebook")

# def rp():
#     f = open("Names.csv", "r")
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     f.close()